import sys
import numpy as np
from pathlib import Path

# Добавляем src в пути
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

from src.database import StatMetricDB
from src.stats_engine import StatAuditor


def run_pipeline():
    db = StatMetricDB()
    auditor = StatAuditor()

    print("🚀 [StatGuard] Starting adaptive A/B analysis...")

    # Data Simulation (Baseline vs Challenger)
    group_a = np.random.normal(loc=50, scale=5, size=100)
    group_b = np.random.normal(loc=53, scale=5, size=100)

    # Adaptive Testing
    p_val, lift, t_type = auditor.run_analysis(group_a, group_b)

    # Logging to SQLite
    test_name = "DeepWatch_V1_vs_V2_Comparison"
    db.log_experiment(test_name, p_val, lift, t_type)

    print(f"\n" + "=" * 40)
    print(f"📊 TEST: {test_name}")
    print(f"📈 LIFT: {lift:.2f}%")
    print(f"🧬 P-VALUE: {p_val:.4f} ({t_type})")

    if p_val < 0.05:
        print("✅ VERDICT: STATISTICALLY SIGNIFICANT. DEPLOY!")
    else:
        print("❌ VERDICT: INSIGNIFICANT. KEEP REFINING.")
    print("=" * 40)


if __name__ == "__main__":
    run_pipeline()
