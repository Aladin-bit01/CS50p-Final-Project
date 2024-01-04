import pygame
from sys import exit
import operations

text_font = pygame.font.Font('font/Pixeltype.ttf', 50)
def image_surface(image):
    return pygame.image.load(image).convert_alpha()

def image_rect(image_surf, x, y):
    return image_surf.get_rect(center=(x, y))

def phrase_rect(sentence, x, y, color=(64, 64, 64)):
    global text_font
    surf = text_font.render(sentence, False, color)
    rect = surf.get_rect(center=(x, y))
    return (surf, rect)



# Constants
LIGHT_BLUE = (152, 195, 195)



class Operations:
    def __init__(self, x, y, operation, name):
        self.font = pygame.font.Font('font/Pixeltype.ttf', 60)
        self.surface = self.font.render(operation, False, (64, 64, 64))
        self.rect = self.surface.get_rect(center=(x, y))
        self.name = name

    def draw(self, color=(210, 190, 150)):
        pygame.draw.circle(screen, color, self.rect.center, 50)
        screen.blit(self.surface, self.rect)


class Levels:
    def __init__(self, x, y, niveau, name):
        self.font = pygame.font.Font('font/Pixeltype.ttf', 60)
        self.surface = self.font.render(name, False, (64, 64, 64))
        self.rect = self.surface.get_rect(center=(x, y))
        self.niveau = niveau
        self.name = name

    def draw(self, color=(210, 190, 150)):
        pygame.draw.circle(screen, color, self.rect.center, 50)
        screen.blit(self.surface, self.rect)


class DisplayOperation:
    def __init__(self, operation=None):
        self.font = pygame.font.Font('font/Pixeltype.ttf', 40)
        self.operation_surf = self.font.render(f'{operation}', False, (64, 64, 64))
        self.rect = self.operation_surf.get_rect(topleft=(50, 150))
        self.rect.h += 5

    def draw(self):
        self.rect = pygame.draw.rect(screen, (210, 190, 150), self.rect)
        self.rect = pygame.draw.rect(screen, (210, 190, 150), self.rect, 10)
        screen.blit(self.operation_surf, self.rect)


class Game:
    def __init__(self):
        self.start_the_game = False
        self.choose_level = False
        self.start_playing = False
        self.active_text_box = False
        self.ready = False

        # Game elements
        self.game_algo = []
        self.user_answer = ''
        self.user_rect = DisplayOperation().rect

    def handle_space_key(self):
        global addition, substraction, multiplication, division, choose_level, game_algo, level_1, level_2, level_3
        operationes = [addition, substraction, multiplication, division]
        for op in operationes:
            if op.rect.collidepoint(pygame.mouse.get_pos()):
                self.choose_level = True
                self.game_algo.append(op.name)

        if self.choose_level:
            levelos = [level_1, level_2, level_3]
            for level in levelos:
                if level.rect.collidepoint(pygame.mouse.get_pos()):
                    self.start_playing = True
                    self.game_algo.append(level.niveau)

    def handle_playing_events(self, event):
        global active_text_box, user_answer, ready
        if event.type == pygame.MOUSEBUTTONDOWN and self.user_rect.collidepoint(event.pos):
            self.active_text_box = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.ready = True

            if event.key == pygame.K_SPACE:
                self.user_answer += ' '
            elif event.key == pygame.K_BACKSPACE and self.user_answer != '':
                self.user_answer = self.user_answer[:-1]
            elif event.key == pygame.K_BACKSPACE and self.user_answer == '':
                self.user_answer = ''
            else:
                self.user_answer += event.unicode


def events_loop(game):
    global LIGHT_BLUE
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game.start_the_game:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game.handle_space_key()

            if game.start_playing:
                game.handle_playing_events(event)

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game.start_the_game = True


def update(game):
    global LIGHT_BLUE
    if game.ready:
        # Your logic for checking the answer and updating the game state
        pass


def render(game):
    global LIGHT_BLUE, sentence_surf, sentence_rect, addition, substraction, multiplication, division, command_surf, command_rect, command1_surf, command1_rect, level_surf, level_rect, level_1, level_2, level_3, user_rect, user_answer, active_text_box, ready
    if game.start_the_game:
        render_operations_screen()
        if game.choose_level:
            pygame.time.wait(300)
            render_levels_screen()
    else:
        render_start_screen()


def render_operations_screen():
    global LIGHT_BLUE, sentence_surf, sentence_rect, addition, substraction, multiplication, division, command_surf, command_rect, command1_surf, command1_rect
    screen.fill(LIGHT_BLUE)
    screen.blit(sentence_surf, sentence_rect)
    addition.draw()
    substraction.draw()
    multiplication.draw()
    division.draw()
    screen.blit(command_surf, command_rect)
    screen.blit(command1_surf, command1_rect)


def render_levels_screen():
    global LIGHT_BLUE, level_surf, level_rect, level_1, level_2, level_3, command_surf, command_rect, command1_surf, command1_rect
    screen.fill(LIGHT_BLUE)
    screen.blit(level_surf, level_rect)
    level_1.draw()
    level_2.draw()
    level_3.draw()
    screen.blit(command_surf, command_rect)
    screen.blit(command1_surf, command1_rect)


def render_start_screen():
    global little_professor_surf, little_professor_rect, title_surf, title_rect, start_message_surf, start_message_rect
    screen.fill((255, 255, 204))
    screen.blit(little_professor_surf, little_professor_rect)
    screen.blit(title_surf, title_rect)
    screen.blit(start_message_surf, start_message_rect)


def main():
    global LIGHT_BLUE
    pygame.init()
    global screen
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('Little Professor')
    clock = pygame.time.Clock()

    global little_professor_surf, little_professor_rect, title_surf, title_rect, start_message_surf, start_message_rect, sentence_surf, sentence_rect, addition, substraction, multiplication, division, command_surf, command_rect, command1_surf, command1_rect, level_surf, level_rect, level_1, level_2, level_3, user_rect, user_answer

    little_professor_surf = image_surface('Graphics/start_screen_little_professo.png')
    little_professor_surf = pygame.transform.smoothscale(little_professor_surf, (int(little_professor_surf.get_width() * 0.4), int(little_professor_surf.get_height() * 0.4)))
    little_professor_rect = image_rect(little_professor_surf, 300, 200)

    text_font = pygame.font.Font('font/Pixeltype.ttf', 50)
    title_surf, title_rect = phrase_rect('Little Professor', 300, 60)
    start_message_surf, start_message_rect = phrase_rect('Press space to start', 300, 350)

    sentence_surf, sentence_rect = phrase_rect('Choose a Mathematical Operation: ', 300, 50)

    addition = Operations(80, 200, '+', 'Addition')
    substraction = Operations(230, 200, '-', 'Substraction')
    multiplication = Operations(380, 200, 'x', 'Multiplication')
    division = Operations(530, 200, '/', 'Division')

    command_surf, command_rect = phrase_rect('Put your mouse on the operation', 300, 300)
    command1_surf, command1_rect = phrase_rect('and press space ', 300, 330)

    level_surf, level_rect = phrase_rect('Select a level: ', 300, 50)
    level_1 = Levels(150, 200, 1, '1')
    level_2 = Levels(300, 200, 2, '2')
    level_3 = Levels(450, 200, 3, '3')

    game = Game()

    while True:
        events_loop(game)
        update(game)
        render(game)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

