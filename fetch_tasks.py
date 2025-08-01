# fetch_all_task_variants.py
import os, json, time, urllib.request, urllib.error, re

ORG               = "TaskBeacon"
EXCLUDED_REPOS    = {"task-registry", ".github","psyflow","taskbeacon-mcp","community","taskbeacon.github.io"}
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
    return re.sub(r'[\\/:*?"<>|]', '__', branch_name)

def get_md_title(file_path: str, default: str) -> str:
    """Extracts the first H1-level title from a Markdown file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("# "):
                    return line[2:].strip()
    except Exception as e:
        print(f"    - Could not read {file_path} to get title: {e}")
    return default

def download(url: str, dest: str, retries: int = MAX_RETRIES) -> bool:
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req) as response, open(dest, 'wb') as out_file:
                out_file.write(response.read())
            return True
        except urllib.error.HTTPError as e:
            if e.code == 404:
                # This is a common case, so no need to be noisy
                return False
            print(f"    - HTTP error {e.code} on attempt {attempt}/{retries}: {e}")
        except Exception as e:
            print(f"    - attempt {attempt}/{retries} failed: {e}")
        
        if attempt != retries:
            time.sleep(SLEEP_BETWEEN_SEC)
    print(f"    - Failed to download {url} after {retries} attempts.")
    return False

def fetch_branches(repo: str) -> list[str]:
    api = f"https://api.github.com/repos/{ORG}/{repo}/branches"
    req = urllib.request.Request(api, headers=HEADERS)
    with urllib.request.urlopen(req) as r:
        return [b["name"] for b in json.load(r)]

# ----------------------------------------------------------------------
print(f"Fetching repo list from {REPOS_API}")
with urllib.request.urlopen(urllib.request.Request(REPOS_API, headers=HEADERS)) as r:
    repos_json = json.load(r)

task_repos = [r["name"] for r in repos_json
              if not r["private"] and r["name"] not in EXCLUDED_REPOS]

print("Task repos:", task_repos)

master_index_entries = []

for repo in sorted(task_repos):
    print(f"\nProcessing {repo}")
    try:
        branches = fetch_branches(repo)
        print("   Branches:", branches)
    except Exception as e:
        print(f"   - Failed to fetch branches for {repo}: {e}")
        continue

    repo_dir = os.path.join(ROOT_TASKS_DIR, repo)
    os.makedirs(repo_dir, exist_ok=True)

    variants = {} # safe_name -> {md_path, title}

    for br in branches:
        safe_name  = safe_branch(br)
        dest_md    = os.path.join(repo_dir, f"{safe_name}.md")

        
        readme_url = RAW_URL.format(org=ORG, repo=repo, branch=br) + "README.md"


        print(f"  -> Fetching README.md for branch {br}")
        if download(readme_url, dest_md):
            title = get_md_title(dest_md, default=br)
            print(f"    + Saved as {dest_md} (Title: '{title}')")
            variants[safe_name] = {"md_path": dest_md, "title": title}

        else:
            print(f"    - README.md not found for branch {br}, skipping.")

    if not variants:
        print(f"   No variants with README.md found for {repo}, skipping index generation.")
        continue

    # Determine the main title for the task entry
    # Priority: title from 'main' branch, then first variant's title, then repo name
    main_title = repo
    if 'main' in variants:
        main_title = variants['main']['title']
    elif variants:
        main_title = next(iter(variants.values()))['title']

    # If there's only one variant, link directly to it in the master index.
    if len(variants) == 1:
        variant_name = next(iter(variants.keys()))
        master_index_entries.append(f"   {main_title} </Tasks/{repo}/{variant_name}>")
        print(f"   - Added direct link for single-variant task: {main_title}")
    
    # If there are multiple variants, create a separate index file for them.
    else:
        rst_path = os.path.join(ROOT_TASKS_DIR, f"{repo}_index.rst")
        with open(rst_path, "w", encoding="utf-8") as f:
            f.write(f"{main_title}\n{'='*len(main_title)}\n\n")
            f.write(".. toctree::\n   :maxdepth: 1\n   :caption: Variants\n\n")
            for v_name, v_data in sorted(variants.items()):
                f.write(f"   {v_data['title']} <{repo}/{v_name}>\n")
        
        master_index_entries.append(f"   {main_title} </Tasks/{repo}_index>")
        print(f"   - Wrote {rst_path} for multi-variant task: {main_title}")


# ----------------------------------------------------------------------
# Build the global task library index
master_rst = os.path.join("source", "tasks_index.rst")
with open(master_rst, "w", encoding="utf-8") as f:
    f.write(".. toctree::\n   :maxdepth: 1\n\n")
    # f.write("   Index <index>\n\n")
    for entry in sorted(master_index_entries):
        f.write(f"{entry}\n")
print(f"\n+ Wrote master index {master_rst}")
