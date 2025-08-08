from pathlib import Path

__current_dir = Path(__file__).parent

ivorygrid = __current_dir / "ivorygrid.mplstyle"
forestlight = __current_dir / "forestlight.mplstyle"
sealight = __current_dir / "sealight.mplstyle"

avaiable_styles: dict[str, Path] = {
    "ivorygrid": ivorygrid,
    "forestlight": forestlight,
    "sealight": sealight,
}
