from src.components.instrument import Instrument


class Stave:
  id: int
  instrument: Instrument
  

  def __init__(self, id: int,  instrument: Instrument):
    self.id = id
    self.instrument = instrument

  def __str__(self):
    return f"Stave(id={self.id}, instrument={self.instrument.name})"