# Mission 0 — Create your GitHub workspace

## 1. Task / objective
The objective of Mission 0 was to set up a clean, structured workspace for the Digital Detective assignment. This involved verifying essential development tools (Python 3 and Git), establishing a local directory named `digital-detective-8437`, generating the mission folder scaffold, creating the root `README.md` with a mission index, and publishing the initial repository to GitHub.

## 2. Work completed
- Checked and confirmed the installations and versions of Python 3 and Git in the Terminal.
- Verified the local directory name `digital-detective-8437` matching the required pattern (`assignment-name + hyphen + last 4 digits of USN`).
- Created all nine mission directories (`mission-00-setup` through `mission-08-final-report`) and the `evidence/` folder.
- Added empty placeholder `README.md` files inside every mission directory, plus `number_converter.py` inside `mission-05-numbers-data/`.
- Written the root `README.md` containing an overview, mission index table with markdown navigation links, and project guidelines.
- Connected the local project directory to GitHub at `https://github.com/mayureshsonawane17/digital-detective-8437.git`.

## 3. Commands / tools used
- `python3 --version`: Verified the Python runtime environment. Output: `Python 3.9.6`.
- `git --version`: Verified the Git version control system. Output: `git version 2.54.0 (Apple Git-157)`.
- `mkdir`: Used to create mission directories and the `evidence` folder.
- `touch`: Used to generate the required Markdown documentation files and Python source files.
- `git status`: Inspected the repository tree and tracked vs untracked file status.
- `git remote -v`: Confirmed the remote GitHub repository URL mapping.
- `git push`: Published the project repository to the public GitHub remote.

## 4. My understanding
- **What a repository is:** A Git repository is a managed storage structure that tracks the entire evolutionary history of a project. Instead of manually saving multiple copies of folders, Git records snapshots of changes (commits), allowing us to inspect history, revert mistakes, and collaborate safely.
- **Why organizing by mission matters:** Segmenting the project into dedicated mission folders keeps the repository clean, modular, and easy to navigate. Each mission represents a discrete learning topic, and having a dedicated folder and `README.md` ensures that documentation, code, and evidence remain self-contained rather than cluttering the root folder.

## 5. Difficulties faced
- No major difficulties were encountered during the directory setup or tool verification process.

## 6. How I resolved them
- Not applicable.

## 7. Evidence / files
- Root index: `README.md`
- Mission setup file: `mission-00-setup/README.md`
- Directory scaffold:
  - `mission-01-computer-basics/README.md`
  - `mission-02-terminal/README.md`
  - `mission-03-operating-system/README.md`
  - `mission-04-programs/README.md`
  - `mission-05-numbers-data/README.md` and `number_converter.py`
  - `mission-06-git-github/README.md`
  - `mission-07-networking/README.md`
  - `mission-08-final-report/README.md`
  - `evidence/`

## 8. Commit details
- **Commit message:** `Set up Digital Detective mission structure`
- **Branch:** `main`
- **Pushed to:** `https://github.com/mayureshsonawane17/digital-detective-8437.git`
