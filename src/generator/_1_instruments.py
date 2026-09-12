from src.components.instrument import Instrument
from src.files import instruments_file, ensembles_file
from src.files import choices_file
import random


def decide_instruments() -> list[Instrument]:
  # Check if instruments have already been chosen.
  choice = choices_file.get("instruments", None)
  if not choice: choice = random.choice(list(ensembles_file.values()))
  # Create list of instruments.
  instruments: list[Instrument] = []
  for instrument_name in choice:
    instruments.append(Instrument(instrument_name=instrument_name))
  # Save choice and return instruments.
  choices_file["instruments"] = choice
  return instruments
