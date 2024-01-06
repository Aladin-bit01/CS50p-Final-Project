import pygame
from sys import exit
import re
import operations
from classes import Display_Operation, Levels, Operations

# Constants
RED = (255,0,0)
SKYBLUE = (152, 195, 195)
BEIGE = (210, 190, 150)
YELLOW = (255, 255, 204)

# Globals
final_state = False
start_the_game = False
choose_level = False
start_playing = False
user_answer = ''
num = 0
score = 0
game_algo = []


def main():
    global num,score,user_answer,start_the_game,choose_level,start_the_game,final_state
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('Little Professor')
    clock = pygame.time.Clock()

    # Images
    little_professor_surf = image_surface('Graphics/start_screen_little_professo.png')
    little_professor_surf = pygame.transform.smoothscale_by(little_professor_surf, 0.4)
    little_professor_rect = image_rect(little_professor_surf, 300, 200)

    # Font
    text_font = pygame.font.Font('Font/Pixeltype.ttf', 50)
    # Game title
    title_surf, title_rect = phrase_rect('Little Professor', 300, 60,text_font)
    # start message
    start_message_surf, start_message_rect = phrase_rect('Press space to start', 300, 350,text_font)

    # Operations
    sentence_surf, sentence_rect = phrase_rect('Choose a Mathematical Operation: ', 300, 50,text_font)

    addition = Operations(80, 200, '+', 'Addition')
    substracction = Operations(230, 200, '-', 'Substraction')
    multiplication = Operations(380, 200, 'x', 'Multiplication')
    division = Operations(530, 200, '/', 'Division')
    operationes = [addition, substracction, multiplication, division]

    command_surf, command_rect = phrase_rect('Select the operation and press space ', 300, 300,text_font)

    # Levels:
    level_surf, level_rect = phrase_rect('Select a level: ', 300, 50,text_font)
    level_1 = Levels(150, 200, 1, '1')
    level_2 = Levels(300, 200, 2, '2')
    level_3 = Levels(450, 200, 3, '3')
    levelos = [level_1, level_2, level_3]

    # Game In Playing
    play_surface = text_font.render('Let\'s Play !', False, (64, 64, 64))
    play_surface_rect = play_surface.get_rect(topleft=(50, 50))
    user_rect = Display_Operation().rect
    user_rect.x = 180
    user_rect.y = 200
    user_rect.w = Display_Operation().rect.w + 5
    answer_prompt_surf = text_font.render('Answer: ', False, (64, 64, 64))
    answer_prompt_rect = answer_prompt_surf.get_rect(topleft=(50, 200))

    click_surf, click_rect = phrase_rect('Press Enter to continue ', 230, 300,text_font)

    # Final State

    restart_surf, restart_rect = phrase_rect('Press Space to play again', 300, 200,text_font)
    mathgame_surf = image_surface('Graphics/mathgame.webp')
    mathgame_surf = pygame.transform.smoothscale_by(mathgame_surf, 0.05)
    mathgame_rect = image_rect(mathgame_surf, 300, 300)

    # Audio
    right_answer_mp3 = pygame.mixer.Sound('Audio/item1.ogg')
    wrong_answer_mp3 = pygame.mixer.Sound('Audio/negative_beeps-6008.mp3')

    while True:
        # for loop
        events_loop(operationes, levelos)
        # Game screen
        # Operations Screen
        if num == 10:
            start_the_game = False
            final_state = True
        if start_the_game:
            screen.fill(SKYBLUE)
            screen.blit(sentence_surf, sentence_rect)
            addition.draw(screen)
            substracction.draw(screen)
            multiplication.draw(screen)
            division.draw(screen)
            ops = [addition, substracction, multiplication, division]
            for op in ops:
                if op.rect.collidepoint(pygame.mouse.get_pos()):
                    op.draw(screen, RED)

            screen.blit(command_surf, command_rect)

            # Levels screen
            if choose_level:
                pygame.time.wait(300)
                screen.fill(SKYBLUE)
                screen.blit(level_surf, level_rect)
                level_1.draw(screen)
                level_2.draw(screen)
                level_3.draw(screen)
                levels = [level_1, level_2, level_3]
                for level in levels:
                    if level.rect.collidepoint(pygame.mouse.get_pos()):
                        level.draw(screen, RED)
                screen.blit(command_surf, command_rect)

            # Real Game Screen
            if start_playing:

                screen.fill(SKYBLUE)
                screen.blit(play_surface, play_surface_rect)
                screen.blit(answer_prompt_surf, answer_prompt_rect)
                screen.blit(click_surf, click_rect)

                user_rect = pygame.draw.rect(screen, BEIGE, user_rect)
                user_text_surf = text_font.render(user_answer, True, (64, 64, 64))
                user_rect.w = max(Display_Operation().rect.w, user_text_surf.get_width() + 10)
                screen.blit(user_text_surf, user_rect)

                equation = display_operation(game_algo)
                question_surf = Display_Operation(equation).operation_surf
                question_rect = Display_Operation(equation).rect
                screen.blit(question_surf, question_rect)

                while True:
                    event = pygame.event.poll()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            user_answer = user_answer.replace(user_answer[-1], ' ')

                        else:
                            user_answer += event.unicode
                        user_answer = (' ' + user_answer).rstrip()
                        user_rect = pygame.draw.rect(screen, BEIGE, user_rect)
                        user_text_surf = text_font.render(user_answer, True, (64, 64, 64))
                        user_rect.w = max(Display_Operation().rect.w, user_text_surf.get_width() + 10)
                        screen.blit(user_text_surf, user_rect)

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            if user_answer.strip().replace('-', '').isdigit():
                                x = user_answer
                                if correct_answer(equation, user_answer.strip()):
                                    score += 1
                                    right_answer_mp3.play(0)
                                else:
                                    wrong_answer_mp3.play(0)

                                user_answer = ''
                                num += 1
                                break

                    pygame.display.update()
        # Ending screen
        elif final_state:

            screen.fill(YELLOW)
            score_surf, score_rect = phrase_rect(f'Your score: {score} out of 10', 300, 100,text_font)
            screen.blit(score_surf, score_rect)
            screen.blit(restart_surf, restart_rect)
            screen.blit(mathgame_surf, mathgame_rect)
        # Starting screen
        else:
            score = 0
            screen.fill(YELLOW)
            screen.blit(little_professor_surf, little_professor_rect)
            screen.blit(title_surf, title_rect)
            screen.blit(start_message_surf, start_message_rect)

        clock.tick(60)
        pygame.display.flip()


def display_operation(details_list):
    if details_list[0] == 'Addition':
        return operations.addition(details_list[1])
    elif details_list[0] == 'Substraction':
        return operations.substraction(details_list[1])
    elif details_list[0] == 'Multiplication':
        return operations.multiplication(details_list[1])
    else:
        return operations.division(details_list[1])


def correct_answer(math_equation, answer):
    math_equation = math_equation.replace('=', '')
    num1, num2 = re.split(r'[+\-x/]', math_equation)
    if '+' in math_equation:
        return int(num1) + int(num2) == int(answer)
    elif '-' in math_equation:
        return int(num1) - int(num2) == int(answer)
    elif 'x' in math_equation:
        return int(num1) * int(num2) == int(answer)
    else:
        return int(num1) / int(num2) == int(answer)


def image_surface(image):
    return pygame.image.load(image).convert_alpha()


def image_rect(image_surf, x, y):
    return image_surf.get_rect(center=(x, y))

def phrase_rect(sentence, x, y,text_font,color=(64, 64, 64)):
    surf = text_font.render(sentence, False, color)
    rect = surf.get_rect(center=(x, y))
    return (surf, rect)

def events_loop(operations_list,levels_list):
    global start_the_game, choose_level, start_playing, user_answer, final_state, num
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if start_the_game:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:

                for op in operations_list:
                    if op.rect.collidepoint(pygame.mouse.get_pos()):
                        choose_level = True
                        game_algo.append(op.name)
            if choose_level:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:

                    for level in levels_list:
                        if level.rect.collidepoint(pygame.mouse.get_pos()):
                            start_playing = True
                            game_algo.append(level.niveau)

            if start_playing:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_answer = user_answer[:-1]

                    else:
                        user_answer += event.unicode

        elif final_state:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    num = 0
                    final_state = False
                    start_the_game = False
                    choose_level = False
                    start_playing = False


        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_the_game = True




if __name__ == '__main__':
    main()