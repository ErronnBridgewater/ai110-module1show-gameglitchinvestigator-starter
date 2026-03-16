def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":  #FIX: Refactored logic into logic_utils.py using Copilot Agent mode
        return 1, 20
    if difficulty == "Normal": #FIX: Refactored logic into logic_utils.py using Copilot Agent mode
        return 1, 100
    if difficulty == "Hard": #FIX: Refactored logic into logic_utils.py using Copilot Agent mode
        return 1, 50
    return 1, 100


def parse_guess(raw: str): 
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None: #FIX: Refactored logic into logic_utils.py using Copilot Agent mode
        return False, None, "Enter a guess."

    if raw == "": #FIX: Refactored logic into logic_utils.py using Copilot Agent mode
        return False, None, "Enter a guess."

    try:
        if "." in raw: #FIX: Refactored logic into logic_utils.py using Copilot Agent mode
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None #FIX: Refactored logic into logic_utils.py using Copilot Agent mode


def check_guess(guess, secret):
    """
    Compare guess to secret and return outcome.

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win"

    try:
        if guess > secret: #FIX: Refactored logic into logic_utils.py using Copilot Agent mode
            return "Too High"
        else:
            return "Too Low"
    except TypeError: #FIX: Refactored logic into logic_utils.py using Copilot Agent mode
        g = str(guess)
        if g == secret:
            return "Win"
        if g > secret:
            return "Too High"
        return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int): 
    """Update score based on outcome and attempt number."""
    if outcome == "Win": #FIX: Refactored logic into logic_utils.py using Copilot Agent mode
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High": #FIX: Refactored logic into logic_utils.py using Copilot Agent mode
        if attempt_number % 2 == 0: 
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low": #FIX: Refactored logic into logic_utils.py using Copilot Agent mode
        return current_score - 5

    return current_score
