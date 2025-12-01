This folder contains shared helper code used by the notebooks.

- `data_io.py`: centralised dataset loaders and config handling.
	- Used by notebooks via `from src.data_io import load_supervised_xy, load_unsupervised_features`.

You can add small, reusable utilities here to keep notebooks clean.
