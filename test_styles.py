from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from mlp_personal_style import avaiable_styles

output_image_folder = Path(__file__).parent.joinpath("test_images")


def plot_data(data, stylepath: Path, stylename: str):
    """
    Create the exact plot shown in the image using minimal libraries (matplotlib only).

    Args:
        data: Dictionary containing all plot data from generate_dataset()
    """
    with plt.style.context(stylepath):
        # Set up the figure with light gray background
        fig = plt.figure(figsize=(15, 3))

        # Create subplots
        gs = fig.add_gridspec(
            1,
            5,
            width_ratios=[1, 1, 1, 1, 1],
            left=0.05,
            right=0.95,
            top=0.85,
            bottom=0.15,
            wspace=0.3,
        )

        # Add main title
        fig.suptitle(f"{stylename} light", fontsize=14, fontweight="normal", y=0.95)

        # Subplot 1: Scatter plot
        ax1 = fig.add_subplot(gs[0])

        # Plot blue circles
        ax1.scatter(
            data["scatter"]["x_blue"],
            data["scatter"]["y_blue"],
            s=30,
            alpha=0.7,
            marker="o",
        )

        # Plot pink squares
        ax1.scatter(
            data["scatter"]["x_pink"],
            data["scatter"]["y_pink"],
            s=25,
            alpha=0.7,
            marker="s",
        )

        ax1.set_xlim(-2.5, 4)
        ax1.set_ylim(-2.5, 3.5)
        ax1.set_xlabel("x-label")

        # Subplot 2: Overlapping histograms with annotation
        ax2 = fig.add_subplot(gs[1])

        # Plot histograms
        ax2.hist(data["histogram"]["hist1"], bins=30, alpha=0.7, density=True)
        ax2.hist(data["histogram"]["hist2"], bins=30, alpha=0.7, density=True)
        ax2.hist(data["histogram"]["hist3"], bins=25, alpha=0.8, density=True)

        # Add annotation box and arrow
        bbox_props = dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.8)
        ax2.annotate(
            "Annotation",
            xy=(0.7, 7),
            xytext=(0.5, 9),
            bbox=bbox_props,
            fontsize=9,
            arrowprops=dict(arrowstyle="->", color="black", lw=1),
        )

        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 10)
        ax2.tick_params(labelsize=8)

        # Subplot 3: Grouped bar chart
        ax3 = fig.add_subplot(gs[2])

        x_pos = np.arange(len(data["bar"]["categories"]))
        width = 0.35

        bars1 = ax3.bar(x_pos - width / 2, data["bar"]["values1"], width, alpha=0.7)
        bars2 = ax3.bar(x_pos + width / 2, data["bar"]["values2"], width, alpha=0.7)

        ax3.set_xticks(x_pos)
        ax3.set_xticklabels(data["bar"]["categories"])
        ax3.set_ylim(0, 22)
        ax3.tick_params(labelsize=8)

        # Subplot 4: Bubble chart
        ax4 = fig.add_subplot(gs[3])

        for i in range(len(data["bubble"]["x"])):
            ax4.scatter(
                data["bubble"]["x"][i],
                data["bubble"]["y"][i],
                alpha=0.7,
            )

        ax4.set_xlim(-2.5, 6)
        ax4.set_ylim(-4.5, 4)

        # Subplot 5: Sine waves
        ax5 = fig.add_subplot(gs[4])

        for i, wave in enumerate(data["waves"]["waves"]):
            ax5.plot(
                data["waves"]["x"],
                wave,
                linewidth=2,
                alpha=0.8,
            )

        ax5.set_xlim(0, 6)
        ax5.set_ylim(-1.2, 1.2)

        fig.savefig(output_image_folder / f"scatter_{stylepath.stem}.png")


def generate_dataset():
    """
    Generate dataset suitable for creating the exact plot shown in the image.
    Returns a dictionary containing all the data needed for each subplot.
    """
    np.random.seed(42)  # for reproducibility

    # Subplot 1: Scatter plot with two groups
    n_points = 100

    # Blue dots (bottom cluster)
    x1_blue = np.random.normal(-0.5, 0.3, n_points // 2)
    y1_blue = np.random.normal(-1, 0.3, n_points // 2)

    # Pink squares (top-right cluster)
    x1_pink = np.random.normal(1.5, 0.8, n_points // 2)
    y1_pink = np.random.normal(1.5, 0.8, n_points // 2)

    scatter_data = {
        "x_blue": x1_blue,
        "y_blue": y1_blue,
        "x_pink": x1_pink,
        "y_pink": y1_pink,
    }

    # Subplot 2: Overlapping histograms
    hist1 = np.random.beta(2, 5, 1000) * 0.8  # Cyan distribution
    hist2 = np.random.beta(8, 2, 800) * 0.8 + 0.2  # Purple distribution
    hist3 = np.random.beta(12, 3, 600) * 0.3 + 0.65  # Pink distribution

    histogram_data = {"hist1": hist1, "hist2": hist2, "hist3": hist3}

    # Subplot 3: Grouped bar chart
    categories = ["a", "b", "c", "d", "e"]
    values1 = [15, 20, 18, 16, 10]  # Blue bars
    values2 = [12, 17, 15, 14, 8]  # Pink bars

    bar_data = {"categories": categories, "values1": values1, "values2": values2}

    # Subplot 4: Bubble chart
    bubble_x = [0, 2.5, 5, 1, 3]
    bubble_y = [0, 2, 0, -3, -3]
    bubble_sizes = [800, 400, 1200, 600, 300]
    bubble_colors = ["cyan", "lightcoral", "cyan", "magenta", "blue"]

    bubble_data = {
        "x": bubble_x,
        "y": bubble_y,
        "sizes": bubble_sizes,
        "colors": bubble_colors,
    }

    # Subplot 5: Sine waves
    x = np.linspace(0, 6, 200)
    waves = []
    colors = ["magenta", "red", "cyan", "green", "blue", "orange"]

    for i in range(6):
        phase = i * np.pi / 3
        wave = np.sin(x + phase)
        waves.append(wave)

    wave_data = {"x": x, "waves": waves, "colors": colors}

    return {
        "scatter": scatter_data,
        "histogram": histogram_data,
        "bar": bar_data,
        "bubble": bubble_data,
        "waves": wave_data,
    }


# Generate dataset
dataset = generate_dataset()

for style, stylepath in avaiable_styles.items():
    plot_data(dataset, stylepath=stylepath, stylename=style)
