import random
import pytest
import source.games as games

# Parameterize the test with different fixed random values
@pytest.mark.parametrize("fixed_rand", [10, 50, 90])
def test_win_game(monkeypatch, capsys, fixed_rand):
    """
    Test a winning scenario.
    The fixed random number is set to 50.
    The user enters guesses: "30" (too low), "60" (too high), and finally "50" (correct).
    """
    # Force random.randint to always return 50
    monkeypatch.setattr(random, "randint", lambda a, b: fixed_rand)
    
    # Simulate user inputs: first "30", then "60", then "50"
    inputs = iter([str(fixed_rand)])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    games.guessing_game()  # Run the game
    
    # Capture the output
    captured = capsys.readouterr().out
    # Verify that the win message is in the output
    assert "Congratulations" in captured

def test_lost_game(monkeypatch, capsys):
    """
    Test a scenario where the user loses.
    The fixed random number is 50.
    The user enters three wrong guesses.
    """
    monkeypatch.setattr(random, "randint", lambda a, b: 50)
    
    # Provide three incorrect guesses (all lower than 50, so the user never reaches the correct answer)
    inputs = iter(["30", "40", "20"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    games.guessing_game()  # Run the game
    
    captured = capsys.readouterr().out
    # Verify that the loss message is printed
    assert "You lost" in captured

def test_invalid_input(monkeypatch, capsys):
    """
    Test a scenario where the user inputs an invalid integer.
    The game should notify the user about the invalid input and then allow further guesses.
    """
    # Force random.randint to always return 50
    monkeypatch.setattr(random, "randint", lambda a, b: 50)
    
    # Simulate user inputs: first "30", then "60", then "50"
    inputs = iter(["abc", "60", "50"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    games.guessing_game()  # Run the game
    
    # Capture the output
    captured = capsys.readouterr().out
    # Verify that the error message for invalid input is printed
    assert "is not a valid integer" in captured
    # Verify that the win message is in the output
    assert "Congratulations" in captured