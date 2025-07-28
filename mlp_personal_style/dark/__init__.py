from pathlib import Path

__current_dir = Path(__file__).parent

charcoal = __current_dir / "charcoal.mplstyle"
forestdark = __current_dir / "forestdark.mplstyle"

available_styles: dict[str, Path] = {"charcoal": charcoal, "forestdark": forestdark}
