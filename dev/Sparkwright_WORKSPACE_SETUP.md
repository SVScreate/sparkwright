# Sparkwright Dev Workspace Setup

## Terminal Window Group: "Sparkwright"

Three tabs open simultaneously via **Window > Open Window Group > Sparkwright** (or set as default on Terminal launch via Terminal > Settings > General).

Each tab has its own color profile. Profiles configured in **Terminal > Settings > Profiles**.

### Tab 1 — Server
- **Purpose:** Runs local server and opens the game in Safari automatically
- **Run command (Shell tab):**
  ```
  cd ~/Desktop/sparkwright && python3 -m http.server 8000 & open -a Safari "http://localhost:8000/games/mathflash/"
  ```
- Check **"Run inside shell"** is checked

### Tab 2 — Claude
- **Purpose:** Claude Code session
- **Run command (Shell tab):**
  ```
  cd ~/Desktop/sparkwright && claude
  ```
- Check **"Run inside shell"** is checked

### Tab 3 — Git / Files
- **Purpose:** Git commands and file navigation
- **Run command (Shell tab):**
  ```
  cd ~/Desktop/sparkwright
  ```
- Check **"Run inside shell"** is checked

---

## Safari Tab Group: "Sparkwright"

4-tab group saved in Safari. Open manually at start of session.

1. `http://localhost:8000/games/mathflash/` — local test (also auto-opens from Server terminal)
2. `sparkwright.org` — live site
3. GitHub repo — source control
4. Netlify — deploy status

---

## Key Commands

| Action | Command |
|--------|---------|
| Start local server | `python3 -m http.server 8000` |
| Stop local server | `Ctrl + C` |
| Start Claude Code | `claude` |
| Open project folder in Finder | `open .` |
| Check git status | `git status` |
| See recent commits | `git log --oneline -10` |

## Local Test URL
`http://localhost:8000/games/mathflash/`
