from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import time
import shutil

# 👉 CHANGE THIS PATH
VAULT_PATH = Path(r"C:\Users\Code Queen ❤\Desktop\Hackhaton 0")

INBOX = VAULT_PATH / "Inbox"
NEEDS_ACTION = VAULT_PATH / "Needs_Action"

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        src = Path(event.src_path)
        dest = NEEDS_ACTION / src.name

        shutil.copy(src, dest)

        # create markdown task
        md_file = dest.with_suffix(".md")

        md_file.write_text(f"""
---
type: file_task
status: pending
---

## Task
Process file: {src.name}

## Actions
- [ ] Review file
- [ ] Take action
""")

        print(f"✅ New task created: {md_file}")

observer = Observer()
observer.schedule(Handler(), str(INBOX), recursive=False)
observer.start()

print("🚀 Watcher running...")

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()

observer.join()