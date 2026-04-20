# Sensor Data Visualization

This project generates synthetic temperature sensor data and saves a publication-style figure with three comparative plots.

## Installation

Activate the `ece105` conda environment, then install the required Python packages:

```powershell
conda activate ece105
conda install numpy matplotlib
```

If you prefer `mamba`, you can use:

```powershell
conda activate ece105
mamba install numpy matplotlib
```

## Usage

Run the script from the project directory with:

```powershell
python generate_plots.py
```

The script uses a fixed random seed for reproducibility, generates 200 simulated readings for each of two sensors, and saves the resulting figure to the current directory.

## Example Output

Running the script produces the file `sensor_analysis.png`.

That image contains three plots arranged in a single row:

1. A scatter plot of Sensor A and Sensor B temperature readings versus time from 0 to 10 seconds.
2. An overlaid histogram comparing the temperature distributions of the two sensors.
3. A box plot comparing Sensor A and Sensor B, including a dashed horizontal line showing the combined mean temperature.

## AI Tools Used and Disclosure

[Placeholder paragraph: describe any AI tools used to help with planning, writing, debugging, or documentation for this project, and include any disclosure language required by your course or instructor.]
