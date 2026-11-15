Mission 2

Task 2.1 
Operation           |Command                |What it does
Current directory.  |pwd                    |Prints the full path of the folder I’m in
List	            |ls	                    |Shows files and folders here
Detailed list.      |ls -l              	|Shows permissions, owner, size and date
Change directory	|cd ..	                |Moves to the parent folder
Create directory	| mkdir                 |terminal-practice	Makes a new folder
Create empty file	|touch notes.txt        |Makes an empty file
Copy	            |cp notes.txt copy.txt  |Duplicates the file
Move/rename	        |mv copy.txt backup.txt |Renames or moves the file
Display contents	|cat notes.txt.         | 	Prints the file’s contents



Task 2.2
echo "line one" > notes.txt
echo "line two" >> notes.txt
cat notes.txt
cp notes.txt notes-backup.txt
mv notes-backup.txt backup.txt

What is the difference between replacing a file's contents and adding text to the end?
  Using `>` (overwrite) erases whatever content previously existed in the file and replaces it with the new output. Using `>>` (append) preserves the existing contents and attaches the new text at the end of the file.
What is the difference between copying a file and moving a file? 
  Copying (`cp`) duplicates the file so that both the original and new file exist independently. Moving (`mv`) relocates or renames the file so only the new destination exists; the original path is removed.
What information does the current-directory display provide?
  `pwd` (Print Working Directory) provides the complete absolute path starting from the root directory (`/`). It helps me know exactly where I am in the filesystem hierarchy so I don't accidentally create or modify files in the wrong folder.
Why is a directory-listing operation useful?
  `ls` allows me to immediately see what files and directories exist in my current location, check whether newly created files are present, and verify their names and extensions before running commands on them.

---

Task 2.3 

 (`ls` vs `ls -lah`):
 `ls` simply outputs file and folder names without extra information.
 `ls -lah` adds three options (flags):
   `-l`: Uses the long listing format (shows permissions, owner, size, timestamp).
   `-a`: Includes hidden files and folders that start with a dot (such as `.git`).
   `-h`: Converts file sizes from raw bytes into human-readable units (like `480B`, `2.1K`, `3.1K`).


Task 2.4

Homebrew version : `Homebrew 7.0.13` is installed and active.
  Sample managed packages: Verified with `brew list --formula` (examples installed include `ca-certificates`, `ffmpeg`, etc.).
  Why package managers are useful:* 
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
