# Mission 4 — How programs run

## 1. Task / objective
The objective of Mission 4 is to understand how computer programs are translated and executed. This includes:
- Writing and executing a starter Python program (`hello.py`) from the Terminal.
- Comparing how compilers and interpreters work using a comparison table.
- Explaining the trade-offs between compiled and interpreted execution in my own words.

---

## 2. Work completed

### Task 4.1 — Create and run a Python program
1. Created `mission-04-programs/hello.py` containing:
   ```python
   print("Hello from Python")
   ```
2. Executed the program from the Terminal using:
   ```bash
   python3 mission-04-programs/hello.py
   ```
3. **Confirmed Output:**
   ```text
   Hello from Python
   ```

---

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | Translates the entire source code into machine code before the program runs. | Translates and executes instructions line by line on the fly while the program is running. |
| **Typical output** | Standalone machine code binary or executable file (e.g., `.exe` or Mach-O executable). | Executes directly in memory; does not produce a separate standalone executable file. |
| **One example** | C, C++, Rust, Go | Python, JavaScript, Ruby |
| **One advantage** | Runs much faster because the machine code executes directly on the CPU without translation overhead. | Faster development cycle, easier interactive debugging, and write-once-run-anywhere portability. |

#### Explanation of Differences:
A compiler translates the entire source code file into native machine code all at once before running, producing a standalone executable file that runs directly on the CPU. In contrast, an interpreter reads the source code line by line at runtime, translating and executing instructions on the fly without generating a separate binary. Because of this, compiled programs like C++ run much faster and are heavily optimized for performance, whereas interpreted languages like Python offer greater flexibility, rapid prototyping, and easier debugging across different operating systems.

---

## 3. Commands / tools used
- `python3 hello.py`: Executed the Python script using the Python 3 interpreter.
- Text Editor (VS Code): Created and saved `hello.py`.
- Git: Used to stage, commit, and push this mission.

---

## 4. My understanding
Computers only understand binary machine instructions (0s and 1s). Human-readable code written in high-level languages must be translated before the processor can run it. Compilers do all the translation upfront so the final binary runs at top speed, while interpreters trade runtime speed for developer convenience, translating code dynamically as it executes. Python actually compiles source code into intermediate bytecode (`.pyc`) first, and then the Python Virtual Machine (PVM) interprets that bytecode.

---

## 5. Difficulties faced
- No major difficulties encountered. The script ran immediately with `python3`.

---

## 6. How I resolved them
- Not applicable.

---

## 7. Evidence / files
- Python script: `mission-04-programs/hello.py`
- Documentation: `mission-04-programs/README.md`

---

## 8. Commit details
- **Commit message:** `Compare compilers and interpreters`
- **Branch:** `main`
- **Pushed to:** `https://github.com/mayureshsonawane17/digital-detective-8437.git`
