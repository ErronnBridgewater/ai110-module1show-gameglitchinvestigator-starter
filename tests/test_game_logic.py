<<<<<<< HEAD
from logic_utils import check_guess, update_score, get_range_for_difficulty
=======
from logic_utils import check_guess
>>>>>>> d28145213e029bd9f9244f5f8071e0985a5e266e

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"
<<<<<<< HEAD


# --- Tests targeting the new-game reset glitch ---

def test_first_guess_score_uses_attempt_1_not_0():
    # Bug: reset set attempts=0, so the first guess after reset was scored as
    # attempt #0, giving 100 - 10*(0+1) = 90 points instead of the correct
    # 100 - 10*(1+1) = 80 points. After the fix, attempts resets to 1.
    score_correct = update_score(0, "Win", attempt_number=1)   # fixed behaviour
    score_bugged  = update_score(0, "Win", attempt_number=0)   # old bugged behaviour
    assert score_correct == 80
    assert score_bugged  == 90  # documents what the bug produced
    assert score_correct != score_bugged


def test_get_range_easy_not_full_range():
    # Bug: reset always called random.randint(1, 100) regardless of difficulty.
    # On Easy the range must be 1–20, not 1–100.
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20
    assert high != 100  # would be 100 with the bugged hard-coded range


def test_get_range_hard_not_full_range():
    # Same bug: Hard mode should use 1–50, not 1–100.
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50
    assert high != 100


def test_get_range_normal():
    # Normal mode correctly uses 1–100; verifies the non-glitch path is intact.
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100
=======
>>>>>>> d28145213e029bd9f9244f5f8071e0985a5e266e
