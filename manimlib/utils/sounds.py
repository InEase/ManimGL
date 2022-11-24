from __future__ import annotations

import os

from manimlib.utils.directories import get_sound_dir, get_project_root
from manimlib.utils.file_ops import find_file


def get_full_sound_file_path(sound_file_name: str) -> str:
    return find_file(
        sound_file_name,
        directories=[
            os.path.join(get_project_root(), "assets/raster"),
            get_sound_dir()
        ],
        extensions=[".wav", ".mp3", ""]
    )
