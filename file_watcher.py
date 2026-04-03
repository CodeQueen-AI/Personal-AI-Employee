# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# from pathlib import Path
# import time
# import shutil

# # 👉 STEP 1: PATH SET KARO (IMPORTANT)
# VAULT_PATH = Path("C:/Users/Code Queen ❤/Desktop/Hackhaton 0/AI_Employee_Vault")

# INBOX = VAULT_PATH / "Inbox"
# NEEDS_ACTION = VAULT_PATH / "Needs_Action"

# # 👉 STEP 2: DEBUG PRINTS (CHECK KARNE KE LIYE)
# print("VAULT:", VAULT_PATH)
# print("INBOX:", INBOX)
# print("INBOX EXISTS:", INBOX.exists())
# print("NEEDS_ACTION EXISTS:", NEEDS_ACTION.exists())

# # 👉 STEP 3: WATCHER CLASS
# class Handler(FileSystemEventHandler):
#     def on_created(self, event):
#         if event.is_directory:
#             return

#         src = Path(event.src_path)
#         dest = NEEDS_ACTION / src.name

#         shutil.copy(src, dest)

#         # markdown task create
#         md_file = dest.with_suffix(".md")

#         md_file.write_text(f"""
# ---
# type: file_task
# status: pending
# ---

# ## Task
# Process file: {src.name}

# ## Actions
# - [ ] Review file
# - [ ] Take action
# """)

#         print(f"✅ New task created: {md_file}")

# # 👉 STEP 4: OBSERVER START
# observer = Observer()
# observer.schedule(Handler(), str(INBOX), recursive=False)
# observer.start()

# print("🚀 Watcher running...")

# # 👉 STEP 5: LOOP
# try:
#     while True:
#         time.sleep(5)
# except KeyboardInterrupt:
#     observer.stop()

# observer.join()




from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import time
import shutil
from datetime import datetime

# 👉 PATH
VAULT_PATH = Path("C:/Users/Code Queen ❤/Desktop/Hackhaton 0/AI_Employee_Vault")

INBOX = VAULT_PATH / "Inbox"
NEEDS_ACTION = VAULT_PATH / "Needs_Action"

print("VAULT:", VAULT_PATH)
print("INBOX:", INBOX)
print("INBOX EXISTS:", INBOX.exists())
print("NEEDS_ACTION EXISTS:", NEEDS_ACTION.exists())


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

        # 🔥 IMPROVED OUTPUT
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