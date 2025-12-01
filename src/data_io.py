"""
data_io.py
Utility functions for loading supervised and unsupervised datasets
for the Machine Learning 2 group assignment.

This prevents teammates from:
- accidentally loading the wrong file
- including the supervised target in clustering
- using inconsistent paths across notebooks
"""

from pathlib import Path
from functools import lru_cache
import os
import pandas as pd
import numpy as np
try:
    import yaml
except ImportError:  # graceful fallback; users should install PyYAML from requirements.txt
    yaml = None


# ---------------------------------------------------
# Base paths (adjust here if project moves)
# ---------------------------------------------------
ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"
CONFIG_PATH = ROOT / "config.yaml"


# ---------------------------------------------------
# Configuration helpers
# ---------------------------------------------------
@lru_cache(maxsize=1)
def get_config() -> dict:
    """
    Load configuration from config.yaml (once, cached).
    Fallback to sane defaults if file is missing or PyYAML unavailable.
    """
    # Allow override via env var (absolute or relative to ROOT)
    env_path = os.getenv("ASSIGNMENT_ML_CONFIG")
    cfg_path = Path(env_path) if env_path else CONFIG_PATH
    if not cfg_path.is_absolute():
        cfg_path = ROOT / cfg_path

    default_cfg = {
        "paths": {
            "supervised": "data/raw/clean_supervised.csv",
            "unsupervised": "data/raw/clean_unsupervised.csv",
        },
        "supervised": {
            "target": "mental_health_score",
            "test_size": 0.2,
            "random_state": 42,
        },
        "unsupervised": {
            "use_numeric_only": True,
            "random_state": 42,
            "default_k": 3,
        },
    }

    if yaml is None or not cfg_path.exists():
        return default_cfg

    try:
        with cfg_path.open("r", encoding="utf-8") as f:
            parsed = yaml.safe_load(f) or {}
        # Shallow merge: keep defaults when keys are missing
        cfg = default_cfg.copy()
        for section, values in (parsed or {}).items():
            if isinstance(values, dict) and section in cfg:
                merged = cfg[section].copy()
                merged.update(values)
                cfg[section] = merged
            else:
                cfg[section] = values
        return cfg
    except Exception as e:
        raise RuntimeError(f"Failed to parse config at {cfg_path}: {e}")


def _resolve_path_from_root(path_str: str) -> Path:
    p = Path(path_str)
    return p if p.is_absolute() else (ROOT / p)


# ---------------------------------------------------
# Supervised dataset loaders
# ---------------------------------------------------
def load_supervised():
    """
    Load the full supervised dataset from data/raw/.
    Returns:
        DataFrame with all columns including the target.
    """
    cfg = get_config()
    path = _resolve_path_from_root(cfg["paths"]["supervised"]) if "paths" in cfg and "supervised" in cfg["paths"] else (DATA_RAW / "clean_supervised.csv")
    if not path.exists():
        raise FileNotFoundError(f"Supervised dataset not found: {path}")
    return pd.read_csv(path)


def load_supervised_xy(target_col=None):
    """
    Load supervised dataset and split into (X, y).
    Args:
        target_col (str): name of target column.
                          If None, tries to auto-detect.
    Returns:
        X (DataFrame), y (Series)
    """
    df = load_supervised()

    # Default from config (falls back to 'mental_health_score')
    if target_col is None:
        cfg = get_config()
        target_col = (cfg.get("supervised", {}).get("target") or "mental_health_score")
        if target_col not in df.columns:
            # If configured target not present, try legacy default then error
            if "mental_health_score" in df.columns:
                target_col = "mental_health_score"
            else:
                raise ValueError(
                    "No target_col provided and neither the configured target nor 'mental_health_score' were found. "
                    "Pass target_col explicitly."
                )

    if target_col not in df.columns:
        raise ValueError(f"Target column '{target_col}' not found in dataset.")

    X = df.drop(columns=[target_col])
    y = df[target_col]
    return X, y


# ---------------------------------------------------
# Unsupervised dataset loaders
# ---------------------------------------------------
def load_unsupervised():
    """
    Load the full unsupervised dataset from data/raw/.
    Returns:
        DataFrame with all original columns.
    """
    cfg = get_config()
    path = _resolve_path_from_root(cfg["paths"]["unsupervised"]) if "paths" in cfg and "unsupervised" in cfg["paths"] else (DATA_RAW / "clean_unsupervised.csv")
    if not path.exists():
        raise FileNotFoundError(f"Unsupervised dataset not found: {path}")
    return pd.read_csv(path)


def load_unsupervised_features(drop_non_numeric=None, drop_columns=None):
    """
    Load the unsupervised dataset but return ONLY features suitable
    for clustering.

    Args:
        drop_non_numeric (bool): if True, keeps only numeric columns.

    Returns:
        DataFrame containing features for clustering.
    """
    df = load_unsupervised()

    cfg = get_config()
    cfg_target = cfg.get("supervised", {}).get("target", "mental_health_score")

    # Defaults from config: use_numeric_only controls drop_non_numeric
    if drop_non_numeric is None:
        drop_non_numeric = bool(cfg.get("unsupervised", {}).get("use_numeric_only", True))

    # Default drop_columns: drop the supervised target to avoid leakage
    if drop_columns is None:
        drop_columns = (cfg_target,)

    if drop_columns:
        df = df.drop(columns=list(drop_columns), errors="ignore")

    if drop_non_numeric:
        df = df.select_dtypes(include=[np.number])

    if df.shape[1] < 2:
        raise ValueError(
            f"Unsupervised features too few: {df.shape[1]} found. "
            f"Dataset must contain ≥2 numeric columns."
        )

    return df
