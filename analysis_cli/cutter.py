import os
from importlib import resources

from cookiecutter.main import cookiecutter


def cutter(wp, analysis, output_dir="."):

    init_loc = resources.path(__package__, '__init__.py')
    folder, _ = os.path.split(init_loc)

    print(f"Folder is: {folder}")
    print(folder)

    prefix = f"5.{wp + 1}.{analysis + 2}"
    project_name = f"{prefix} Analysis {analysis}"

    extra_context = {
        "project_name": project_name,
        "prefix": prefix
    }

    val = cookiecutter(folder, no_input=True, overwrite_if_exists=True,
                       extra_context=extra_context, output_dir=output_dir)

    return val
