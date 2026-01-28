import numpy as np
from scipy import stats
from typing import Tuple


class StatAuditor:
    """
    Automated statistical engine for adaptive hypothesis testing.
    """

    @staticmethod
    def run_analysis(group_a: np.ndarray, group_b: np.ndarray) -> Tuple[float, float, str]:
        """
        Runs advanced A/B test analysis with automated test selection.

        Returns:
            p_value: Probability of null hypothesis
            lift: Percentage difference between means
            test_type: Name of the test performed
        """
        # 1. Check for Normality (Shapiro-Wilk)
        # If p_norm > 0.05, data is likely normally distributed
        _, p_norm_a = stats.shapiro(group_a)
        _, p_norm_b = stats.shapiro(group_b)

        # 2. Metric calculation
        mean_a, mean_b = np.mean(group_a), np.mean(group_b)
        lift = ((mean_b - mean_a) / mean_a) * 100

        # 3. Adaptive Test Selection Logic
        if p_norm_a > 0.05 and p_norm_b > 0.05:
            # Normal distribution -> Student's T-test
            _, p_value = stats.ttest_ind(group_a, group_b)
            test_type = "T-Test (Parametric)"
        else:
            # Non-normal distribution -> Mann-Whitney U Test
            # More robust against outliers and non-Gaussian data
            _, p_value = stats.mannwhitneyu(group_a, group_b, alternative='two-sided')
            test_type = "Mann-Whitney (Non-parametric)"

        return float(p_value), float(lift), test_type
