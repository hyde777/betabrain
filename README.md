# BetaBrain
An implementation of the [mastermind](https://en.wikipedia.org/wiki/Mastermind_(board_game)) game in python,
and a working solver.

## Project Structure
```
└──────betabrain/
    ├──────solver/ The solver(s) for the mastermind game
    ├──────GUI/    An example of GUI using the game
    ├──────game/    The actual code running the game
    └──────tests/  Unit test code
```

## Tests
Unit tests are done using the vanilla [`unittest` module](https://docs.python.org/3/library/unittest.html). You
can execute them by doing a
```
python -m unittest tests/*.py
```
