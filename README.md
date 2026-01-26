# 📈 StatGuard-Metric: Adaptive ML Experimentation Framework

![Python 3.11](https://img.shields.io)
![SciPy](https://img.shields.io)
![SQLite](https://img.shields.io)
![Streamlit](https://img.shields.io)

**StatGuard-Metric** is a professional engineering framework for A/B testing and scientific validation of ML models. It automatically selects the optimal statistical criteria based on data distribution, protecting businesses from false-positive conclusions and random noise.

## 🌟 Key Features
*   **Scientific Rigor:** Automated normality check using the **Shapiro-Wilk test**.
*   **Adaptive Testing:** Dynamic switching between **Student's T-Test** (parametric) and **Mann-Whitney U-test** (non-parametric).
*   **Persistence Layer:** Full logging of every experiment into a persistent **SQLite** database.
*   **Live Dashboard:** Interactive visualization of results and experiment history via **Streamlit & Plotly**.

## 🛠 Tech Stack
*   **Stats Engine:** SciPy, NumPy, Statsmodels.
*   **Data Management:** SQLite, Pandas.
*   **Visualization:** Streamlit, Plotly.
*   **Core:** Python 3.11+, OOP Architecture.

## 📈 Data Pipeline (Architecture)
1.  **Ingestion:** Simulating or loading metrics from Group A and Group B.
2.  **Profiling:** Assessing distribution shape and statistical assumptions.
3.  **Inference:** Executing tests, calculating **P-Value** and **Lift**.
4.  **Logging:** Committing test metadata to the SQL storage.
5.  **Visualization:** Rendering the analytical dashboard for business decision-making.

```mermaid
graph LR
    classDef storage fill:#e1f5fe,stroke:#01579b,color:#01579b;
    classDef engine fill:#fff3e0,stroke:#e65100,color:#e65100;
    classDef ui fill:#f3e5f5,stroke:#4a148c,color:#4a148c;

    A([<b>Start:</b> A/B Metrics]) --> B{Stats Engine}
    B -->|Normality Check| C[[T-Test or Mann-Whitney]]
    C -->|Calculates| D(P-Value & Lift)
    D -->|Commit| E[(SQLite Database)]
    E -->|Fetch| F[/Streamlit Dashboard/]

    class E storage;
    class B,C,D engine;
    class F ui;
```

## 🧠 Decision Logic
The system selects the algorithm based on data properties:
1. **Normality Check (Shapiro-Wilk):**
   - If $p > 0.05$ (Normal) $\rightarrow$ **Student's T-Test**.
   - If $p < 0.05$ (Skewed) $\rightarrow$ **Mann-Whitney U-Test**.
2. **Lift Calculation:** Measuring the relative effect size.
3. **Audit Trail:** Automated logging of results to the SQL database.

## 🛡️ Robustness Features
*   **Outlier Resistance:** Automatic fallback to non-parametric tests for "noisy" infrastructure data.
*   **Data Validation:** Integrated cleaning pipeline to handle missing values (NaN) before processing.
*   **Safe Path Resolution:** Cross-platform path handling (`os.path.abspath`) for reliable deployment on Mac/Linux/Win.

## 📸 Real Case: From Metrics to Verdict

| **Distribution View** | **Stats Analysis** | **Business Verdict** |
| :--- | :--- | :--- |
| <img src="reports/dist_plot.png" width="250"> | `P-Value: 0.0004`, `Lift: +5.65%` | **✅ Approved.** Difference is statistically significant. Deploying new model. |

## 💰 Business Impact
*   **Evidence-Based Decisions:** Eliminates human bias in model evaluation.
*   **Risk Mitigation:** Prevents deployment of models showing "random" growth.
*   **Historical Audit:** A complete trail of all experiments for retrospective analysis.

## 🛠 Installation & Usage
1. **Clone repo:** `git clone https://github.com`
2. **Setup env:** `python -m venv .venv && source .venv/bin/activate`
3. **Install:** `pip install -r requirements.txt`
4. **Run Pipeline:** `python main.py`
5. **View Dashboard:** `streamlit run app.py`

## 🗺 Future Roadmap
- [ ] **Bayesian Methods:** Implementing Bayesian A/B testing for smaller sample sizes.
- [ ] **A/B/C Support:** Testing multiple variants simultaneously.
- [ ] **Alerting:** Integration with Slack/Telegram for instant experiment notifications.

## 🤝 Contributing
