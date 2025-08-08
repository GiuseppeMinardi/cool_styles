from pathlib import Path  # noqa: D100

import matplotlib.pyplot as plt
import mpl_personal_style
import pytest


@pytest.mark.parametrize("style_var", [
    "charcoal",
    "forestdark",
    "forestlight",
    "ivorygrid",
    "seadark",
    "sealight",
])
def test_style_path_exists(style_var):
    """Check that the style variable exists and points to a valid file."""
    style_path = getattr(mpl_personal_style, style_var)

    assert isinstance(style_path, Path), f"{style_var} is not a Path"
    assert style_path.suffix == ".mplstyle", f"{style_var} is not a .mplstyle file"
    assert style_path.exists(), f"{style_var} file does not exist"


@pytest.mark.parametrize("style_var", [
    "charcoal",
    "forestdark",
    "forestlight",
    "ivorygrid",
    "seadark",
    "sealight",
])
def test_matplotlib_can_use_style(style_var):
    """Ensure matplotlib can load the style without errors."""
    style_path = getattr(mpl_personal_style, style_var)

    try:
        plt.style.use(style_path)
    except Exception as e:
        pytest.fail(f"Failed to load style {style_var}: {e}")