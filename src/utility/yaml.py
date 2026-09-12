import os
import yaml


def get_yaml_data(file_path: str) -> dict:
  with open(file_path) as file:
    data = yaml.safe_load(file)
  return data


def create_or_get_yaml_file(file_path: str) -> dict:
  # If the file exists return the data.
  if os.path.exists(file_path):
    return get_yaml_data(file_path)
  # Create parent directories if they don't exist.
  os.makedirs(os.path.dirname(file_path), exist_ok=True)
  # Create empty yaml file.
  with open(file_path, "w") as f:
      yaml.dump({}, f)
  return {}


def save_yaml(file_path: str, data: dict):
  with open(file_path, "w") as f:
    yaml.dump(data, f)
  