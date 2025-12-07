import numpy as np


def accuracy_score(y_true, y_pred):
    """Accuracy sore classification metric.

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        Ground truth target values.
    y_pred : array-like of shape (n_samples,)
        Predicted values.

    Returns
    -------
    accuracy : float
        Accuracy score.
    """
    return np.mean(y_true == y_pred)
