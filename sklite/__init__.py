"""scikit-lite: Lightweight ML library with scikit-learn compatible API."""

__version__ = "0.0.1a0"

import warnings

from sklite.cluster import KMeans
from sklite.linear_model import LinearRegression, LogisticRegression, SGDRegressor
from sklite.metrics import (
    accuracy_score,
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    root_mean_squared_error,
)

__all__ = [
    "LinearRegression",
    "LogisticRegression",
    "KMeans",
    "SGDRegressor",
    "accuracy_score",
    "mean_absolute_error",
    "mean_squared_error",
    "r2_score",
    "root_mean_squared_error",
]

warnings.warn(
    "This library is in pre-alpha stage. APIs may change without notice.",
    category=UserWarning,
    stacklevel=2,
)
