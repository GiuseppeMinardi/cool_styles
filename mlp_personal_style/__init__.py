"""
MLPPersonalStyle - Simple Matplotlib Style Package

This package provides custom matplotlib styles that can be easily imported and used.

Example:
    from matplotlib import pyplot as plt
    from mlp_personal_style import light, dark
    
    plt.style.use(light.incredible_style)
"""

from . import light
from . import dark

__version__ = "0.1.0"