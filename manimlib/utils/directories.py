from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

from manimlib.utils.customization import get_customization
from manimlib.utils.file_ops import guarantee_existence
from pyrootutils import find_root

PROJECT_ROOT: Optional[str] = None


def get_project_root() -> str:
    global PROJECT_ROOT
    if PROJECT_ROOT is None:
        PROJECT_ROOT = find_root(search_from=__file__, indicator=[".git", "pyproject.toml"])
    return PROJECT_ROOT


def get_directories() -> dict[str, str]:
    return get_customization()["directories"]


def get_temp_dir() -> str:
    if (Path(get_project_root()) / "temp").exists():
        return str(Path(get_project_root()) / "temp")
    return get_directories()["temporary_storage"]


def get_tex_dir() -> str:
    return guarantee_existence(os.path.join(get_temp_dir(), "Tex"))


def get_text_dir() -> str:
    return guarantee_existence(os.path.join(get_temp_dir(), "Text"))


def get_mobject_data_dir() -> str:
    return guarantee_existence(os.path.join(get_temp_dir(), "mobject_data"))


def get_downloads_dir() -> str:
    return guarantee_existence(os.path.join(get_temp_dir(), "manim_downloads"))


def get_output_dir() -> str:
    return guarantee_existence(get_directories()["output"])


def get_raster_image_dir() -> str:
    return get_directories()["raster_images"]


def get_vector_image_dir() -> str:
    return get_directories()["vector_images"]


def get_sound_dir() -> str:
    return get_directories()["sounds"]


def get_shader_dir() -> str:
    return get_directories()["shaders"]
