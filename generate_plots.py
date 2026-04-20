import matplotlib.pyplot as plt
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


def plot_scatter(ax, timestamps, sensor_a, sensor_b):
    """
    Plot sensor readings versus time on an existing Matplotlib Axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Existing Axes object to modify in place.
    timestamps : numpy.ndarray
        One-dimensional ``float64`` array of shape ``(200,)`` containing
        timestamps in seconds for the sensor readings.
    sensor_a : numpy.ndarray
        One-dimensional ``float64`` array of shape ``(200,)`` containing
        Sensor A temperature readings in degrees Celsius.
    sensor_b : numpy.ndarray
        One-dimensional ``float64`` array of shape ``(200,)`` containing
        Sensor B temperature readings in degrees Celsius.

    Returns
    -------
    None
        This function modifies ``ax`` in place and does not return a value.
    """
    ax.scatter(timestamps, sensor_a, color="blue", alpha=0.7, s=30, label="Sensor A")
    ax.scatter(
        timestamps,
        sensor_b,
        color="orange",
        alpha=0.7,
        s=30,
        label="Sensor B",
    )
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Sensor Readings vs Time")
    ax.legend()
    ax.grid(True, alpha=0.3)

    return None


def plot_histogram(ax, sensor_a, sensor_b):
    """
    Plot overlaid histograms of the two sensor reading distributions.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Existing Axes object to modify in place.
    sensor_a : numpy.ndarray
        One-dimensional ``float64`` array of shape ``(200,)`` containing
        Sensor A temperature readings in degrees Celsius.
    sensor_b : numpy.ndarray
        One-dimensional ``float64`` array of shape ``(200,)`` containing
        Sensor B temperature readings in degrees Celsius.

    Returns
    -------
    None
        This function modifies ``ax`` in place and does not return a value.
    """
    ax.hist(sensor_a, bins=20, color="blue", alpha=0.6, label="Sensor A")
    ax.hist(sensor_b, bins=20, color="orange", alpha=0.6, label="Sensor B")
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of Sensor Temperature Readings")
    ax.legend()
    ax.grid(True, alpha=0.3)

    return None


def plot_boxplot(ax, sensor_a, sensor_b):
    """
    Plot a box plot comparing the two sensor reading distributions.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Existing Axes object to modify in place.
    sensor_a : numpy.ndarray
        One-dimensional ``float64`` array of shape ``(200,)`` containing
        Sensor A temperature readings in degrees Celsius.
    sensor_b : numpy.ndarray
        One-dimensional ``float64`` array of shape ``(200,)`` containing
        Sensor B temperature readings in degrees Celsius.

    Returns
    -------
    None
        This function modifies ``ax`` in place and does not return a value.
    """
    ax.boxplot([sensor_a, sensor_b], labels=["Sensor A", "Sensor B"])
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Box Plot of Sensor Temperature Readings")
    ax.grid(True, alpha=0.3)

    return None


def main():
    """
    Generate sensor data, create all plots, and display the figure.

    Parameters
    ----------
    None

    Returns
    -------
    None
        This function builds the figure, draws the plots, and displays it.
    """
    seed = 3297
    sensor_a, sensor_b, timestamps = generate_data(seed)

    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    plot_scatter(axes[0], timestamps, sensor_a, sensor_b)
    plot_histogram(axes[1], sensor_a, sensor_b)
    plot_boxplot(axes[2], sensor_a, sensor_b)
    fig.tight_layout()
    plt.show()

    return None


if __name__ == "__main__":
    main()
