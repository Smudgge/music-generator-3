from src.theory import instruments_file


class Instrument:
  range: list[str] = []
  midi_index = 0
  standard_amount = 0
  order = 10

  def __init__(this, instrument_name: str):
    data = instruments_file.get(instrument_name, None)
    if data == None: raise Exception(f"Carnt find instrument {instrument_name}")
    this.range = data.get("range", [])
    this.midi_index = data.get("midi_index", 0)
    this.standard_amount = data.get("standard_amount", 0)
    this.order = data.get("order", 0)


def decide_instruments() -> list[Instrument]:
  return