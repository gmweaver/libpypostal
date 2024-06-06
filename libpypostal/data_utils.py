"""Libpostal data utils."""
import importlib.resources
import os
import subprocess
from typing import Literal

LIBPOSTAL_DATA_DIR_ENV_NAME = "LIBPOSTAL_DATA_DIR"
DEFAULT_DATA_VERSION = "v1.0.0"


def set_data_dir_env_var(data_dir: str) -> None:
    """Sets libpostal data directory environment variable."""
    os.environ[LIBPOSTAL_DATA_DIR_ENV_NAME] = data_dir


def download_libpostal_data(
    # pylint: disable=too-many-arguments
    output_dir: str,
    file: Literal["base", "parser", "language_classifier", "all"] = "all",
    data_dir_version: str = DEFAULT_DATA_VERSION,
    data_file_version: str = DEFAULT_DATA_VERSION,
    parser_model_version: str = DEFAULT_DATA_VERSION,
    lang_class_model_version: str = DEFAULT_DATA_VERSION,
    set_env_var: bool = True,
) -> None:
    """Downloads libpostal data.

    Arguments:
        output_dir: directory to download and expand data files to.
        file: data files to download.
        data_dir_version: data directory version.
        data_file_version: data file version.
        parser_model_version: parser model version.
        lang_class_model_version: lang class model version.
        set_env_var: indicates whether LIBPOSTAL_DATA_DIR should be set.
    """
    with importlib.resources.path(
        "libpypostal", "libpostal_download_data"
    ) as script_path:
        subprocess.run(
            [
                script_path.as_posix(),
                "download",
                file,
                output_dir,
                data_dir_version,
                data_file_version,
                parser_model_version,
                lang_class_model_version,
            ],
            check=True,
        )

    if set_env_var:
        set_data_dir_env_var(output_dir)
