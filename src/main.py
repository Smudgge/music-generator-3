from src.components.system import System
from src.utility.yaml import get_yaml_data


# Settings
settings = get_yaml_data("settings.yaml")
name = settings.get("name", "op1")
play_music = settings.get("play_music", True)


# 1) Music theory.


# 2) Structure.



if __name__ == "__main__":

  # 1) Load music theory.

  # 2) Generate structure.
  system = System()


  