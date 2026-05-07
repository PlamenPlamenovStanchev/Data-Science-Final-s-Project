# Data Science Final Project: Sports Injury Analysis

## Overview

This project analyzes injury patterns across four major professional sports leagues in the United States: MLB, NBA, NFL, and NHL. It combines raw injury datasets from different league sources into a standardized analytical dataset, then uses exploratory data analysis, statistical hypothesis testing, effect size interpretation, and an exploratory machine learning extension to compare injury frequency, injury type, head injury risk, and injury severity.

Professional sports injuries are shaped by sport-specific movement demands, contact intensity, equipment, league reporting practices, and medical protocols. Because each league records injuries differently, a major part of the project is devoted to cleaning, standardizing, and validating the data before making comparisons.

## Project Goals

- Build a reproducible data cleaning pipeline for multi-league injury data.
- Standardize inconsistent injury descriptions into comparable injury categories.
- Compare injury distributions across MLB, NBA, NFL, and NHL.
- Evaluate whether contact-heavy leagues show higher head injury risk.
- Analyze whether lower-body injuries dominate across leagues.
- Compare severity across injury categories using games missed as a proxy.
- Explore variability in injury profiles across high-contact and lower-contact sports.
- Add an exploratory machine learning model for head injury risk prediction.

## Research Hypotheses

The analysis is organized around five main hypotheses:

- **H1: Injury distribution differences across leagues.** Injury category distributions differ significantly between sports leagues.
- **H2: Contact sports and head injury risk.** Contact-intensive sports, represented by NFL and NHL, have a higher proportion of head injuries than NBA and MLB.
- **H3: Dominance of lower-body injuries.** Lower-body injuries are the most common injury category across leagues.
- **H4: Injury severity differences.** Severity, measured by games missed, differs significantly across injury categories.
- **H5: Variability in injury patterns.** High-contact sports show greater variability in injury patterns than lower-contact sports.

## Data

The project uses historical injury data for:

- MLB injuries
- NBA injuries from 2010 to 2020
- NFL injuries from 2009 to 2021
- NHL injuries

Raw files are stored in `datasets/raw/`. The cleaned and integrated dataset is stored in `datasets/processed/cleaned_injuries.csv`.

## Injury Categories

Because the raw datasets use different schemas and reporting styles, injuries are mapped into broader categories:

- `Head`
- `Upper Body`
- `Lower Body`
- `Illness`
- `Rest/Non-injury`
- `Unknown`
- `Other`

The analysis focuses primarily on true injury records and separates non-injury statuses such as rest, illness, and unknown cases where appropriate.

## Methodology

The project follows a structured data science workflow:

1. **Data collection and inspection**
   - Load raw league datasets.
   - Compare columns, missing values, and reporting formats.

2. **Data cleaning**
   - Normalize text fields.
   - Handle missing and empty values.
   - Extract injury information from free-text fields, especially NBA notes.
   - Standardize date, league, player, team, and injury fields.

3. **Feature engineering**
   - Categorize injuries using rule-based keyword matching.
   - Create comparable league-level and injury-level variables.
   - Prepare severity fields where games missed is available.

4. **Data integration**
   - Align schemas across all leagues.
   - Merge cleaned league datasets into one processed dataset.
   - Validate category quality and final record counts.

5. **Exploratory data analysis**
   - Compare overall injury distributions.
   - Visualize injury patterns by league.
   - Analyze head injury distribution.
   - Examine games missed and severity patterns.
   - Compare frequency and severity using visual summaries.

6. **Statistical testing**
   - Chi-square tests for categorical association.
   - Cramer's V for effect size.
   - Risk ratios and odds ratios for head injury comparisons.
   - Binomial comparisons for lower-body dominance.
   - Kruskal-Wallis and Mann-Whitney tests for severity differences.
   - Holm correction for multiple pairwise tests.
   - Shannon entropy and permutation testing for injury profile variability.

7. **Machine learning extension**
   - Build an exploratory classification model for head injury risk.
   - Use preprocessing pipelines with categorical and numeric features.
   - Evaluate model performance using classification metrics and ROC-AUC.

## Key Findings

- Injury distributions differ meaningfully across leagues, supporting the idea that each sport has a distinct injury profile.
- NFL injuries are strongly concentrated in lower-body categories.
- NHL injuries show a substantial upper-body component alongside lower-body injuries.
- MLB injuries are heavily influenced by upper-body and throwing-related mechanics.
- NBA has a large `Other` category, likely reflecting broad movement demands and less standardized injury descriptions in the source data.
- Contact-intensive leagues, especially NFL and NHL, show substantially higher head injury rates than NBA and MLB.
- Lower-body injuries are the most common anatomical category overall, but MLB is an important exception because upper-body injuries are more frequent in the cleaned data.
- Severity differs across injury categories, but the most frequent injuries are not always the most severe.
- Head injuries are less frequent than lower-body injuries but remain especially important because of their medical complexity, return-to-play uncertainty, and long-term health implications.
- Injury variability is not explained by contact intensity alone; movement patterns, equipment, playing environment, and reporting structure also matter.

## Repository Structure

```text
.
|-- datasets/
|   |-- raw/
|   |   |-- ba_injuries_2010-2020.csv
|   |   |-- mlb_injury.csv
|   |   |-- nfl_injuries_2009_2021.csv
|   |   `-- nhl_injuries.csv
|   `-- processed/
|       `-- cleaned_injuries.csv
|-- images/
|   |-- ba hit.jpg
|   |-- concussion-vector-illustration-labeled-educational-post-head-trauma-scheme-concussion-vector-illustration-labeled-educational-post-156638716.webp
|   |-- mlb pitching motion.jpg
|   |-- nfl tackle.jpg
|   `-- nhl collision.jpg
|-- notebooks/
|   |-- 01_data_preparation.ipynb
|   |-- 02_analysis.ipynb
|   `-- 03_ml_extension.ipynb
|-- src/
|   |-- data_cleaning.py
|   |-- feature_engineering.py
|   `-- hypothesis_testing.py
|-- requirements.txt
`-- README.md
```

## Notebooks

- `notebooks/01_data_preparation.ipynb`
  - Cleans the raw league datasets.
  - Normalizes text fields and missing values.
  - Extracts NBA injury types from free-text notes.
  - Categorizes injuries into standardized groups.
  - Harmonizes schemas and creates the processed dataset.

- `notebooks/02_analysis.ipynb`
  - Defines the project assumptions and hypotheses.
  - Performs exploratory data analysis.
  - Visualizes injury distributions, head injuries, severity, trends, and league profiles.
  - Runs the main statistical tests.
  - Provides the discussion, limitations, and conclusion.

- `notebooks/03_ml_extension.ipynb`
  - Builds an exploratory model for head injury risk prediction.
  - Prepares features and target labels.
  - Trains a scikit-learn pipeline.
  - Evaluates model performance and discusses limitations.

## Source Modules

- `src/data_cleaning.py`
  - Provides helper functions for text cleaning, empty string normalization, and NBA injury keyword extraction.

- `src/feature_engineering.py`
  - Contains rule-based keyword patterns used to map injury descriptions into standardized injury categories.

- `src/hypothesis_testing.py`
  - Provides reusable statistical helpers such as p-value formatting, Cramer's V, Holm correction, and Shannon entropy.

## Setup

### 1. Clone or download the project

Open a terminal in the project root directory.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

```bash
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Jupyter

```bash
jupyter notebook
```

If Jupyter is not already installed in your environment, install it first:

```bash
pip install notebook
```

## How to Reproduce the Analysis

Run the notebooks in this order:

1. `notebooks/01_data_preparation.ipynb`
2. `notebooks/02_analysis.ipynb`
3. `notebooks/03_ml_extension.ipynb`

The first notebook creates or refreshes the processed dataset. The second notebook performs the main analysis. The third notebook is optional and should be interpreted as an exploratory extension, not as a clinical prediction system.

## Dependencies

The main Python libraries are listed in `requirements.txt`:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scipy`
- `scikit-learn`
- `ipython`

The notebooks also use Python standard library modules such as `re`, `sys`, `pathlib`, and `itertools`.

## Limitations

The results should be interpreted with caution because:

- The source datasets use different reporting standards.
- Injury definitions are not perfectly consistent across leagues.
- Some records rely on unstructured or vague text descriptions.
- The `Other` category may contain hidden patterns that could not be confidently assigned.
- Games missed is an imperfect proxy for medical severity.
- Exposure levels differ by league, season length, roster size, and playing time.
- Medical protocols, injury list rules, and return-to-play policies vary by league.
- The analysis is observational and should not be treated as causal evidence.

## Future Work

Future improvements could include:

- Exposure-adjusted injury rates using athlete-games, player-minutes, or player-seasons.
- Manual validation of injury category labels.
- More advanced natural language processing for injury description classification.
- Player-level context such as age, position, workload, and prior injury history.
- Season-level and longitudinal trend modeling.
- More detailed clinical outcome data beyond games missed.
- Stronger predictive modeling with richer features and external validation.

## Conclusion

This project shows that professional sports injury patterns are strongly league-specific. Contact intensity matters, especially for head injury risk, but it is not the only driver. Sport mechanics, repetitive movement, equipment, playing environment, and reporting practices all shape the observed injury profiles. The analysis supports league-specific prevention strategies and highlights the importance of more standardized injury data for future sports health research.
