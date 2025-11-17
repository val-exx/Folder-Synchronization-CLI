# Folder-Synchronization-CLI

A lightweight Python command-line tool that synchronizes the content of a source folder with a destination folder.  
The script copies new files, updates modified ones, and optionally removes obsolete files from the destination.  
All operations are logged in a timestamped `report.txt` file.

This project was created as a personal exercise to practice Python, filesystem management, and backend development concepts.

---

## 🚀 Features

- ✓ Copy files from the source folder to the destination if missing  
- ✓ Update destination files when their content differs from the source  
- ✓ Optional `--delete` logic: remove files in the destination that no longer exist in the source  
- ✓ Automatic creation of a backup folder if the destination does not exist  
- ✓ Detailed logging: updated, copied, and deleted files saved to `report.txt`  
- ✓ Uses only Python standard libraries (`pathlib`, `shutil`, `filecmp`, `datetime`, `os`)

---

## 📁 Project Structure
folder-sync-cli/  
├── main.py  
├── sync_manager.py  
├── report.txt  
├── documents  
└── backup

---

## 🧠 Logic Overview

### 1️⃣ Validate folders
- If the **source folder does not exist**, the program stops.
- If the **destination folder does not exist**, a default folder named `backup` is automatically created inside the parent directory of the source.

### 2️⃣ Copy or update files
For each file inside the source folder:
- If the file **does not exist** in the destination → it is **copied**.
- If the file exists but is **different** (`filecmp.cmp(..., shallow=False)`) → it is **updated**.

### 3️⃣ Optional deletion (`delete=True`)
If deletion is enabled:
- All files that **exist in the destination but not in the source** are identified using `dircmp`.
- These obsolete files are removed from the destination.

### 4️⃣ Logging
Every execution appends a new entry to **`report.txt`**, containing:
- Timestamp (`YYYY_MM_DD_HH_MM_SS`)
- List of updated files
- List of copied files
- List of deleted files (if enabled)

---

## 💻 Usage Example

### Basic synchronization: 
```bash
python sync.py --source "C:/Users/Vale/documents" --dest "D:/backup"
```
### Basic synchronization + delete obsolete files:
```bash
python sync.py --source "C:/Users/Vale/documents" --dest "D:/backup" --delete
```


