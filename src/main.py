import numpy as np
from src.database import StatMetricDB
from src.stats_engine import calculate_ab_test


def run_pipeline():
    # 1. Initialize database
    db = StatMetricDB()

    print("🚀 Запуск эксперимента в StatGuard-Metric...")

    # 2. Data Simulation
    # А: The Old model (mean 50, spread 5)
    # Б: The new model (mean 53, spread 5)
    group_a = np.random.normal(loc=50, scale=5, size=100)
    group_b = np.random.normal(loc=53, scale=5, size=100)

    # 3. Perform calculations
    p_val, lift = calculate_ab_test(group_a, group_b)

    # 4. Add the result to the database
    test_name = "DeepWatch_V1_vs_V2_Comparison"
    db.log_experiment(test_name, p_val, lift)

    # 5. Put the summary in the console
    print(f"📊 Тест: {test_name}")
    print(f"📈 Прирост (Lift): {lift:.2f}%")
    print(f"🧬 P-Value: {p_val:.4f}")

    if p_val < 0.05:
        print("✅ Вердикт: Разница значима. Деплоим!")
    else:
        print("❌ Вердикт: Разница случайна. Дорабатываем.")


if __name__ == "__main__":
    run_pipeline()
