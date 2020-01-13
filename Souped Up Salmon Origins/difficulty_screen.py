import pygame
from sprite_library import *
from gameskit.ui_elements import *
pygame.font.init()
pygame.mixer.init()
difficulty = 0


class Background:
    def __init__(self, position):
        self.position = position
        self.image = pygame.image.load("assets/images/reef.jpeg")

    def draw(self, surface):
        surface.blit(self.image, self.position)

    def render(self, brush):
        pass


class Button:
    def __init__(self, position, size, colour, hover_colour, text, difficulty, callback):
        self.position = position
        self.size = size
        self.colour = colour
        self.hover_colour = hover_colour
        self.text = text
        self.difficulty = difficulty
        self.callback = callback
        self.font = pygame.font.SysFont("comic sans", 45)
        self.hovering = False

    def draw(self, surface):
        if self.hovering:
            pygame.draw.rect(surface, self.hover_colour, (self.position[0],
                                                          self.position[1], self.size[0], self.size[1]))
        else:
            pygame.draw.rect(surface, self.colour, (self.position[0], self.position[1], self.size[0], self.size[1]))

        label = self.font.render(self.text, 30, (40, 180, 250))
        surface.blit(label, self.position)

    def is_mouse_hovering(self, mouse_x, mouse_y):
        return(self.position[0] <= mouse_x <= self.position[0] + self.size[0]
               and self.position[1] <= mouse_y <= self.position[1] + self.size[1])

    def click(self):
        self.callback()


window = pygame.display.set_mode((800, 600))
current_state = 0

play = Button((0, 100), (140, 35), (0, 150, 0), (0, 0, 0), "Too Easy", 5, None)
easy = Button((0, 150), (80, 35), (0, 250, 0), (0, 0, 0), "Easy", 10,  easy)
medium = Button((0, 200), (115, 35), (220, 255, 10), (0, 0, 0), "Medium", 20, medium)
hard = Button((0, 250), (80, 35), (220, 0, 0), (0, 0, 0), "Hard", 35, hard)
very_hard = Button((0, 300), (150, 35), (160, 0, 0), (0, 0, 0), "Very Hard", 50,  very_hard)
funny = Button((0, 350), (140, 35), (100, 0, 0), (0, 0, 0), "F U N N Y", 200, funny)


title_label = Button((0, 0), (140, 35), (0, 0, 0), (0, 0, 0), "Difficulty", 0,  None)
background = Background((0, 0))
buttons = [play, easy, medium, hard, very_hard, funny]


def dif_get_input():
    if current_state == 0:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        hovered_button = None

        for button in buttons:
            button.hovering = button.is_mouse_hovering(mouse_x, mouse_y)
            if button.hovering:
                hovered_button = button

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == pygame.BUTTON_LEFT:
                    if hovered_button:
                        hovered_button.click()


def dif_update():
    if current_state == 0:
        pass


def dif_render():
    if current_state == 0:
        background.draw(window)

        play.draw(window)

        title_label.draw(window)
    elif current_state == 1:
        window.fill((255, 255, 120))
    pygame.display.flip()


pygame.mixer.music.load('assets/music/Come_And_Get_Your_Love1.mp3')
pygame.mixer.music.play(0)
while True:
    dif_get_input()
    dif_update()
    dif_render()
    print(difficulty)

