# 🔬 StatGuard-Metric: Adaptive ML Experimentation Framework

![Python](https://img.shields.io)
![SciPy](https://img.shields.io)
![SQLite](https://img.shields.io)
![Streamlit](https://img.shields.io)


**StatGuard-Metric** is a professional engineering framework for A/B testing and scientific validation of ML models. It automatically selects the optimal statistical criteria based on data distribution, protecting businesses from false-positive conclusions and random noise.

## 🌟 Key Features
* **Scientific Rigor:** Automated normality check using the **Shapiro-Wilk test**.
* **Adaptive Testing:** Dynamic switching between **Student's T-Test** (parametric) and **Mann-Whitney U-test** (non-parametric).
* **Persistence Layer:** Full logging of every experiment into a persistent **SQLite** database.
* **Live Dashboard:** Interactive visualization of results and experiment history via **Streamlit & Plotly**.

## 🛠 Tech Stack
* **Stats Engine:** SciPy, NumPy, Statsmodels.
* **Data Management:** SQLite, Pandas.
* **Visualization:** Streamlit, Plotly.
* **Core:** Python 3.11+, OOP Architecture.

## 🧠 Decision Logic
The system selects the algorithm based on data properties:
1. **Normality Check (Shapiro-Wilk):**
   - If p > 0.05 (Normal) -> **Student's T-Test**.
   - If p < 0.05 (Skewed) -> **Mann-Whitney U-Test**.
2. **Lift Calculation:** Measuring the relative effect size between groups.
3. **Audit Trail:** Automated logging of p-values and results to the SQL database.

## 📈 Data Pipeline (Architecture)

1. **Ingestion:** Loading metrics from Group A and Group B (SQLite/CSV).
2. **Profiling:** Assessing distribution normality (Shapiro-Wilk).
3. **Inference:** Executing adaptive tests, calculating P-Value and Lift.
4. **Logging:** Committing test metadata and verdicts to SQL storage.
5. **Visualization:** Rendering the analytical dashboard in Streamlit.

## 🛡️ Robustness Features
* **Outlier Resistance:** Automatic fallback to non-parametric tests for "noisy" data.
* **Safe Path Resolution:** Cross-platform path handling via **Pathlib**.
* **Data Validation:** Integrated cleaning pipeline to handle missing values (NaN).

## 🛠 Installation & Usage
1. **Clone repo:** `git clone https://github.com`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Run Pipeline:** `python main.py`
4. **View Dashboard:** `streamlit run app.py`

## 🗺 Future Roadmap
- [ ] **Bayesian Methods:** Implementing Bayesian A/B testing.
- [ ] **A/B/C Support:** Testing multiple variants simultaneously.
- [ ] **Alerting:** Integration with Telegram for instant experiment notifications.

## 🤝 Contributing
Feel free to fork this project, report issues, or suggest new statistical methods (e.g., Bootstrap or Bayesian priors). Your feedback helps make StatGuard more robust!
