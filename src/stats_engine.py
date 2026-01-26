import numpy as np
from scipy import stats


def calculate_ab_test(group_a, group_b):
    """
    Performs the T-test of Studen for two independent samples.
    Returns p-value and lift (the difference of averages in %).
    """
    # 1. Average
    mean_a = np.mean(group_a)
    mean_b = np.mean(group_b)

    # 2. Lift (relative increase B to A)
    # Это то, что бизнес понимает лучше всего: "Мы стали лучше на 5%"
    lift = ((mean_b - mean_a) / mean_a) * 100

    # 3. Perform statistical test
    t_stat, p_value = stats.ttest_ind(group_a, group_b)

    return p_value, lift
