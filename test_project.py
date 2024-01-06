import pytest
import project


def test_true_correct_answer():
    assert project.correct_answer('2 + 3= ','5') == True
    assert project.correct_answer('2 - 3= ', '-1') == True
    assert project.correct_answer('2 x 3= ', '6') == True
    assert project.correct_answer('6 / 3= ', '2') == True


def test_false_correct_answer():
    assert project.correct_answer('2 + 3= ', '6') == False
    assert project.correct_answer('2 - 3= ', '-6') == False
    assert project.correct_answer('2 x 3= ', '7') == False
    assert project.correct_answer('6 / 3= ', '1') == False

