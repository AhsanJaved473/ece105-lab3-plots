"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np
import matplotlib.pyplot as plt

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

def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """
    Draw a scatter plot of sensor data over time onto a given Axes object.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Temperature readings for Sensor A.
    sensor_b : numpy.ndarray
        Temperature readings for Sensor B.
    timestamps : numpy.ndarray
        Time values for the readings.
    ax : matplotlib.axes.Axes
        The axes object to modify in place.

    Returns
    -------
    None
    """
    ax.scatter(timestamps, sensor_a, label='Sensor A', alpha=0.7, s=10)
    ax.scatter(timestamps, sensor_b, label='Sensor B', alpha=0.7, s=10)
    ax.set_title('Sensor Readings vs. Time')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Temperature (°C)')
    ax.legend()

def plot_histogram(sensor_a, sensor_b, ax):
    """
    Draw a histogram of sensor temperature distributions onto a given Axes object.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Temperature readings for Sensor A.
    sensor_b : numpy.ndarray
        Temperature readings for Sensor B.
    ax : matplotlib.axes.Axes
        The axes object to modify in place.

    Returns
    -------
    None
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, label='Sensor A')
    ax.hist(sensor_b, bins=30, alpha=0.5, label='Sensor B')
    ax.set_title('Temperature Distribution')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Frequency')
    ax.legend()

def plot_boxplot(sensor_a, sensor_b, ax):
    """
    Draw a box plot of sensor data and a combined mean line onto an Axes object.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Temperature readings for Sensor A.
    sensor_b : numpy.ndarray
        Temperature readings for Sensor B.
    ax : matplotlib.axes.Axes
        The axes object to modify in place.

    Returns
    -------
    None
    """
    data = [sensor_a, sensor_b]
    # Uses 'tick_labels' to stay compatible with Matplotlib 3.9+
    ax.boxplot(data, tick_labels=['Sensor A', 'Sensor B'])
    
    # Calculate combined mean for the dashed line
    combined_mean = np.mean(np.concatenate([sensor_a, sensor_b]))
    ax.axhline(combined_mean, color='red', linestyle='--', label=f'Mean: {combined_mean:.2f}')
    
    ax.set_title('Sensor Comparison Boxplot')
    ax.set_ylabel('Temperature (°C)')
    ax.legend()

def main():
    """
    Orchestrate data generation and visualization.

    Generates synthetic data, initializes a multi-panel figure, populates
    subplots using specific plotting functions, and saves the output.
    """
    # 1. Generate data
    sensor_a, sensor_b, timestamps = generate_data(seed=42)

    # 2. Create figure with 4 subplot slots (2 rows, 2 columns)
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    ax1, ax2 = axes[0]
    ax3, ax4 = axes[1]

    # 3. Call plotting functions
    plot_scatter(sensor_a, sensor_b, timestamps, ax1)
    plot_histogram(sensor_a, sensor_b, ax2)
    plot_boxplot(sensor_a, sensor_b, ax3)

    # 4. Leave the fourth subplot empty
    ax4.axis('off')

    # 5. Final layout adjustments and save as requested by Lab Guide
    plt.tight_layout()
    plt.savefig('sensor_analysis.png', dpi=150, bbox_inches='tight')
    print("Successfully generated sensor_analysis.png")

# 6. Execution block (The Security Guard)
if __name__ == "__main__":
    main()
