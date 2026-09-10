from src.theory import notes_file


def pitch_expanded(pitch: str) -> tuple[str, int]:
  return (pitch[0:-1], int(pitch[-1]))


def pitch_to_midi(pitch: str) -> int:
  (letter, octave) = pitch_expanded(pitch)
  octave_direction = octave - 4
  midi_octave_4 = notes_file[letter]
  return midi_octave_4 + (octave_direction * 12)


def midi_to_pitch(midi: int, sharps: bool = True) -> str:
  candidates = []
  # Loop though all letters to see which match.
  for letter, midi_octave_4 in notes_file.items():
    diff = midi - midi_octave_4
    if diff % 12 == 0:
      octave = (diff // 12) + 4
      candidates.append(f"{letter}{octave}")
  # If none match raise error.
  if len(candidates) == 0: raise ValueError(f"No pitch found for midi value {midi}")
  # Find smallest candidates [C#, Db].
  min_length = min(len(c) for c in candidates)
  smallest = [c for c in candidates if len(c) == min_length]
  # If theres only one candidate return that.
  if len(smallest) == 1: return smallest[0]
  # Return the first candidate that abides by {sharps}
  for candidate in smallest:
    if sharps and "#" in candidate:
      return candidate
    if not sharps and "b" in candidate:
      return candidate
  raise ValueError(f"No {'sharp' if sharps else 'flat'} spelling found among {smallest}")


def validate_midi(midi: int):
  if midi < 12:
    raise ValueError(f"Midi pitch cannot be below C0 (12). pitch={midi}")
  if midi > 127:
    raise ValueError(f"Midi pitch cannot be higher than G9 (127). pitch={midi}")


class Pitch:
  """
  C4 = 60
  C3 = 48
  C2 = 36
  C1 = 24 (+12)
  C0 = 12
  """
  pitch = 'C0'
  midi = 12
  letter = 'C'
  octave = 0

  def __init__(self, pitch: str = None, letter: str = None, octave: int = None, midi: int = None):
    # Find midi number value from arguments.
    if pitch is not None:
      midi = pitch_to_midi(pitch)
    elif letter is not None and octave is not None:
      midi = pitch_to_midi(f"{letter}{octave}")
    else:
      raise ValueError("Must provide either pitch, letter+octave, or midi")
    # Validate midi number.
    validate_midi(midi)
    # Set values.
    self.midi = midi
    self.pitch = midi_to_pitch(self.midi)
    (self.letter, self.octave) = pitch_expanded(self.pitch)

  def __str__(self) -> str:
    return f"Pitch(pitch={self.pitch}, midi={self.midi})"

  def add(self, semitones: int):
    self.midi += semitones
    self.pitch = midi_to_pitch(self.midi)
    (self.letter, self.octave) = pitch_expanded(self.pitch)


SEMIBREVE = 0
MINIM = 2
CROTCHET = 4
QUAVER = 8


class Note:
  pitch: Pitch = Pitch(pitch='C0')
  duration = 0 # Semibreve / Full bar of 4/4

  def __init__(self, pitch: Pitch, duration: int):
    self.pitch = pitch
    self.duration = duration

  def __str__(self) -> str:
    return f"Note(duration={self.duration}, pitch={self.pitch})"
