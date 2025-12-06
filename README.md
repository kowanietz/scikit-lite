# scikit-lite

⚠️ **PRE-ALPHA** - This package is in very early development. APIs will change.

A lightweight machine learning library built from scratch with NumPy, following scikit-learn's API conventions.

## Features

Currently implemented:
- **Linear Models**
  - `LinearRegression` - Ordinary Least Squares (closed-form solution)
  - `SGDRegressor` - Linear regression with Stochastic Gradient Descent
- **Metrics**
  - Mean Squared Error (MSE)
  - Root Mean Squared Error (RMSE)
  - Mean Absolute Error (MAE)
  - R² Score

## Installation

```bash
pip install scikit-lite
```

## Quick Start

```python
import numpy as np
from sklite.linear_model import LinearRegression

# Create sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Fit model
model = LinearRegression()
model.fit(X, y)

# Make predictions
predictions = model.predict([[6], [7]])
print(predictions)  # [12. 14.]
```

## Project Goals

This project aims to:
1. Provide educational implementations of ML algorithms
2. Maintain scikit-learn API compatibility
3. Use Rust for performance-critical components (planned)
4. Serve as a learning resource for understanding ML algorithms

## Development Status

**Current Version: 0.0.1 (Pre-Alpha)**

This is an early placeholder release to reserve the package name. Expect breaking changes.

### Roadmap

- [ ] More linear models (Ridge, Lasso, ElasticNet)
- [ ] Classification algorithms (Logistic Regression, SVM)
- [ ] Clustering (K-Means, DBSCAN)
- [ ] Tree-based models (Decision Trees, Random Forests)
- [ ] Preprocessing utilities (StandardScaler, MinMaxScaler)
- [ ] Rust optimization for performance-critical components

## Requirements

- Python >= 3.11
- NumPy >= 2.3.5

## Contributing

This project is in early development. Contributions are welcome but please note the API is unstable.

## License

MIT License - See LICENSE file for details.

## Acknowledgments

Inspired by scikit-learn's excellent API design and educational resources.
