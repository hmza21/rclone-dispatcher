import subprocess
import requests
import json
import time
import sys
import os

with open(os.path.join(os.path.dirname(__file__), 'config.json'), 'r') as file:
    config: dict = json.load(file)

remotes: list[dict] = config.get('remotes', [])

print("Rclone monitor starting. Checking internet connection...")

while True:
    try:
        res = requests.get("https://www.google.com")
        if res.status_code == 200:
            break

    except requests.RequestException:
        time.sleep(config.get("interval", 5))
    
    print("No internet connection. Retrying...")

print("Internet connected. Starting rclone...")

for remote in remotes:
    try:
        remote_name = remote.get('name')
        remote_dir = remote.get('dir')
        base_dir = config.get('base_dir', '')
        if not remote_name or not remote_dir or not base_dir:
            print(f"Invalid remote configuration: {remote}")
            continue

        mount_path = os.path.abspath(os.path.join(base_dir, remote_dir))
        subprocess.run([
            "rclone", "mount",
            f"{remote_name}:",
            mount_path,
            "--vfs-cache-mode", "full",
            "--vfs-cache-max-size", "10G",
            "--dir-cache-time", "12h",
            "--poll-interval", "15s",
            "--daemon"
        ], check=True)
        
    except Exception as e:
        print("Rclone error: ", e)
        sys.exit(1)

print("Rclone dispatcher done. Exiting...")
sys.exit(0)
