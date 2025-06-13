# fetch_all_task_variants.py
import os, json, time, urllib.request, urllib.error, re

ORG               = "TaskBeacon"
EXCLUDED_REPOS    = {"taskbeacon.github.io", ".github", "task_index","nback","MID","Rest","PRL",'Movie','psyflow'}
MAX_RETRIES       = 3           # attempts per download
SLEEP_BETWEEN_SEC = 2           # wait between retries

HEADERS = {                     # add a token here if you hit rate-limits
    "User-Agent": "TaskBeacon-variant-fetcher"
}

RAW_URL  = "https://raw.githubusercontent.com/{org}/{repo}/{branch}/"
REPOS_API = f"https://api.github.com/orgs/{ORG}/repos"

ROOT_TASKS_DIR   = os.path.join("source", "Tasks")
os.makedirs(ROOT_TASKS_DIR, exist_ok=True)

def safe_branch(branch_name: str) -> str:
    """Make branch name filesystem-safe (convert / to __ etc.)."""
    return re.sub(r"[\\/:*?\"<>|]", "__", branch_name)

def download(url: str, dest: str, retries: int = MAX_RETRIES) -> bool:
    for attempt in range(1, retries + 1):
        try:
            urllib.request.urlretrieve(url, dest)
            return True
        except Exception as e:
            print(f"    ⚠️  attempt {attempt}/{retries} failed: {e}")
            if attempt != retries:
                time.sleep(SLEEP_BETWEEN_SEC)
    return False

def fetch_branches(repo: str) -> list[str]:
    api = f"https://api.github.com/repos/{ORG}/{repo}/branches"
    req = urllib.request.Request(api, headers=HEADERS)
    with urllib.request.urlopen(req) as r:
        return [b["name"] for b in json.load(r)]

# ----------------------------------------------------------------------
print(f"🔍 Fetching repo list from {REPOS_API}")
with urllib.request.urlopen(urllib.request.Request(REPOS_API, headers=HEADERS)) as r:
    repos_json = json.load(r)

task_repos = [r["name"] for r in repos_json
              if not r["private"] and r["name"] not in EXCLUDED_REPOS]

print("📦 Task repos:", task_repos)

master_index_entries = []

for repo in task_repos:
    print(f"\n📂 Processing {repo}")
    branches = fetch_branches(repo)
    print("   Branches:", branches)

    repo_dir = os.path.join(ROOT_TASKS_DIR, repo)
    os.makedirs(repo_dir, exist_ok=True)

    ok_variants = []

    for br in branches:
        safe_name  = safe_branch(br)
        dest_file  = os.path.join(repo_dir, f"{safe_name}.md")
        raw_url    = RAW_URL.format(org=ORG, repo=repo, branch=br) + "README.md"

        print(f"  ↳ Fetching {raw_url}")
        if download(raw_url, dest_file):
            print("    ✅ saved as", dest_file)
            ok_variants.append(safe_name)
        else:
            print("    ❌ giving up")
        meta_url  = RAW_URL.format(org=ORG, repo=repo, branch=br) + "meta.json"
        meta_dest = os.path.join(repo_dir, f"{safe_name}.meta.json")
        if download(meta_url, meta_dest):
            print("  ✅  meta.json saved",meta_dest)
        else:
            print("    ❌ giving up")

    # make per-task rst if we downloaded at least one variant
    if ok_variants:
        rst_path = os.path.join(ROOT_TASKS_DIR, f"{repo}_index.rst")
        with open(rst_path, "w", encoding="utf-8") as f:
            f.write(f"{repo} variants\n{'='*(len(repo)+9)}\n\n")
            f.write(".. toctree::\n   :maxdepth: 1\n   :caption: Variants\n\n")
            for v in ok_variants:
                f.write(f"   {repo}/{v}\n")
        master_index_entries.append(f"Tasks/{repo}_index")
        print(f"   🧾 wrote {rst_path}")

# ----------------------------------------------------------------------
# build the global task library index
master_rst = os.path.join("source", "tasks_index.rst")
with open(master_rst, "w", encoding="utf-8") as f:
    f.write("Task Library\n============\n\n")
    f.write(".. toctree::\n   :maxdepth: 1\n   :caption: Tasks\n\n")
    for entry in sorted(master_index_entries):
        f.write(f"   {entry}\n")
print(f"\n✅ Wrote master index {master_rst}")
