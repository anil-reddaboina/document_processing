import yaml


def load_config(config_path: str = "config/config.yaml") -> dict:
    """
    Loads a YAML configuration file.

    Args:
        config_path (str): The path to the configuration file. Defaults to "config/config.yaml".

    Returns:
        dict: The loaded configuration as a dictionary.
    """
    with open(config_path, "r") as file:
        config=yaml.safe_load(file)
    return config
