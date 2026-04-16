# Git Setup

This workspace comes pre-initialized as a Git repository with an initial commit. Follow these steps to push it to a remote.

---

## Option 1 — GitHub

```bash
# 1. Create a new empty repo on GitHub (via github.com/new)
#    Don't initialize with README / .gitignore / LICENSE — we have them already

# 2. Unzip the workspace and cd into it
unzip workspace.zip
cd workspace

# 3. Point to your new GitHub repo
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# 4. Push
git branch -M main
git push -u origin main
```

---

## Option 2 — GitLab

```bash
cd workspace
git remote add origin https://gitlab.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

---

## Option 3 — Self-hosted / other

```bash
cd workspace
git remote add origin YOUR_REMOTE_URL
git push -u origin main
```

---

## Recommended workflow

### Branching strategy

- `main` — always shippable, protected
- `project/[name]/feature-slug` — work on features per project
- Example: `project/alpha/US-101-guest-checkout`

### Commit convention

Follow Conventional Commits for readable history:

```
feat(alpha): add guest checkout (US-101)
fix(beta): correct email validation regex (BUG-042)
docs(team): update Design agent skills
chore: bump dependencies
refactor(alpha): extract PricingCalculator service
```

### Protect main

In GitHub settings, under "Branches":
- Require PR before merging to `main`
- Require 1 approval
- Require status checks to pass

This prevents accidental direct pushes and keeps main shippable.

---

## What's tracked

- All agent definitions (`team/`)
- All project contexts and state files (`projects/`)
- All shared resources (`shared/`)
- All specs and ADRs

## What's ignored

See `.gitignore` — OS files, editor configs, secrets, node_modules, build artifacts, scratch files.

---

## Working across multiple machines

Once pushed to a remote:

```bash
# On another machine
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
# Start working — all agents and projects are there
```

---

## Backing up decisions

Every decision made with an agent should end up as a file commit. The git log becomes the decision trail:

```bash
git log --oneline --graph projects/alpha/adr/
# shows the full history of architecture decisions for project alpha
```
