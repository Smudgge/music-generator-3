from src.components.system import System
from src.components.note import Note, Pitch, SEMIBREVE
from src.utility.yaml import get_yaml_data, create_or_get_yaml_file
from src.generator._1_instruments import decide_instruments


# Settings
settings = get_yaml_data("settings.yaml")
name = settings.get("name", "op1")
play_music = settings.get("play_music", True)


# Composition
file = create_or_get_yaml_file(f"music/{name}/choices.yaml")
system = System()


if __name__ == "__main__":

  # 1) Decide instruments.
  instruments = decide_instruments()

  note = Note(Pitch('C3'), SEMIBREVE)
  print(note)

  