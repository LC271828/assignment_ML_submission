# Machine Learning Group Assignment – Repository Overview

This repository contains all work for the Machine Learning 2 group assignment.

The assignment has three components:
1. **Pre-class work** (problem selection and dataset preparation)
2. **In-class work (24 Nov 2025)** – background, feature description, algorithm choices, and manual K-Means
3. **Next-week presentation** – implementation result + evaluation

See `docs/assignment_context.md` for the official task instructions.

---

## Repository Structure
```bash
assignment_ML/
├── data/
│ ├── raw/ # Full supervised & unsupervised datasets (100+ rows)
│ ├── processed/ # Cleaned datasets (if needed)
│ └── in_class/ # Small in-class samples used in the notebook
│     ├── sample_supervised.csv
│     └── sample_unsupervised.csv
│
├── docs/
│ ├── assignment_context.md # Official instructions (minimal, lecturer-provided)
│ ├── pre_class/ # Optional notes/materials from pre-class work
│ ├── in_class/ # Work done during class on 24 Nov
│ └── presentation_next_week/ # Slides + evaluation for next week
│
├── scripts/ # Tools: zip, environment checks, project overview
├── src/ # (Optional) Code for implementation phase
└── README.md #
```


---

## Where to Work

- **Teammates editing pre-class materials:**  
  → `docs/pre_class/`

- **Teammates working on the 24 Nov in-class notebook:**  
  → `docs/in_class/`

- **Teammates preparing next week's slide deck + results:**  
  → `docs/presentation_next_week/`

---

## Important Files

- `docs/assignment_context.md`  
  Exact assignment instructions (no interpretation).

- `docs/in_class/class_task.ipynb`  
  Notebook for the 24 Nov in-class work.

- `data/raw/clean_supervised.csv`  
- `data/raw/clean_unsupervised.csv`

- `data/in_class/sample_supervised.csv`  
  5-sample supervised subset for quick demos.

- `data/in_class/sample_unsupervised.csv`  
  5-sample unsupervised subset used in the manual K-Means.


## Next Week Contribution Guide
Teammates working on Week 13 tasks should go to:

`docs/presentation_next_week/`

and follow the instructions in `README.md`.

## Optional: Code Style

If you want to format/lint before committing:

- Format with Black:
  ```bash
  black src/ scripts/
