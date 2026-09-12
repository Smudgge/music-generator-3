from src.utility.yaml import get_yaml_data, create_or_get_yaml_file

# Settings
settings = get_yaml_data("settings.yaml")
name: str = settings.get("name", "op1")
play_music: bool = settings.get("play_music", True)
overwrite_choices: bool = settings.get("overwrite_choices", False)


# Choices
choices_file = create_or_get_yaml_file(f"music/{name}/choices.yaml")


# Theory
notes_file = get_yaml_data("theory/_0_notes.yaml")
instruments_file = get_yaml_data("theory/_1_instruments.yaml")
ensembles_file = get_yaml_data("theory/_2_ensembles.yaml")
form_file = get_yaml_data("theory/_3_form.yaml")