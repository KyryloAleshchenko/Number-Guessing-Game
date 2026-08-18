# Number Guessing Game

A simple command-line game where you try to guess a randomly generated number between 1 and 100.

## How it works

1. The game picks a random number between 1 and 100.
2. You choose a difficulty level, which sets how many guesses you get:
   - **Easy** — 10 chances
   - **Medium** — 5 chances
   - **Hard** — 3 chances
3. After each guess, you're told whether the number is higher or lower.
4. Guess the number before you run out of chances to win!

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) (for dependency management)

## Setup

```bash
uv sync
```

## Running the game

```bash
uv run python main/game_engine.py
```

## Running tests

```bash
uv run pytest
```
