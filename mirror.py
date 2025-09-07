import git
import os

# --- Configuration ---
SOURCE_REPO = "https://github.com/theUser0011/source-repo.git"
DEST_REPO = "https://theUser0011:{PAT}@github.com/theUser0011/fork-repo.git"  # PAT injected below
LOCAL_DIR = "./temp-mirror"
PAT = os.environ.get("ACCOUNT2_PAT")  # store your PAT as env variable for safety

# --- Replace PAT in URL ---
DEST_REPO = DEST_REPO.format(PAT=PAT)

# --- Clone or update the source repo ---
if not os.path.exists(LOCAL_DIR):
    print(f"Cloning source repo to {LOCAL_DIR}...")
    repo = git.Repo.clone_from(SOURCE_REPO, LOCAL_DIR)
else:
    print(f"Pulling latest changes in {LOCAL_DIR}...")
    repo = git.Repo(LOCAL_DIR)
    origin = repo.remotes.origin
    origin.pull()

# --- Add or update mirror remote ---
if "mirror" not in [r.name for r in repo.remotes]:
    repo.create_remote("mirror", DEST_REPO)
else:
    repo.remotes.mirror.set_url(DEST_REPO)

# --- Push all branches and tags to mirror ---
print("Pushing to mirror repo...")
repo.remotes.mirror.push(refspec="--all", force=True)
repo.remotes.mirror.push(refspec="--tags", force=True)

print("✅ Mirror completed successfully!")
