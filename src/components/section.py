from __future__ import annotations


class Section:
  key: str = None
  sub: Section = None # For form within a form.

  def __init__(self, key: str, sub: Section = None):
    self.key = key
    self.sub = sub

  def __str__(self):
    if self.key: return f"{self.key}{self.sub}"
    return f"{self.key}"