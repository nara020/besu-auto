import os
import shutil
from pathlib import Path
import glob

# List of files and directories to remove
targets = [
    "config",
    "validators.json",
    "docker-compose.yml",
    ".env",
]
# Add node directories (not just data)
targets += [f"node{i}" for i in range(1, 6)]

def main():
    # Find all *ConfigFile.json files in current directory
    configfiles = glob.glob("*config.json")
    print("This will delete the following files and directories:")
    for t in targets:
        print(f"- {t}")
    for cf in configfiles:
        print(f"- {cf}")
    confirm = input("\nAre you sure you want to delete these? (y/N): ").strip().lower()
    if confirm != "y":
        print("Aborted.")
        return
    for t in targets:
        path = Path(t)
        if path.exists():
            if path.is_dir():
                shutil.rmtree(path)
                print(f"[Deleted directory] {t}")
            else:
                path.unlink()
                print(f"[Deleted file] {t}")
        else:
            print(f"[Not found] {t}")
    for cf in configfiles:
        path = Path(cf)
        if path.exists():
            path.unlink()
            print(f"[Deleted file] {cf}")
        else:
            print(f"[Not found] {cf}")
    print("\nCleanup complete.")

if __name__ == "__main__":
    main() 