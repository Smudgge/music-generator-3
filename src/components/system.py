from src.components.instrument import Instrument
from src.components.stave import Stave


class System:
  staves: dict[int, Stave] = {}

  
  def __str__(self):
    string_builder = ""
    for stave in self.staves.values():
      string_builder += ("  " + stave.__str__() + ", \n")
    return f"System(staves=(\n{string_builder}))"

  def toInstrumentString(self) -> str:
    string_builder = ""
    for stave in self.staves.values():
      string_builder += f"{stave.id}={stave.instrument.name}, "
    return string_builder[0:-2]

  def setInstruments(self, instruments: list[Instrument]):
    for index, instrument in enumerate(instruments):
      self.staves[index] = Stave(id=index, instrument=instrument)


  def getStave(self, index: int) -> Stave:
    return self.staves[index]