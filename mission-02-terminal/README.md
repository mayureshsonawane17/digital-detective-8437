Mission 2

## 1. Task / objective
The objective of Mission 2 is to gain confidence working with the command-line interface (CLI) on macOS. This involves:
- Practicing core navigation, file creation, inspection, and manipulation commands.
- Safely creating, modifying, copying, and renaming files in an isolated practice directory.
- Understanding command-line flags and the Unix pipe (`|`) operator.
- Checking the system package manager (Homebrew) and explaining its role in software management.

---

## 2. Work completed

### Task 2.1 — Explore basic Terminal operations

| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display (`pwd`)** | Prints the full absolute path of the directory I am currently inside. | Displayed `/Users/[redacted]/Desktop/digital-detective-8437`. |
| **Directory listing (`ls`)** | Lists the visible files and folders in the current working directory. | Showed all mission folders, `README.md`, and `evidence/` in plain columns. |
| **Detailed listing (`ls -l`)** | Lists directory contents in long format showing file permissions, owner, size, and modification date. | Listed each entry on its own line with attributes like `drwxr-xr-x` and byte counts. |
| **Change directory (`cd ..` and `cd <dir>`)** | Moves the shell session to the parent directory or into a target subfolder. | Moving `cd ..` changed path to the Desktop; `cd digital-detective-8437` returned inside the project. |
| **Create directory (`mkdir terminal-practice`)** | Creates a new folder at the specified path. | A new directory named `terminal-practice` was created without error. |
| **Create empty file (`touch notes.txt`)** | Creates a new blank file or updates the timestamp of an existing file. | An empty file `notes.txt` was created inside `terminal-practice/` with 0 bytes. |
| **Copy file (`cp notes.txt notes_backup.txt`)** | Duplicates an existing file to a new target path while preserving the original. | Created a second identical copy `notes_backup.txt` alongside `notes.txt`. |
| **Move / rename file (`mv notes_backup.txt notes_archive.txt`)** | Relocates or renames a file from source to destination. | `notes_backup.txt` was renamed to `notes_archive.txt`; the old name disappeared. |
| **Display file contents (`cat notes.txt`)** | Reads and outputs the contents of a text file directly to the terminal screen. | Displayed the two written lines from the practice file in Terminal. |

---

### Task 2.2 — Practise file changes safely
Inside the `terminal-practice/` folder, I performed the following:
1. Created `notes.txt` and added a first line using single redirection (`>`):
   ```bash
   echo "First line: Digital Detective practice file." > notes.txt
   ```
2. Appended a second line without erasing the first using append redirection (`>>`):
   ```bash
   echo "Second line: Appending text without overwriting." >> notes.txt
   ```
3. Displayed the file with `cat notes.txt` and confirmed both lines were present.
4. Created a backup with `cp notes.txt notes_backup.txt` and renamed it with `mv notes_backup.txt notes_archive.txt`.

#### Questions Answered:
* **What is the difference between replacing a file's contents and adding text to the end?**  
  Using `>` (overwrite) erases whatever content previously existed in the file and replaces it with the new output. Using `>>` (append) preserves the existing contents and attaches the new text at the end of the file.
* **What is the difference between copying a file and moving a file?**  
  Copying (`cp`) duplicates the file so that both the original and new file exist independently. Moving (`mv`) relocates or renames the file so only the new destination exists; the original path is removed.
* **What information does the current-directory display provide?**  
  `pwd` (Print Working Directory) provides the complete absolute path starting from the root directory (`/`). It helps me know exactly where I am in the filesystem hierarchy so I don't accidentally create or modify files in the wrong folder.
* **Why is a directory-listing operation useful?**  
  `ls` allows me to immediately see what files and directories exist in my current location, check whether newly created files are present, and verify their names and extensions before running commands on them.

---

### Task 2.3 — Understand flags and pipes

#### Flags (`ls` vs `ls -lah`):
* `ls` simply outputs file and folder names without extra information.
* `ls -lah` adds three options (flags):
  * `-l`: Uses the long listing format (shows permissions, owner, size, timestamp).
  * `-a`: Includes hidden files and folders that start with a dot (such as `.git`).
  * `-h`: Converts file sizes from raw bytes into human-readable units (like `480B`, `2.1K`, `3.1K`).
* **Observation:** Running `ls -lah` revealed hidden directories like `.git` and `.` / `..`, and made file sizes much easier to understand at a glance compared to raw byte numbers.

#### Unix Pipes (`|`):
I tested sending directory output through a pipe into `head`:
```bash
ls -lah | head -n 5
```
* **What the pipe symbol (`|`) does:** The pipe takes the standard output (`stdout`) of the command on the left and redirects it directly into the standard input (`stdin`) of the command on the right without creating intermediate temporary files.
* **Left side contribution (`ls -lah`):** Produces a full detailed list of all files and folders.
* **Right side contribution (`head -n 5`):** Reads the incoming stream and filters it so only the first 5 lines are printed to the terminal.

---

### Task 2.4 — Understand package managers
* **Homebrew Version Check:** Tested on my Mac using `brew --version`.
  * **Result:** `Homebrew 7.0.13` is installed and active.
  * **Sample managed packages:** Verified with `brew list --formula` (examples installed include `ca-certificates`, `ffmpeg`, etc.).
* **Why package managers are useful:**  
  A package manager automates finding, downloading, compiling, installing, updating, and removing software tools and libraries from the command line. Instead of manually downloading installer packages from websites and figuring out dependencies by hand, a package manager resolves all prerequisites automatically with a single command (like `brew install <tool>`), keeping the system organized and up to date.

---

## 3. Commands / tools used
- `pwd`: Displayed working directory path.
- `ls`, `ls -l`, `ls -lah`: Inspected directory contents with varying levels of detail.
- `cd`: Navigated between folders.
- `mkdir`: Created `terminal-practice` folder.
- `touch`: Created initial practice files.
- `echo` with `>` and `>>`: Wrote and appended text lines safely.
- `cat`: Displayed file text in the terminal.
- `cp`: Duplicated files for backup purposes.
- `mv`: Renamed backup files.
- `|` (Pipe) with `head -n 5`: Filtered multi-line terminal output.
- `brew --version` & `brew list`: Verified package manager status on macOS.

---

## 4. My understanding
The command line is much faster and more scriptable than a graphical user interface once you know the core commands. Understanding how `>` and `>>` differ is critical to prevent accidental data loss. Furthermore, the Unix philosophy of small tools doing one job well—connected together using pipes (`|`)—allows us to build powerful one-line workflows directly in the shell.

---

## 5. Difficulties faced
- No major difficulties. Commands were executed inside the designated `terminal-practice/` folder to prevent affecting any system or project files.

---

## 6. How I resolved them
- Not applicable.

---

## 7. Evidence / files
- Mission documentation: `mission-02-terminal/README.md`
- Practice directory created: `terminal-practice/`
  - `notes.txt`
  - `notes_archive.txt`

---

## 8. Additional notes
- Personal usernames and private paths have been redacted as `[redacted]` to preserve privacy.

---

## 9. Commit details
- **Commit message:** `Complete Terminal and file management mission`
- **Branch:** `main`
- **Pushed to:** `https://github.com/mayureshsonawane17/digital-detective-8437.git`
