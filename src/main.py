from src.components.system import System
from src.generator._1_instruments import decide_instruments
from src.generator._2_form import generate_form
from src.memory import system
from src.files import name, choices_file, overwrite_choices
from src.utility.yaml import save_yaml

if __name__ == "__main__":

  # If overwrite is set to true, we should clear
  # the choices file.
  if overwrite_choices: choices_file.clear()

  # 1) Decide instruments.
  instruments = decide_instruments()
  system.setInstruments(instruments=instruments)
  print(f"Instruments=({system.toInstrumentString()})")

  # 2) Decide form.
  form = generate_form()
  system.setForm(form)
  print(f"Form=")

  # Save Choices.
  save_yaml(file_path=f"music/{name}/choices.yaml", data=choices_file)

  
  
  