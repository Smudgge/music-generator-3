**Classical music generator V3**
Creates music using random numbers and music theory.Essentially starting with selecting instuments, structure, form all the way to selecting harmonies and melodies by selecting random options. This is the 3rd version of this generator, the first one only generated for 5 strings, this aims to be more flexible supporting any combo of instuments.

## Running the music generator
- Install requirements `pip install -r requirements.txt`
- Run project
- - `./run.sh` or
- - `PYTHONPYCACHEPREFIX=.cache python -m src.main` or
- - `PYTHONPYCACHEPREFIX=.cache python3 -m src.main`

## Creating music
- See `settings.yaml` for main configurable values.
- See `theory` to change the musical tool box.
