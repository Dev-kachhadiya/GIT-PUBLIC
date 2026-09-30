# GitHub Basics

## 1. Repository (Repo)
- A repository is a project folder stored on GitHub.
- It contains your code, files, commit history, and project settings.
- Public repos are visible to everyone; private repos are restricted.

## 2. Clone a Repository
```bash
git clone <repository-url>
```
- This creates a local copy of the project on your computer.

## 3. Branches
- Branches let you work on different versions of a project.
- The default branch is usually `main` or `master`.

```bash
git checkout -b feature-name
```

## 4. Commit Changes
- A commit saves your changes with a message.

```bash
git add .
git commit -m "Add feature"
```

## 5. Push to GitHub
```bash
git push origin feature-name
```
- This uploads your branch to GitHub.

## 6. Pull Requests (PRs)
- A pull request is a request to merge changes from one branch into another.
- Used for code review before merging.
- Common workflow:
  1. Create a branch
  2. Make changes
  3. Commit and push
  4. Open a pull request
  5. Review and merge

## 7. Merge and Update Local Repo
```bash
git pull origin main
git checkout main
git merge feature-name
```

## 8. Issues
- Issues are used to track bugs, tasks, improvements, and discussions.
- Good for project planning and bug tracking.

## 9. README
- A `README.md` file explains what the project does.
- It often includes setup instructions, usage examples, and project info.

## 10. GitHub Actions
- GitHub Actions automate tasks like tests, builds, and deployments.
- Common use cases:
  - run unit tests
  - build the app
  - deploy to hosting

## 11. Forking
- Forking creates your own copy of someone else's repository.
- Useful when you want to contribute without changing the original project.

## 12. Useful Commands
```bash
git status
git log
git branch
git fetch
git pull
git push
git diff
```

## 13. Basic GitHub Workflow
```text
Create branch -> Make changes -> Commit -> Push -> Open PR -> Review -> Merge
```

## 14. Good Practices
- Use clear commit messages
- Keep branches small and focused
- Review code before merging
- Update your local repo regularly
- Write simple and useful README documentation

## 15. Common Terms
- `repo` = repository
- `commit` = saved change set
- `branch` = separate line of development
- `merge` = combine branches
- `PR` = pull request
- `push` = upload local changes to GitHub
- `pull` = download and merge changes from GitHub

## Quick Example
```bash
git clone https://github.com/username/project.git
cd project
git checkout -b fix-login
# make edits
 git add .
 git commit -m "Fix login bug"
 git push origin fix-login
```

This is a simple starting point for using GitHub effectively.
