from src.main import instruments_file


class Instrument:
  range: list[str] = []
  midi_index = 0
  order = 10

  def __init__(self, instrument_name: str):
    data = instruments_file.get(instrument_name, None)
    if data == None: raise Exception(f"Carnt find instrument {instrument_name}")
    self.range = data.get("range", [])
    self.midi_index = data.get("midi_index", 0)
    self.order = data.get("order", 0)