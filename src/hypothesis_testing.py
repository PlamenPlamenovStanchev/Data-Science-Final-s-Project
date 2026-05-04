"""Reusable statistical helpers for the injury hypothesis tests.

The notebook uses these helpers to keep hypothesis-testing cells focused on
analysis instead of repeating small formatting and effect-size utilities.
"""

import numpy as np


def format_p(p_value):
    """Format a p-value for readable notebook output.

    Very small p-values are displayed as ``< 0.001`` because printing long
    scientific-notation values can distract from interpretation. Other values
    are rounded to four decimals, which is enough precision for the EDA and
    hypothesis-testing narrative in the notebook.
    """
    if p_value < 0.001:
        return "< 0.001"
    return f"{p_value:.4f}"


def cramers_v_from_table(contingency_table, chi2_stat):
    """Calculate Cramer's V effect size for a chi-square test.

    Parameters
    ----------
    contingency_table:
        A pandas contingency table, usually created with ``pd.crosstab``.
        Rows and columns represent two categorical variables.
    chi2_stat:
        The chi-square statistic returned by ``scipy.stats.chi2_contingency``.

    Returns
    -------
    float
        Cramer's V, a normalized association measure between 0 and 1. This is
        useful because large datasets can produce tiny p-values even when the
        practical association is weak.
    """
    n = contingency_table.to_numpy().sum()
    rows, columns = contingency_table.shape
    return np.sqrt(chi2_stat / (n * min(rows - 1, columns - 1)))


def holm_adjust(p_values):
    """Apply Holm's step-down correction to multiple p-values.

    The H4 severity analysis performs several pairwise Mann-Whitney tests.
    Testing many pairs increases the chance of false positives, so this helper
    controls the family-wise error rate while remaining less conservative than
    a simple Bonferroni correction.

    Parameters
    ----------
    p_values:
        Sequence or array of raw p-values from multiple statistical tests.

    Returns
    -------
    numpy.ndarray
        Adjusted p-values in the same order as the input values.
    """
    order = np.argsort(p_values)
    adjusted = np.empty(len(p_values), dtype=float)
    running_max = 0
    m = len(p_values)

    for rank, idx in enumerate(order):
        value = min(1, p_values[idx] * (m - rank))
        running_max = max(running_max, value)
        adjusted[idx] = running_max

    return adjusted


def shannon_entropy_from_counts(counts):
    """Calculate Shannon entropy from category counts.

    Shannon entropy summarizes how evenly records are distributed across
    categories. In H5, a higher entropy means a league has a more diverse injury
    category mix, while a lower entropy means one injury category dominates.

    Zero-count categories are ignored in the logarithm step because
    ``log2(0)`` is undefined and those categories contribute no uncertainty.
    """
    counts = np.asarray(counts, dtype=float)
    probabilities = counts[counts > 0] / counts.sum()
    return -(probabilities * np.log2(probabilities)).sum()
