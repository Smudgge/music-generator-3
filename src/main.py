from src.components.system import System
from src.utility.yaml import get_yaml_data, create_or_get_yaml_file
from src.generator._1_instruments import decide_instruments


# Settings
settings = get_yaml_data("settings.yaml")
name = settings.get("name", "op1")
play_music = settings.get("play_music", True)


# Music theory.
instruments_file = get_yaml_data("theory/_1_instruments.yaml")
chords_file = get_yaml_data("theory/chords.yaml")
progressions_file = get_yaml_data("theory/progressions.yaml")


# Composition
file = create_or_get_yaml_file(f"music/{name}/choices.yaml")
system = System()




if __name__ == "__main__":

  # 1) Decide instruments.
  instruments = decide_instruments()


  