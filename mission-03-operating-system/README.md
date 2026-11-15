 Mission 3 

Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |

Operating system / system details| Shows the operating system name, kernel version, and hardware architecture. | macOS (Darwin Kernel 27.2.0 on `arm64` Apple Silicon architecture). |
Current account identity | Displays the username of the account running the current shell session. | `[redacted]` (retrieved with `whoami` and kept private). |
Available and used storage | Shows total disk space, used space, free space, and mount points. | Disk `/dev/disk3s1s1`: `460Gi` total size, `13Gi` used, `309Gi` available (Mounted on `/`). |
System activity snapshot | Displays currently active processes, CPU load, and memory usage. | Captured running system snapshot showing active background daemons and applications. |


Task 3.2 

What is a process?
  A process is a program in execution. When a program is stored on disk, it is just passive code; when opened, the OS loads it into RAM and allocates CPU time and resources to run it as an active process.
What does the PID column represent?
  PID stands for **Process Identifier**. It is a unique numerical ID assigned by the operating system to every running process so the OS can track, schedule, prioritize, and terminate it.
Two examples of processes running on my computer:
  1. `launchd` (PID `1`): The primary parent process / system daemon on macOS that starts and manages all other background services.
  2. `Google Chrome` (PID `20498`): A user-level web browser application process running in the background.



Task 3.3 

 Absolute vs Relative Paths:
Absolute Path: The complete path starting from the root directory (`/`). It always points to the exact same location regardless of where you currently are.  
  Example from my repo: `/Users/[redacted]/Desktop/digital-detective-8437/mission-03-operating-system`
Relative Path: A path defined relative to the current working directory you are in.  
  Example from my repo: `mission-03-operating-system/README.md` (or `../terminal-practice` when inside a subfolder).

File Permissions:

| Permission | Meaning | Example |
| :--- | :--- | :--- |
| r — Read | Allows viewing or opening the file's contents. On directories, allows listing contents. | Opening a document in an editor. |
| w — Write | Allows modifying, editing, or deleting the file. On directories, allows adding or removing files. | Saving changes to a text file. |
| x — Execute | Allows running the file as a program or script. On directories, allows entering/traversing into it. | Running a bash script or Python program. |

My File Observation: Running `ls -l` on `terminal-practice/notes.txt` showed permissions `-rw-r--r--`.  
   The owner has `rw-` permissions, meaning the owner can Read and Write the file, but cannot Execute it.

---

Task 3.4

| Process management | Controls process creation, CPU scheduling, prioritization, and termination so multiple programs can run simultaneously. | Allocating CPU time slices between Chrome, VS Code, and Terminal. |
| Memory management | Allocates and tracks RAM space for running programs and prevents one program from corrupting another's memory. | Freeing up RAM when an application is closed. |
| Device management | Communicates with hardware components and peripherals using device drivers. | Sending print jobs to a printer or reading input from a USB mouse. |
| File management | Organizes how data is structured, saved, named, retrieved, and protected on storage disks. | Managing directories and files using the APFS file system on macOS. |
| User interface / shell | Provides a way for users to interact with the computer, either graphically (GUI) or through text commands (CLI). | The macOS Aqua desktop GUI and the Terminal command line. |
| Security and permissions | Controls user access to files, devices, and system resources to protect against unauthorized changes. | Prompting for user password/Touch ID when running administrative actions. |

