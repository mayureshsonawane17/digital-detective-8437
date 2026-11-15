# Mission 1 — Know your computer

## 1. Task / objective
The objective of Mission 1 is to understand how computer systems work at a fundamental level. This includes:
- Tracing an everyday computing task through the **IPOS** (Input, Processing, Output, Storage) cycle.
- Identifying and categorizing different hardware components and software types (Operating System, Application, and Utility).
- Exploring real-world embedded or specialized computer systems around us outside of laptops and phones.

---

## 2. Work completed

### Task 1.1 — Trace one activity using IPOS
* **Chosen Activity:** Writing and saving a Python script in a text editor (VS Code).

| Stage | What happens in this activity? | Hardware / Component involved |
| :--- | :--- | :--- |
| **Input** | I type code on the keyboard and click menus with the trackpad. | Built-in keyboard, trackpad |
| **Processing** | The keyboard sends scan signals to the OS; the CPU calculates syntax highlighting, formats text, and stores the open file temporarily in working memory. | CPU (Processor) and RAM (Memory) |
| **Output** | The editor displays the code characters in real-time on the monitor. | Laptop screen / Retina Display |
| **Storage** | When I press `Cmd + S` (`Save`), the data held in temporary RAM is written to permanent storage so it remains safe after closing the app. | Internal SSD (Solid State Drive) |

#### Explanation of Activity Flow:
1. **Input to Processing:** Each keystroke generates an electrical interrupt signal. The OS keyboard driver receives this and passes keycodes to VS Code.
2. **Processing to Output:** The CPU executes the editor's rendering code, updating the display buffer in RAM, which the GPU outputs to the screen in milliseconds.
3. **Processing to Storage:** While editing, the document lives in volatile RAM. Once saved, the operating system's file system flushes the buffer to non-volatile flash storage (SSD), making the file durable.

---

### Task 1.2 — Identify hardware and software

| Item / software name | Hardware or software? | Software type (if applicable) | Purpose |
| :--- | :--- | :--- | :--- |
| **Keyboard** | Hardware | Not applicable | Used to enter characters, commands, and code. |
| **CPU (Processor)** | Hardware | Not applicable | The "brain" of the computer that executes instructions and calculations. |
| **RAM (Memory)** | Hardware | Not applicable | Fast, temporary storage for running programs and active data. |
| **Internal SSD** | Hardware | Not applicable | Permanent storage for files, applications, and the operating system. |
| **macOS** | Software | Operating System | Manages hardware resources, CPU scheduling, file systems, and security. |
| **Visual Studio Code** | Software | Application Software | Code editor used for writing, inspecting, and editing source code. |
| **Google Chrome** | Software | Application Software | Web browser used for research, viewing websites, and checking documentation. |
| **Terminal (zsh)** | Software | Utility Software | Command-line tool providing direct access to the operating system shell. |
| **macOS Activity Monitor** | Software | Utility Software | System monitoring utility to inspect CPU, memory usage, and running processes. |

---

### Task 1.3 — Computer systems around you

| System | Main purpose | One input | One output |
| :--- | :--- | :--- | :--- |
| **Automated Teller Machine (ATM)** | Allows bank customers to securely withdraw cash, check balances, or deposit money without a human teller. | Keypad / PIN pad (or Touchscreen selection) | Cash dispenser mechanism (or printed receipt / balance display) |
| **Smart Traffic Signal Controller** | Regulates intersection traffic automatically to prevent accidents and optimize traffic flow. | Inductive road loop sensors (or optical traffic cameras) | Colored signal lights (Red, Yellow, Green) and pedestrian walk signals |
| **Metro Ticket Vending Machine (TVM)** | Automatically dispenses transit tokens/tickets or recharges commuter smart cards. | Touchscreen destination selection (or smart card RFID tap) | Dispensed ticket/token (or screen confirmation showing updated balance) |

---

## 3. Commands / tools used
- **Text Editor (VS Code):** Used to draft, review, and format this documentation.
- **macOS System Information / Activity Monitor:** Used to verify installed hardware components (Apple Silicon CPU, RAM, SSD).
- **Git:** Used to stage, commit, and push this mission's work.

---

## 4. My understanding
- **The IPOS Cycle:** Every computer fundamentally works by taking raw input, processing it according to programmed rules, presenting output to a user, and saving it to storage when needed. Understanding this distinction helps in troubleshooting where a problem lies (e.g., whether an issue is input-related, CPU-related, or disk-related).
- **Software Types:**
  - *Operating System Software* acts as the manager between hardware and user programs (e.g., macOS, Windows, Linux).
  - *Application Software* lets the user accomplish specific tasks (e.g., VS Code for writing code, browsers for surfing the web).
  - *Utility Software* helps maintain, optimize, and diagnose the computer (e.g., Terminal, Disk Utility, Activity Monitor).
- **Everyday Systems:** Computers are not just laptops or smartphones; specialized embedded computers control everyday infrastructure like transportation, banking, and public utilities.

---

## 5. Difficulties faced
- No major difficulties were encountered while classifying components or explaining the IPOS cycle.

---

## 6. How I resolved them
- Not applicable.

---

## 7. Evidence / files
- `mission-01-computer-basics/README.md` (contains completed IPOS, hardware/software, and embedded systems tables).

---

## 8. Additional notes
- All tables and explanations have been verified and written in my own words.

---

## 9. Commit details
- **Commit message:** `Complete computer basics and IPOS mission`
- **Branch:** `main`
- **Pushed to:** `https://github.com/mayureshsonawane17/digital-detective-8437.git`
