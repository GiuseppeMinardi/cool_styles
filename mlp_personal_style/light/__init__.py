from pathlib import Path

__current_dir = Path(__file__).parent

ivorygrid = __current_dir / "ivorygrid.mplstyle"
papyrus = __current_dir / "papyrus.mplstyle"
forestlight = __current_dir / "forestlight.mplstyle"

avaiable_styles: dict[str, Path] = {
    "ivorygrid": ivorygrid,
    "papyrus": papyrus,
    "forestlight": forestlight,
}
