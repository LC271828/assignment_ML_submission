"""Quick environment verification script.

Checks:
1. Imports core packages from requirements.txt
2. Prints versions
3. Runs a minimal pandas DataFrame creation
4. Executes a simple scikit-learn KMeans clustering
5. (Optional) Matplotlib backend availability

Run with: python scripts/check_env.py
"""
from __future__ import annotations
import importlib
import sys

REQUIRED = [
    "numpy",
    "pandas",
    "scipy",
    "sklearn",  # scikit-learn
    "matplotlib",
    "seaborn",
    "ipykernel",
    "jupyter"
]

missing = []
versions = {}
for name in REQUIRED:
    try:
        mod = importlib.import_module(name)
        ver = getattr(mod, "__version__", "<no __version__>")
        versions[name] = ver
    except Exception as e:  # broad: we want any import failure noted
        missing.append((name, repr(e)))

print("Python:", sys.version.split()[0])
print("Environment check: core package versions")
for k, v in versions.items():
    print(f" - {k:12s} : {v}")

if missing:
    print("\nMissing or failed imports:")
    for name, err in missing:
        print(f" - {name}: {err}")
    print("\nFAIL: Environment incomplete.")
    sys.exit(1)

# Simple functionality tests
print("\nFunctional tests:")
try:
    import numpy as np
    import pandas as pd
    from sklearn.cluster import KMeans

    df = pd.DataFrame({"x": [1, 2, 3, 10, 11, 12], "y": [1, 1, 2, 10, 11, 12]})
    X = df.values
    km = KMeans(n_clusters=2, n_init=10, random_state=42)
    labels = km.fit_predict(X)
    print(" - KMeans cluster labels:", labels.tolist())
    print(" - KMeans centers:\n", km.cluster_centers_)
except Exception as e:
    print(" - KMeans test FAILED:", repr(e))
    print("\nFAIL: Core ML functionality issue.")
    sys.exit(2)

# Matplotlib backend quick check (avoid opening windows)
try:
    import matplotlib
    backend = matplotlib.get_backend()
    print(f" - Matplotlib backend: {backend}")
except Exception as e:
    print(" - Matplotlib backend check FAILED:", repr(e))

print("\nSUCCESS: Environment appears healthy.")
