"""Unit test suite for wiener_process.py"""

import pytest
import numpy as np
from pypricer.simulations import wiener_process
import pandas as pd

def test_wiener_process_shape():
    """Test if output shape is as requested"""
    n_paths, n_steps = 5, 100
    dt, sigma, mu = 0.01, 0.1, 0.05

    paths = wiener_process.generate_wiener_process(n_paths, n_steps, dt, sigma, mu)

    assert paths.shape == (n_steps + 1, n_paths)


@pytest.mark.parametrize(
    "mu", [0.05, 0, -0.03], ids=["Positive drift", "No drift", "Negative drift"]
)
def test_wiener_process_deterministic_drift(mu):
    """Test if deterministic paths are generated correctly"""
    n_paths, n_steps = 1, 10
    dt = 0.01
    sigma = 0.0

    paths = wiener_process.generate_wiener_process(n_paths, n_steps, dt, sigma, mu)

    expected_paths = mu * dt * np.arange(0.0, n_steps + 1)

    np.testing.assert_allclose(paths.values.ravel(), expected_paths, atol=1e-6)


if __name__ == "__main__":
    pass
