import pygame
from sys import exit
import operations
import re

#Constants
SKYBLUE= (152, 195, 195)
BEIGE= (210, 190, 150)
YELLOW= (255,255,204)
KEYBOARD_NUMBERS= [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
#Globals
start_the_game = False
choose_level = False
start_playing = False
#active_text_box= True
ready = False
user_answer = ''




class Operations:
    def __init__(self, x, y, operation,name):
        font= pygame.font.Font('font/Pixeltype.ttf', 60)
        self.surface  = font.render(operation, False, (64, 64, 64))
        self.rect = self.surface.get_rect(center=(x,y))
        self.name= name

    def draw(self, color= BEIGE):
        pygame.draw.circle(screen,color,self.rect.center,50)
        screen.blit(self.surface,self.rect)
class Levels:
    def __init__(self, x, y, niveau, name):
        font = pygame.font.Font('font/Pixeltype.ttf', 60)
        self.surface = font.render(name, False, (64, 64, 64))
        self.rect = self.surface.get_rect(center=(x, y))
        self.niveau = niveau
        self.name= name
    def draw(self, color=BEIGE):
        pygame.draw.circle(screen, color, self.rect.center, 50)
        screen.blit(self.surface, self.rect)

class Display_Operation:
    def __init__(self,operation= None):
        font = pygame.font.Font('font/Pixeltype.ttf', 40)
        self.operation_surf = font.render(f'{operation}', False ,(64,64,64))
        self.rect= self.operation_surf.get_rect(topleft= (50,150))
        self.rect.h += 5

    def draw(self):
        self.rect= pygame.draw.rect(screen,BEIGE, self.rect)
        self.rect = pygame.draw.rect(screen, BEIGE, self.rect, 10)
        screen.blit(self.operation_surf,self.rect)




def correct_answer(math_equation):
    math_equation= math_equation.replace('=', '')
    num1, num2= re.split(r'[+\-x/]', math_equation)
    if '+' in math_equation:
        return int(num1) + int(num2) == int (user_answer)
    elif '-' in math_equation:
        return int(num1) - int(num2) == int(user_answer)
    elif 'x' in math_equation:
        return int(num1) * int(num2) == int(user_answer)
    else:
        return int(num1) / int(num2) == int(user_answer)

def events_loop():
    global start_the_game, choose_level,start_playing,user_answer, active_text_box, ready
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if start_the_game:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                operationes = [addition, substracction, multiplication, division]
                for op in operationes:
                    if op.rect.collidepoint(pygame.mouse.get_pos()):
                        choose_level= True
                        game_algo.append(op.name)
                if choose_level:
                    levelos= [level_1, level_2,level_3]
                    for level in levelos:
                        if level.rect.collidepoint(pygame.mouse.get_pos()):
                            start_playing= True
                            game_algo.append(level.niveau)

            if start_playing:
                #INPUT BOX COLOR
                #if event.type == pygame.MOUSEBUTTONDOWN and user_rect.collidepoint(event.pos):
                #    active_text_box= True
                #Handling the Input
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        ready = True
                if ready:
                    if user_rect.collidepoint(pygame.mouse.get_pos()):
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                user_answer += ' '
                            elif event.key == pygame.K_BACKSPACE and user_answer != '':
                                user_answer= user_answer.replace(user_answer[-1], '')
                            elif event.key == pygame.K_BACKSPACE and user_answer == '':
                                user_answer = ''
                            else:
                                if event.key in KEYBOARD_NUMBERS:
                                    user_answer += event.unicode

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_the_game= True
def display_operation(details_list):
    if details_list[0] == 'Addition':
        return operations.addition(details_list[1])
    elif details_list[0] == 'Substraction':
        return operations.substraction(details_list[1])
    elif details_list[0] == 'Multiplication':
        return operations.multiplication(details_list[1])
    else:
        return operations.division(details_list[1])



def image_surface(image):
    return pygame.image.load(image).convert_alpha()
def image_rect(image_surf,x,y):
    return image_surf.get_rect(center= (x,y))

def phrase_rect(sentence,x,y, color= (64,64,64)):
    global text_font
    surf= text_font.render(sentence, False, color)
    rect= surf.get_rect(center= (x,y))
    return (surf,rect)



pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption('Little Professor')
clock= pygame.time.Clock()




#Images
little_professor_surf= image_surface('Graphics/start_screen_little_professo.png')
little_professor_surf= pygame.transform.smoothscale_by(little_professor_surf,0.4)
little_professor_rect= image_rect(little_professor_surf,300,200)

#Font
text_font= pygame.font.Font('font/Pixeltype.ttf', 50)
#Game title
title_surf, title_rect= phrase_rect('Little Professor',300,60)
#start message
start_message_surf, start_message_rect = phrase_rect('Press space to start', 300, 350)

#Operations
sentence_surf, sentence_rect = phrase_rect('Choose a Mathematical Operation: ', 300, 50)

addition= Operations(80,200, '+', 'Addition')
substracction= Operations(230,200, '-', 'Substraction')
multiplication= Operations(380,200, 'x', 'Multiplication')
division= Operations(530,200, '/', 'Division')

command_surf, command_rect = phrase_rect('Put your mouse on the operation', 300,300)
command1_surf,command1_rect = phrase_rect('and press space ', 300,330)

#Levels:
level_surf, level_rect= phrase_rect('Select a level: ', 300,50)
level_1= Levels(150,200, 1, '1')
level_2= Levels(300,200, 2, '2')
level_3= Levels(450,200, 3, '3')

#Operation to use in game
game_algo= []



#Game In Playing
play_surface= text_font.render('Let\'s Play !', False, (64,64,64))
play_surface_rect= play_surface.get_rect(topleft= (50,50))
user_rect= Display_Operation().rect
user_rect.x = 180
user_rect.y = 200
user_rect.h= Display_Operation().rect.h + 5
answer_prompt_surf= text_font.render('Answer: ', False, (64,64,64))
answer_prompt_rect= answer_prompt_surf.get_rect(topleft= (50,200))

click_surf, click_rect= phrase_rect('Click Enter twice to start ', 230, 150)






num = 0
while True:
    #for loop
    events_loop()
#Game screen
    #Operations Screen
    if num == 10:
        print('Done')
        pygame.quit()
        exit()
    if start_the_game:
        screen.fill(SKYBLUE)
        screen.blit(sentence_surf,sentence_rect)
        addition.draw()
        substracction.draw()
        multiplication.draw()
        division.draw()
        screen.blit(command_surf,command_rect)
        screen.blit(command1_surf, command1_rect)
        #Levels screen
        if choose_level:
            pygame.time.wait(300)
            screen.fill(SKYBLUE)
            screen.blit(level_surf,level_rect)
            level_1.draw()
            level_2.draw()
            level_3.draw()
            screen.blit(command_surf, command_rect)
            screen.blit(command1_surf, command1_rect)
        #Real Game Screen
        if start_playing:
            screen.fill(SKYBLUE)
            screen.blit(play_surface, play_surface_rect)
            screen.blit(answer_prompt_surf, answer_prompt_rect)

            #pygame.draw.rect(screen, BEIGE, user_rect)
            #if active_text_box:
            user_rect= pygame.draw.rect(screen, '#B85067', user_rect)
            user_text_surf = text_font.render(user_answer, True, (64, 64, 64))
            user_rect.w = max(Display_Operation().rect.w, user_text_surf.get_width() + 10)
            screen.blit(user_text_surf, (user_rect.x + 5, user_rect.y + 5))

            if ready:
                equation= display_operation(game_algo)
                question_surf = Display_Operation(equation).operation_surf
                question_rect = Display_Operation(equation).rect
                screen.blit(question_surf, question_rect)

                while True:
                    event = pygame.event.wait()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB and num == 0:
                        num += 1
                        break
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    #if event.type == pygame.MOUSEBUTTONDOWN and user_rect.collidepoint(event.pos) and len(user_answer) > 1:
                    #    active_text_box = True

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        user_answer = ''
                        num += 1
                        break  # Exit the inner loop when the user presses enter

            else:
                screen.blit(click_surf, click_rect)


    #Starting screen
    else:
        screen.fill(YELLOW)
        screen.blit(little_professor_surf,little_professor_rect)
        screen.blit(title_surf,title_rect)
        screen.blit(start_message_surf,start_message_rect)



    clock.tick(60)
    pygame.display.flip()

