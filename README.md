# Data-Science

A curated collection of notebooks, mini-projects, and example apps covering the end-to-end data science journey — from statistics and probability to data preprocessing, visualization, machine learning, and simple web deployment (Flask, Streamlit).

## Repository Structure

- `10_Data_preprocessing_for_ml/`: Data cleaning, transformation, and preparation notebooks for ML.
- `11_Machine_learning/`: Machine learning modules and projects.
  - `1_Introduction_ML/`: Introductory materials for ML (linear regression example and sample dataset).
  - `2_Linear_reg_model/`: Linear regression training notebook plus a minimal Flask app (`app.py`) and HTML template.
  - `3_Multiple_linear_regression_project/`: Algerian forest fires regression project with EDA/feature engineering, model training, scaler and ridge model artifacts.
- `4_Data-Visualization/`: Plotting fundamentals, practice exploration, and plot anatomy images.
- `5_Flask_web_Framework/Flask/`: Flask basics with example routes (`app.py`, `marks.py`, etc.) and Jinja templates.
- `6_streamlit_framework/`: Streamlit widgets and small demo apps.
- `7_Getting_started_with_statistics/`: Basics of statistics and probability for ML.
- `8_Probability_distribution_fuction/`: Probability distributions primer.
- `9_Inferential_statistics/`: Hypothesis testing notebook.
- `File-handling-&-Exception-handling/`: Python file I/O and exception handling exercises and assessment.
- `Logging in python/`: Logging patterns, multiple logger examples, and a simple logging package.
- `Sqlite/`: SQLite notebooks and toy databases for practice.

## Getting Started

### Prerequisites
- Python 3.9+ recommended
- pip

### Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate
```

### Install dependencies
This repository is organized by topic and many notebooks are self-contained. If a subproject includes an `app.py` (Flask/Streamlit) or specific requirements, install them locally in the active environment, for example:
```bash
pip install -r requirements.txt  # if present near an app/notebook
# or install commonly used packages as needed
pip install numpy pandas matplotlib seaborn scikit-learn jupyter flask streamlit
```

### Launch Jupyter
```bash
jupyter notebook
```
Open the notebook of interest (e.g., `11_Machine_learning/3_Multiple_linear_regression_project/EDA_Feature_engineering.ipynb`).

## Running the Example Apps

### Flask
Example locations:
- `11_Machine_learning/2_Linear_reg_model/app.py`
- `5_Flask_web_Framework/Flask/app.py`

Run from the respective folder:
```bash
python app.py
```
Then open the printed URL (typically `http://127.0.0.1:5000`).

### Streamlit
From `6_streamlit_framework/`:
```bash
streamlit run app.py
```

## Projects Highlight

- **Multiple Linear Regression – Algerian Forest Fires** (`11_Machine_learning/3_Multiple_linear_regression_project/`)
  - Notebooks for EDA and model training
  - Saved artifacts: `ridge_regressor_model.pkl`, `scaler.pkl`

- **Linear Regression Demo App** (`11_Machine_learning/2_Linear_reg_model/`)
  - Model training notebook and minimal Flask interface (`templates/index.html`)

## Datasets

Small sample datasets are included for practice (e.g., `Salary_Data.csv`, mobile price regression CSVs, Algerian forest fires CSVs). See corresponding notebooks for usage.

## Contributing

Pull requests and suggestions are welcome. For substantial changes, please open an issue first to discuss what you would like to change.

## License

MIT License © 2025 Mojahidul Islam. Permission to use, copy, modify, and distribute with attribution. See the `LICENSE` file for the full text.

## Author

Mojahidul Islam
