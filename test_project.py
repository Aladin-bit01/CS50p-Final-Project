import pygame
import pytest
import project
import re

image_surf= project.image_surface('Graphics/start_screen_little_professo.png')

def test_display_operation():
    addition = project.display_operation(['Addition', 1])
    match1 = re.search(r'^([0-9]+ \+ [0-9]+ =$)', addition).group(1)
    assert addition == match1

    multiplication = project.display_operation(['Multiplication', 1])
    match2 = re.search(r'^([0-9]+ x [0-9]+ = $)', multiplication).group(1)
    assert multiplication == match2

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

def test_image_rect():
    assert type(image_surf) == pygame.Surface

def test_image_rect():
    assert type(project.image_rect(image_surf,100,200)) == pygame.Rect



