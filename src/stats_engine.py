import numpy as np
from scipy import stats

import numpy as np
from scipy import stats


def calculate_ab_test_advanced(group_a, group_b):
    """
    Advanced test: first checks for normality,
    then selects a suitable algorithm.
    """
    # 1. Normality check (Shapiro-Wilk)
    # If p_norm > 0.05, the data is distributed normally
    _, p_norm_a = stats.shapiro(group_a)
    _, p_norm_b = stats.shapiro(group_b)

    # 2. Base metric calculation
    mean_a, mean_b = np.mean(group_a), np.mean(group_b)
    lift = ((mean_b - mean_a) / mean_a) * 100

    # 3. TEST SELECTION LOGIC
    if p_norm_a > 0.05 and p_norm_b > 0.05:
        # Normal data -> use T-test
        _, p_value = stats.ttest_ind(group_a, group_b)
        test_type = "T-Test (Parametric)"
    else:
        # Data "curves" -> use Mann-Whitney (more reliable for emissions)
        _, p_value = stats.mannwhitneyu(group_a, group_b)
        test_type = "Mann-Whitney (Non-parametric)"

    return p_value, lift, test_type

