from importlib import resources
from pathlib import Path


def _style_path(name: str) -> Path:
    """Return the absolute Path to a style file inside the package."""
    return resources.files(__package__) / "styles" / name

avaiable_styles = [
    
    Path(__file__).parent.joinpath("styles").iterdir()
]

charcoal: str = _style_path("charcoal.mplstyle").as_posix()
forestdark: str = _style_path("forestdark.mplstyle").as_posix()
forestlight: str = _style_path("forestlight.mplstyle").as_posix()
ivorygrid: str = _style_path("ivorygrid.mplstyle").as_posix()
sealight: str = _style_path("sealight.mplstyle").as_posix()