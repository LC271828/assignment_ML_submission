# Week 13 – Presentation: Implementation + Evaluation

This folder contains all work for next week's presentation.

The presentation must include:

---

## 1. Implementation Result

### A. Unsupervised Learning (required)
K-Means clustering is implemented in `implementation_unsupervised.ipynb`.

Deliverables:
- Cluster count selected (k from `config.yaml` or default 3)
- 2D PCA scatter plot
- Cluster labels assigned to all rows
- Silhouette score and a short interpretation of clusters

Stored in:
- `implementation_unsupervised.ipynb`
- Optional: export figures to `figures/`

---

### B. Supervised Learning (implementation)
`implementation_supervised.ipynb` implements a supervised pipeline with preprocessing and two baseline models (Logistic Regression and Random Forest).

Deliverables:
- Target variable binned into three classes (Low/Medium/High) for clarity
- Train/test split with stratification
- Metrics (accuracy and classification report)
- Confusion matrix plot

Stored in:
- `implementation_supervised.ipynb`

---

## 2. Evaluation Model Result

### A. Unsupervised Evaluation
- Silhouette score and cluster-meaning interpretation
- Strengths/weaknesses

Add notes to:
- `evaluation_notes.md`

### B. Supervised Evaluation
- Accuracy and classification report
- Conceptual evaluation:
  - Does it separate students well?
  - Which features influence predictions?

Add notes to:
- `evaluation_notes.md`

---

## 3. Final Presentation Slides

Add slides in:
- `final_slides.pptx` or `final_slides.pdf`

Slides should include:
- Problem summary
- Dataset description
- Methods chosen
- Results (implementation)
- Evaluation
- Conclusion

---

## Where to Work

| Task | File / Folder |
|------|----------------|
| Unsupervised K-Means | `implementation_unsupervised.ipynb` |
| Supervised model | `implementation_supervised.ipynb` |
| Evaluation text | `evaluation_notes.md` |
| Figures | `figures/` |
| Slides | `final_slides.pptx` |

---

## How to Run

1. Ensure dependencies are installed:
  ```powershell
  & ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt
  ```
2. Open each notebook and run cells in order.

## Export Notebooks
Export the notebooks to HTML for sharing:
```powershell
& ".\.venv\Scripts\python.exe" -m nbconvert "docs/presentation_next_week/implementation_supervised.ipynb" --to html --output-dir "docs/presentation_next_week/exports"
& ".\.venv\Scripts\python.exe" -m nbconvert "docs/presentation_next_week/implementation_unsupervised.ipynb" --to html --output-dir "docs/presentation_next_week/exports"
```
This writes `.html` files under `docs/presentation_next_week/exports`.

Notes:
- Notebooks respect optional `config.yaml` keys under `paths`, `supervised`, and `unsupervised`.
- Artifacts are saved to `data/processed/`.

For PDF export on Windows, close any open PDF viewer or export with a unique filename to avoid file-lock issues (e.g., `--output implementation_supervised_run2`).

---
