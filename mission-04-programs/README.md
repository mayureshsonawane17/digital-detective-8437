Mission 4 — How programs run


Task 4.1 — Create and run a Python program
1. Created `mission-04-programs/hello.py` containing:
   ```python
   print("Hello from Python")
   ```
2. Executed the program from the Terminal using:
   ```bash
   python3 mission-04-programs/hello.py
   ```
3. Confirmed Output:
   ```text
   Hello from Python
   ```

---

Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| When translation / execution happens | Translates the entire source code into machine code before the program runs. | Translates and executes instructions line by line on the fly while the program is running. |
| Typical output | Standalone machine code binary or executable file (e.g., `.exe` or Mach-O executable). | Executes directly in memory; does not produce a separate standalone executable file. |
| One example | C, C++, Rust, Go | Python, JavaScript, Ruby |
| One advantage | Runs much faster because the machine code executes directly on the CPU without translation overhead. | Faster development cycle, easier interactive debugging, and write-once-run-anywhere portability. |

Explanation of Differences:
A compiler translates the entire source code file into native machine code all at once before running, producing a standalone executable file that runs directly on the CPU. In contrast, an interpreter reads the source code line by line at runtime, translating and executing instructions on the fly without generating a separate binary. Because of this, compiled programs like C++ run much faster and are heavily optimized for performance, whereas interpreted languages like Python offer greater flexibility, rapid prototyping, and easier debugging across different operating systems.

