Mission 6 

Task 6.1

| Git operation | What it does in your own words |

| Check repository status | Running git status checks which files have been modified, which are staged in the index, and which are untracked. |
| Stage selected changes | Running git add stages specific modified files to the staging area (index) to prepare them for the next snapshot. |
| Create a commit | Running git commit captures a permanent, named snapshot of all currently staged changes along with a log message. |
| View commit history | Running git log shows the chronological timeline of previous commits, authors, dates, and commit hashes. |

Difference between staging and committing:
Staging (git add) is like putting selected items into a box before sealing it; it lets you choose exactly which changes should be part of the next revision. Committing (git commit) is sealing and labeling the box, permanently recording that snapshot into the repository history with a unique cryptographic hash and descriptive message.



Task 6.2 
1. Created and switched to a new branch named update-about:
   git checkout -b update-about
2. Added a My Learning section in the root README.md summarizing what I learned in Missions 0 through 5.
3. Staged and committed the change:
   git commit -m "Add My Learning section to root README"
4. Published the branch to GitHub:
   git push -u origin update-about

-

Task 6.3 
1. Opened the repository on GitHub and located the update-about branch.
2. Created Pull Request 1 targeting the main branch with a description of the README updates.
3. Reviewed the diff and completed the merge into main on GitHub.
4. Switched back to the local main branch and pulled the remote merge commit:
   git checkout main
   git pull origin main
   Successfully fast-forwarded to commit 2a9491e: "Merge pull request 1 from mayureshsonawane17/update-about".

Why branches and Pull Requests are useful:
A branch creates an isolated workspace where a developer can build a feature, test an idea, or fix a bug without risking bugs on the stable main branch. A Pull Request (PR) allows team members to review code, discuss changes, run automated tests, and ensure code quality before merging the work into production.



Task 6.4

- Initialise a repository (git init): Creates a new, blank Git version control repository inside the current folder.
- Check status (git status): Displays the current working tree state, including modified, staged, and untracked files.
- Stage changes (git add): Moves modified files from the working directory into the staging area (index) for the next commit.
- Commit changes (git commit -m): Records a permanent snapshot of the staged files into the project history with a log message.
- View history (git log): Lists the chronological history of commits made to the current branch.
- Create or list branches (git branch): Lists all existing local branches or creates a new branch pointer.
- Switch branches (git switch / git checkout): Moves the working directory HEAD pointer to a different branch.
- Publish changes (git push): Uploads local commits to a remote repository like GitHub.
- Retrieve remote changes (git pull): Fetches and merges the latest changes from the remote branch into the local repository.
