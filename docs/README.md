# Machine Learning Group Assignment – Overview

# TL;DR
> This repo is for our W11/12 Machine Learning group assignment.
> We selected one problem and dataset (≥100 rows) and implemented both supervised and unsupervised pipelines with evaluation.
> Notebooks and exports live under `docs/presentation_next_week/`.


## 1. Problem Statement

We will study a problem from our daily environment that can be analysed using both supervised and unsupervised machine learning methods.

**Working title (to be finalised):**  
> [Example: “Student Screen Time, Study Habits, and Productivity”]  
> [Alternative: “Customer Income and Spending Behaviour”]

**Motivation (why this matters):**

- The problem is close to our surroundings and daily life.
- The data can be represented numerically and used for machine learning.
- The same dataset can support both supervised and unsupervised analysis.

We will finalise the problem in our first group discussion.

---

## 2. Assignment Scope (What We Must Deliver)

According to the assignment:

> “Identify one problem in your surroundings that is suitable to be solved using machine learning. Collect data that can be processed for both supervised learning and unsupervised learning, with a minimum of 100 data points for each case.”

From this, our **minimum scope** is:

1. Choose **one real-world problem** related to our surroundings.
2. Obtain or prepare **one dataset** with at least **100 data points** (rows).
3. Ensure the dataset is structured so that:
   - It can be used for **supervised learning** (has a clear target/label column).
   - It can be used for **unsupervised learning** (has numeric features for clustering).
4. Document:
   - The problem.
   - The dataset.
   - How the dataset could be used for supervised and unsupervised learning.

Status: Implemented end-to-end. Both supervised and unsupervised notebooks run and save results.

Where to see results:
- `docs/presentation_next_week/implementation_supervised.ipynb`
- `docs/presentation_next_week/implementation_unsupervised.ipynb`
- Exports: `docs/presentation_next_week/exports/`

---

## 3. Planned Dataset

We will use a dataset that:

- Has at least **100 rows**.
- Contains **multiple numeric features**.
- Contains at least one **categorical or numeric label** suitable as a supervised target.
- Is meaningful for our chosen problem.

### 3.1. Candidate Themes

We will choose one of these themes (to be decided as a group):

1. **Student lifestyle and productivity**  
   Features could include:
   - Screen time, social media time, study hours, sleep, stress level, GPA, self-rated productivity.

2. **Customer income and spending behaviour** (similar to the example data)  
   Features could include:
   - Age, gender, income, spending score, category/segment.

3. **Other theme (to be proposed by group members)**  
   - [Write idea here]

### 3.2. Data Source

We will decide between:

- **Public dataset** (e.g. from Kaggle / open data portals), or  
- A **simple survey** (Google Form) if we prefer to collect our own data.

Minimum requirement: at least **100 valid rows** after cleaning.

---

## 4. How the Dataset Will Be Used

We will design the dataset so that the **same data** supports:

### 4.1. Supervised Learning (Implemented)

- We will define one column as a **label/target**.
- Examples:
  - For student data: “Productivity level” (High / Medium / Low) or GPA.
  - For customer data: “Customer segment” or “High/Low spender”.
- This column could be predicted using features such as:
  - Screen time, study hours, sleep, income, age, etc.
- Implementation details:
   - Deterministic 3-class target binning (Low/Medium/High)
   - Train/test split with stratification
   - Baselines: Logistic Regression, Random Forest
   - Metrics and confusion matrix saved to `data/processed/`

### 4.2. Unsupervised Learning (Implemented)

- We will use the **feature columns** (numeric) without the label.
- Examples of features:
  - Screen time, study hours, sleep, stress, income, spending score, etc.
- These features can be used for clustering (e.g. K-Means) to find:
  - Student/lifestyle behaviour groups, or
  - Customer segments based on income and spending.
- Implementation details:
   - K-Means with scaling; PCA 2D scatter
   - Silhouette score and K sweep (k=2..6)
   - Cluster interpretation summary
   - Artifacts saved to `data/processed/`

---

## 5. Work Breakdown (6 Group Members)

We will split tasks so everyone has a clear role. One person can take more than one small role if needed, but each area should have an owner.

1. **Problem & Documentation Lead**
   - Finalise the problem statement and motivation.
   - Write the introduction and problem description for the README/report.

2. **Data Source & Acquisition**
   - Search for or propose candidate datasets.
   - If using a public dataset: download and document source.
   - If using a survey: design the questions (Google Form) and manage responses.

3. **Data Cleaning & Formatting**
   - Clean missing values and inconsistent entries.
   - Ensure data types are correct (numeric vs categorical).
   - Prepare final CSV or table used in the project.

4. **Supervised Learning Design (Conceptual)**
   - Decide which column is the label.
   - Decide which features would be used to predict it.
   - Write a clear explanation of how a supervised method (e.g. K-NN, Decision Tree) could be applied to this dataset.

5. **Unsupervised Learning Design (Conceptual)**
   - Decide which features will be used for clustering.
   - Explain how clustering could group the data.
   - Propose possible interpretations of clusters.

6. **Editor & README/Report Integration**
   - Combine all sections into a single, coherent README/report.
   - Make sure the structure is clear and consistent.
   - Check that the description satisfies the assignment requirements.

Current additional roles (implemented):

- “Supervised modelling & evaluation” owner.
- “Unsupervised modelling & visualisation” owner.

---

## 6. Timeline (Draft)

We can adjust this based on the actual deadline.

- **Problem & Dataset**
  - Finalise problem statement.
  - Decide on data source (public dataset vs survey).
  - Assign roles.

- ** Data Preparation**
  - Collect/download data.
  - Clean and format dataset.
  - Confirm we have ≥ 100 valid rows.

- **Conceptual ML Design**
  - Define supervised target and features.
  - Define unsupervised feature set.
  - Write explanations of how ML would be used.

- **Documentation**
  - Finalise README/report.
  - If needed, plan extension to actual modelling (Option B).

---

## 7. Repository / Folder Structure (Suggestion)

We will keep the project organised with a simple structure:

```text
./
├─ data/
│  ├─ raw/           # Original dataset(s)
│  └─ processed/     # Cleaned dataset ready for ML
├─ docs/
│  └─ references/    # Any related reading or links
├─ src/              # (Optional) Code for future modelling (Option B)
├─ README.md         # Main project description and plan
└─ ASSIGNMENT.md     # (Optional) Detailed assignment-specific writeup
```

Key files now:

- `docs/presentation_next_week/implementation_supervised.ipynb`
- `docs/presentation_next_week/implementation_unsupervised.ipynb`
- `docs/presentation_next_week/exports/` (HTML/PDF)
- `data/processed/` (saved metrics and labels)

---

## 8. To-Do List (Immediate Actions)

1. Each member reads this README and adds comments.

2. In our next meeting, we decide:

   - Final problem theme.

   - Whether we use a public dataset or a self-collected survey.

3. Assign the six roles formally and write the names next to each role in Section 5.

4. Create data/ folder and start putting candidate datasets or survey exports there.
