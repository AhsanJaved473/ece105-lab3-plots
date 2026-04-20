import numpy as np


def generate_data(seed):
    """
    Generate simulated temperature readings for two sensors and timestamps.

    Parameters
    ----------
    seed : int
        Seed used to initialize ``np.random.default_rng`` for reproducible
        random data generation.

    Returns
    -------
    sensor_a : numpy.ndarray
        One-dimensional ``float64`` array of shape ``(200,)`` containing
        simulated temperature readings in degrees Celsius for Sensor A. The
        samples are drawn from a normal distribution with mean 25.0 and
        standard deviation 3.0.
    sensor_b : numpy.ndarray
        One-dimensional ``float64`` array of shape ``(200,)`` containing
        simulated temperature readings in degrees Celsius for Sensor B. The
        samples are drawn from a normal distribution with mean 27.0 and
        standard deviation 4.5.
    timestamps : numpy.ndarray
        One-dimensional ``float64`` array of shape ``(200,)`` containing
        timestamps from 0.0 to 10.0 seconds, inclusive.
    """
    rng = np.random.default_rng(seed)
    n = 200

    sensor_a = rng.normal(loc=25.0, scale=3.0, size=n).astype(np.float64)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=n).astype(np.float64)
    timestamps = np.linspace(0.0, 10.0, n, dtype=np.float64)

    return sensor_a, sensor_b, timestamps
