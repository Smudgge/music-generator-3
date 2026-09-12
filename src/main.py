from src.components.system import System
from src.generator._1_instruments import decide_instruments
from src.memory import system
from src.files import name, choices_file
from src.utility.yaml import save_yaml

if __name__ == "__main__":

  # 1) Decide instruments.
  instruments = decide_instruments()
  system.setInstruments(instruments=instruments)

  # Save Choices.
  save_yaml(file_path=f"music/{name}/choices.yaml", data=choices_file)

  print(system)
  

  
  
  