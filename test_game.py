from main.config import CHANCES, EASY, HARD, MEDIUM
from main.game_engine import NumberGuess


def make_input(values):
    """Return a fake `input` that yields each value in turn, ignoring the prompt."""
    values_iter = iter(values)
    return lambda prompt="": next(values_iter)


class TestInit:
    def test_random_number_within_range(self):
        game = NumberGuess()
        assert 1 <= game.random_number <= 100

    def test_random_number_uses_random_randint(self, monkeypatch):
        monkeypatch.setattr("main.game_engine.random.randint", lambda a, b: 42)
        game = NumberGuess()
        assert game.random_number == 42

    def test_chances_start_at_zero(self):
        game = NumberGuess()
        assert game.chances == 0


class TestStart:
    def test_returns_welcome_message(self):
        game = NumberGuess()
        message = game.start()
        assert "Welcome to the Number Guessing Game!" in message
        assert "1. Easy (10 chances)" in message
        assert "2.Medium (5 chances)" in message
        assert "3. Hard (3 chances)" in message


class TestDifficulty:
    def test_easy_sets_chances(self, monkeypatch):
        game = NumberGuess()
        monkeypatch.setattr("builtins.input", make_input([str(EASY)]))
        game.difficulty()
        assert game.chances == CHANCES[0]

    def test_medium_sets_chances(self, monkeypatch):
        game = NumberGuess()
        monkeypatch.setattr("builtins.input", make_input([str(MEDIUM)]))
        game.difficulty()
        assert game.chances == CHANCES[1]

    def test_hard_sets_chances(self, monkeypatch):
        game = NumberGuess()
        monkeypatch.setattr("builtins.input", make_input([str(HARD)]))
        game.difficulty()
        assert game.chances == CHANCES[-1]

    def test_non_numeric_input_is_rejected_then_retries(self, monkeypatch, capsys):
        game = NumberGuess()
        monkeypatch.setattr("builtins.input", make_input(["abc", str(EASY)]))
        game.difficulty()
        assert game.chances == CHANCES[0]
        assert "Enter valid number!" in capsys.readouterr().out

    def test_out_of_range_number_is_rejected_then_retries(self, monkeypatch, capsys):
        game = NumberGuess()
        monkeypatch.setattr("builtins.input", make_input(["4", str(MEDIUM)]))
        game.difficulty()
        assert game.chances == CHANCES[1]
        assert "Please enter valid number" in capsys.readouterr().out


class TestIsWon:
    def test_correct_guess_wins_immediately(self, monkeypatch, capsys):
        game = NumberGuess()
        game.random_number = 50
        game.chances = 3
        monkeypatch.setattr("builtins.input", make_input(["50"]))
        game.is_won()
        assert game.chances == 3
        assert "Congratulations! You won!" in capsys.readouterr().out

    def test_wrong_guesses_decrement_chances_until_exhausted(self, monkeypatch, capsys):
        game = NumberGuess()
        game.random_number = 50
        game.chances = 2
        monkeypatch.setattr("builtins.input", make_input(["10", "20"]))
        game.is_won()
        assert game.chances == 0
        out = capsys.readouterr().out
        assert out.count("Incorrect guess. Try again.") == 2

    def test_invalid_input_decrements_chances(self, monkeypatch, capsys):
        game = NumberGuess()
        game.random_number = 50
        game.chances = 1
        monkeypatch.setattr("builtins.input", make_input(["abc"]))
        game.is_won()
        assert game.chances == 0
        assert "Enter valid value" in capsys.readouterr().out

    def test_zero_chances_never_prompts(self, monkeypatch):
        game = NumberGuess()
        game.chances = 0

        def fail_input(prompt=""):
            raise AssertionError("input() should not be called when chances is 0")

        monkeypatch.setattr("builtins.input", fail_input)
        game.is_won()

    def test_wrong_then_correct_guess(self, monkeypatch, capsys):
        game = NumberGuess()
        game.random_number = 50
        game.chances = 3
        monkeypatch.setattr("builtins.input", make_input(["10", "50"]))
        game.is_won()
        assert game.chances == 2
        out = capsys.readouterr().out
        assert "Incorrect guess. Try again. You have 2 chances" in out
        assert "Congratulations! You won!" in out