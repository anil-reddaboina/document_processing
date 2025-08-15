import yaml
import os
from pathlib import Path


def load_config(config_path: str = "config/config.yaml") -> dict:
    # Get the project root directory (assuming this file is in utils/)
    project_root = Path(__file__).parent.parent
    absolute_config_path = project_root / config_path
    
    with open(absolute_config_path, "r") as file:
        config = yaml.safe_load(file)
    return config
