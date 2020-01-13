from gameskit.ui_elements import *

pygame.font.init()


class HUDLabel(UIElement):
    def update_appearance(self):
        brush = UIBrush(self._surface)
        self._surface.fill((0, 0, 0))
        font_surface = self.__font.render(self.__text, 1, self.__font_colour)
        brush.draw_image((0.5, 0.5), (1, 1), font_surface, scaled_mode=True)

    def __init__(self, position, size, text, font, font_colour):
        UIElement.__init__(self, position, size)
        self.__text = text
        self.__font = font
        self.__font_colour = font_colour
        self.update_appearance()

    def set_text(self, text):
        self.__text = text
