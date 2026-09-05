import yaml


def get_yaml_data(file_path: str) -> dict:
  with open(file_path) as file:
    data = yaml.safe_load(file)
  return data