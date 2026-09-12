from src.files import instruments_file
from src.components.note import Pitch


class Instrument:
  name: str = None
  range: list[Pitch] = []
  midi_index = None
  order = None

  def __init__(self, instrument_name: str):
    self.name = instrument_name
    # Get instrument data.
    data = instruments_file.get(instrument_name, None)
    if data == None: raise Exception(f"Carnt find instrument {instrument_name}")
    # Set pitch range.
    for pitch in data.get("range", []):
      self.range.append(Pitch(pitch=pitch))
    # Set other values.
    self.midi_index = data.get("midi_index", 0)
    self.order = data.get("order", 0)