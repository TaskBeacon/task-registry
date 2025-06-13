import os
import urllib.request

# Define all TaskBeacon repos to pull README.md from
tasks = {
    "SST": "https://raw.githubusercontent.com/TaskBeacon/SST/main/README.md",
    "MID": "https://raw.githubusercontent.com/TaskBeacon/MID/main/README.md",
    "REST": "https://raw.githubusercontent.com/TaskBeacon/REST/main/README.md",
    # Add more here as needed...
}

# Local output folder
task_dir = os.path.join("source", "Tasks")
os.makedirs(task_dir, exist_ok=True)

# Track successful downloads
successful_tasks = []

# Download .md files
for name, url in tasks.items():
    local_path = os.path.join(task_dir, f"{name}.md")
    try:
        print(f"📥 Downloading {name}...")
        urllib.request.urlretrieve(url, local_path)
        print(f"✅ Saved to {local_path}")
        successful_tasks.append(name)
    except Exception as e:
        print(f"❌ Failed to download {name}: {e}")

# Write only successfully downloaded tasks to tasks_index.rst
index_path = os.path.join("source", "tasks_index.rst")
with open(index_path, "w", encoding="utf-8") as f:
    f.write("Task Library\n")
    f.write("============\n\n")
    f.write(".. toctree::\n")
    f.write("   :maxdepth: 1\n")
    f.write("   :caption: Tasks\n\n")
    for name in successful_tasks:
        f.write(f"   Tasks/{name}\n")

print(f"🧾 Wrote task index with {len(successful_tasks)} tasks → {index_path}")