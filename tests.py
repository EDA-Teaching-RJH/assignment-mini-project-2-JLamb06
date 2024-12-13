import pytest
from Game import ur_dice_roll, game_dice_roll, fox, stegosaurus, game, complete, Character

def testname():
    c = Character("Ash","sword","knight")
    assert c.name == "Ash"
    assert c.weapon == "sword"
    assert c.type == "knight"

def test_complete():
    try:
        assert complete("12345")
    except ValueError as exc:
        pytest.fail(exc, pytrace=True)