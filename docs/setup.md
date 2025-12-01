# Environment setup (Windows PowerShell)

> Note: For the minimal assignment (Option A), setting up this environment is optional.
> You only need this if you want to run the example scripts or extend the project to Option B (actual ML modelling).


This project uses a Python virtual environment located at `.venv/` in the workspace root. VS Code is configured to use it automatically.

## 1) Prerequisites
- Python 3.10 installed (recommended for this project)
- VS Code with the Python extension

## 2) Create the venv (only if missing)
If `.venv` does not exist, create it using Python 3.10:

```powershell
# Option A: using py launcher
py -3.10 -m venv .venv

# Option B: using a direct Python path
C:\\Program Files\\Python310\\python.exe -m venv .venv
```

> Note: On some systems Python 3.13 may fail to create a venv due to a stdlib import issue. Use Python 3.10 instead.

## 3) Activate the venv
```powershell
.\\.venv\\Scripts\\Activate.ps1
```

If activation is blocked by policy, either:
```powershell
# Temporary for this session
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\\.venv\\Scripts\\Activate.ps1
```
Or set a permanent policy that allows local scripts:
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

## 4) Upgrade pip (optional)
```powershell
python -m pip install --upgrade pip
```

## 5) Install dependencies
```powershell
pip install -r requirements.txt
```

## 6) Jupyter kernel (current setup)
The kernel has been installed already with display name:

"Python (assignment_ML)"

If you ever need to (re)install it:
```powershell
python -m ipykernel install --user --name assignment_ml --display-name "Python (assignment_ML)"
```

Verify it's available:
```powershell
jupyter kernelspec list
```
Expected entries (paths will vary):
```
assignment_ml   C:\Users\<you>\AppData\Roaming\jupyter\kernels\assignment_ml
python3         .venv\share\jupyter\kernels\python3   
```

Select the kernel in VS Code via the Notebook kernel picker ("Python (assignment_ML)").

## 7) Run project tasks
Two VS Code tasks can help maintain the project:

1. "Refresh Project Overview" – runs `scripts/refresh_project_overview.py`.
2. "Check Environment" – runs `scripts/check_env.py` to verify packages.

Use: `Terminal > Run Task...` and choose the task.

Manual environment check (without task):
```powershell
python scripts/check_env.py
```

## 8) Script reference
| Script | Purpose |
|--------|---------|
| `scripts/refresh_project_overview.py` | (Existing) Generates or updates a summary about project state (extend as needed). |
| `scripts/check_env.py` | Verifies core dependencies, prints versions, runs a tiny KMeans clustering smoke test. |

## 9) Deactivate when done
```powershell
deactivate
```

## Troubleshooting
- If `py -3.10 -m venv .venv` is not found, verify that Python 3.10 is installed and registered with the py launcher (`py -0p`).
- If you used a different path for Python, update `.vscode/settings.json` to point to your venv:
  - `"python.defaultInterpreterPath": "${workspaceFolder}\\.venv\\Scripts\\python.exe"`
- If you change Python versions, recreate the venv and reinstall requirements.
- If the kernel does not appear, rerun the install command and then reopen VS Code.
- If environment check fails, reinstall dependencies:
  ```powershell
  pip install --force-reinstall -r requirements.txt
  ```
