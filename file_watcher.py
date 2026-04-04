from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import time
import shutil
from datetime import datetime

# Path
VAULT_PATH = Path("C:/Users/Code Queen ❤/Desktop/Hackhaton 0/AI_Employee_Vault")

INBOX = VAULT_PATH / "Inbox"
NEEDS_ACTION = VAULT_PATH / "Needs_Action"

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        src = Path(event.src_path)
        dest = NEEDS_ACTION / src.name

        # file copy
        shutil.copy(src, dest)

        # markdown task file
        md_file = dest.with_suffix(".md")

        task_content = f"""
---
type: file_task
status: pending
created: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
---

## Task
Process file: {src.name}

## Actions
- [ ] Review file
- [ ] Take action
"""

        md_file.write_text(task_content)

        # Output
        print("\n📌 NEW TASK ADDED!")
        print("━━━━━━━━━━━━━━━━━━━━━━")
        print(f"📄 File: {src.name}")
        print(f"📍 Location: {md_file}")
        print(f"⏰ Time: {datetime.now().strftime('%H:%M:%S')}")
        print("✅ Status: Task created successfully")
        print("━━━━━━━━━━━━━━━━━━━━━━\n")


observer = Observer()
observer.schedule(Handler(), str(INBOX), recursive=False)
observer.start()

print("🚀 Watcher running... Waiting for new files...\n")

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()

observer.join()