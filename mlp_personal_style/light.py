"""
Light theme styles for matplotlib.

This module provides light-themed styles for matplotlib that can be used directly
with plt.style.use().

Example:
    from matplotlib import pyplot as plt
    from mlp_personal_style import light
    
    plt.style.use(light.incredible_style)
"""

from pathlib import Path

# Get the directory where the styles are located
_styles_dir = Path(__file__).parent / 'styles'

# Define style paths as module attributes
incredible_style = str(_styles_dir / 'light_incredible.mplstyle')

# List of all styles available in this module
available_styles = [incredible_style]