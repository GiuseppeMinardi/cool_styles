from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import make_classification

from mlp_personal_style import dark, light

output_image_folder = Path(__file__).parent.joinpath("test_images")
# Create a sample dataset
X, y = make_classification(
    n_samples=100,
    n_features=3,
    n_redundant=0,
    random_state=42,
    n_classes=4,
    n_clusters_per_class=1,
)
dataset = pd.DataFrame(X, columns=["Feature1", "Feature2", "Feature3"]).assign(target=y)

for style, stylepath in light.avaiable_styles.items():
    with plt.style.context(stylepath):
        fig, ax = plt.subplots()
        for target, grouped_df in dataset.groupby("target"):
            ax.scatter(
                grouped_df["Feature1"], grouped_df["Feature2"], label=f"Class {target}"
            )
        fig.savefig(output_image_folder / f"scatter_{stylepath.stem}.png")

for style, stylepath in dark.available_styles.items():
    with plt.style.context(stylepath):
        fig, ax = plt.subplots()
        for target, grouped_df in dataset.groupby("target"):
            ax.scatter(
                grouped_df["Feature1"], grouped_df["Feature2"], label=f"Class {target}"
            )
        fig.savefig(output_image_folder / f"scatter_{stylepath.stem}.png")
