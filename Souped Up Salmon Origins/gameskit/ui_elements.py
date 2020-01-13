"""Contains all of the user interface (UI) elements to be shown on a PyGame window."""

import os

import pygame

from gameskit.maths import *


class UIBrush:
    """The class that takes Surfaces from other UIElements and draws them on UIWindows

    :param __surface: Private - The PyGame Surface the UIBrush is linked to (all rendering the UIBrush does will appear on this Surface)
    :param __fill_colour: Private - The **fill** colour the UIBrush uses
    :param __stroke_colour: Private - The **stroke** colour the UIBrush uses
    :type __surface: pygame.Surface
    :type __fill_colour: tuple
    :type __stroke_colour: tuple
    """

    def __init__(self, surface: pygame.Surface) -> None:
        """The constructor for a UIBrush (which requires a Surface to work).

        :param surface: The PyGame Surface the brush is linked to
        :type surface: pygame.Surface
        """
        self.__surface = surface
        self.__fill_colour = (0x00, 0x00, 0x00)
        self.__stroke_colour = (0x00, 0x00, 0x00)

    def set_colour(self, fill_colour: tuple=None, stroke_colour: tuple=None) -> None:
        """Changes the colour of the UIBrush

        :param fill_colour: The fill colour to set the UIBrush to
        :param stroke_colour: The stroke colour to set the UIBrush to
        :type fill_colour: tuple
        :type stroke_colour: tuple
        """
        if fill_colour is not None:
            self.__fill_colour = fill_colour
        if stroke_colour is not None:
            self.__stroke_colour = stroke_colour

    @staticmethod
    def __scale_value(scale: float, max_value: float) -> float:
        """Checks if the scale is less than 1. If it is, it scales it up to the max_value.

        :param scale: The scale (or value) to scale up (if needed)
        :param max_value: If the scale is less than 1, this is the amount to scale up by
        :type scale: float
        :type max_value: float
        :return: The scaled up value
        :rtype: float
        """
        if 0 <= scale <= 1:
            scale *= max_value
        return scale

    @staticmethod
    def __scale_tuple(values: tuple, max_values: tuple) -> tuple:
        """Scales a tuple of floats up to another tuple of floats

        :param values: The tuple of values to scale up (if needed)
        :param max_values: The tuple of values to scale up by
        :type values: tuple
        :type max_values: tuple
        :return: The scaled up tuple
        :rtype: tuple
        """
        value1 = UIBrush.__scale_value(values[0], max_values[0])
        value2 = UIBrush.__scale_value(values[1], max_values[1])
        return value1, value2

    def draw_rect(self, origin: tuple, size: tuple, stroke_thickness: int=0, scaled_mode: bool=False) -> None:
        """Draws a rectangle at the specified origin (with the specified size) on the UIBrush's Surface.

        :param origin: The centre of the rectangle
        :param size: The size of the rectangle
        :param stroke_thickness: The size of the **stroke** of the rectangle
        :param scaled_mode: States whether or not to **scale** the origin/size
        :type origin: tuple
        :type size: tuple
        :type stroke_thickness: int
        :type scaled_mode: bool
        """
        if scaled_mode:
            origin_x, origin_y = UIBrush.__scale_tuple(origin, self.__surface.get_size())
            size_x, size_y = UIBrush.__scale_tuple(size, self.__surface.get_size())
        else:
            origin_x, origin_y = origin
            size_x, size_y = size
        origin_x -= size_x / 2
        origin_y -= size_y / 2
        origin_x = int(origin_x)
        origin_y = int(origin_y)
        size_x = int(size_x)
        size_y = int(size_y)
        pygame.draw.rect(self.__surface, self.__fill_colour, pygame.Rect(origin_x, origin_y, size_x, size_y))
        if stroke_thickness > 0:
            pygame.draw.rect(self.__surface, self.__stroke_colour, pygame.Rect(origin_x, origin_y, size_x, size_y), stroke_thickness)

    def draw_oval(self, origin: tuple, size: tuple, stroke_thickness: int=0, scaled_mode: bool=False) -> None:
        """Draws an oval at the specified origin (with the specified size) on the UIBrush's Surface.

        :param origin: The centre of the oval
        :param size: The size of the oval
        :param stroke_thickness: The size of the **stroke** of the oval
        :param scaled_mode: Whether to draw based on *parent* size (0 <= x <= 1) or on *pixel* size
        :type origin: tuple
        :type size: tuple
        :type stroke_thickness: int
        :type scaled_mode: bool
        """
        if scaled_mode:
            origin_x, origin_y = UIBrush.__scale_tuple(origin, self.__surface.get_size())
            size_x, size_y = UIBrush.__scale_tuple(size, self.__surface.get_size())
        else:
            origin_x, origin_y = origin
            size_x, size_y = size
        origin_x -= size_x / 2
        origin_y -= size_y / 2
        origin_x = int(origin_x)
        origin_y = int(origin_y)
        size_x = int(size_x)
        size_y = int(size_y)
        pygame.draw.ellipse(self.__surface, self.__fill_colour, pygame.Rect(origin_x, origin_y, size_x, size_y), stroke_thickness)

    def draw_image(self, origin: tuple, size: tuple, image: pygame.Surface,  scaled_mode: bool=False) -> None:
        """Draws an image (any **Surface** in PyGame) at the specified origin (with the specified size) on the UIBrush's Surface.

        :param origin: The centre of the image
        :param size: The size of the image
        :param image: The image to draw
        :param scaled_mode: Whether
        :type origin: tuple
        :type size: tuple
        :type image: pygame.Surface
        :type scaled_mode: bool
        """
        if scaled_mode:
            origin_x, origin_y = UIBrush.__scale_tuple(origin, self.__surface.get_size())
            size_x, size_y = UIBrush.__scale_tuple(size, self.__surface.get_size())
        else:
            origin_x, origin_y = origin
            size_x, size_y = size
        origin_x -= size_x / 2
        origin_y -= size_y / 2
        origin_x = int(origin_x)
        origin_y = int(origin_y)
        size_x = int(size_x)
        size_y = int(size_y)
        scaled_surface = pygame.transform.scale(image, (size_x, size_y))
        self.__surface.blit(scaled_surface, (origin_x, origin_y))


class UIWindow:
    """The window class that manages all PyGame window activities (and is what
    renders all UIElements).

    :param __window_size: Private - The size of the window (can be adjusted by functions)
    :param __window: Private - The PyGame display (that renders all UIElements)
    :param __brush: Private - The UIBrush used to render all UIElements onto this window
    :param __background_colour: Private - The colour to use as the window's background
    :param __frame_rate: Private - The number of updates/renders to perform every second
    :param __clock: Private - A PyGame Clock used to limit framerate
    :type __window_size: Vector
    :type __window: pygame.Surface
    :type __brush: UIBrush
    :type __background_colour: tuple
    :type __frame_rate: int
    :type __clock: pygame.time.Clock
    """

    def __init__(self, size: Vector, title: str, background_colour: tuple=(0x00, 0x00, 0x00), frame_rate: int=60) -> None:
        """Creates a UIWindow (given a size and title).

        :param size: The size (**width** and **height**) of the window
        :param title: The caption of the window (shown in the bar at the top of the window)
        :param background_colour: The colour to use for the window (also acts as its **clear colour**)
        :param frame_rate: The frame rate to use for the window (defaults to **60**)
        :type size: Vector
        :type title: str
        :type background_colour: tuple
        :type frame_rate: int
        """
        pygame.init()
        self.__window_size = Vector(size.x, size.y)
        self.__window = pygame.display.set_mode(self.__window_size.to_tuple())
        pygame.display.set_caption(title)
        self.__brush = UIBrush(self.__window)
        self.__background_colour = background_colour
        self.__frame_rate = frame_rate
        self.__clock = pygame.time.Clock()

    def wait(self) -> int:
        """Tells the window to wait the allotted time (based on the frame rate).

        :return: The number of **milliseconds** since the previous update
        :rtype: int
        """
        return self.__clock.tick(self.__frame_rate)

    def get_brush(self) -> UIBrush:
        """Returns the UIBrush linked to this window.

        :return: The UIBrush for this window
        :rtype: UIBrush
        """
        return self.__brush

    def show_frame(self) -> None:
        """Switches to a new Surface (which can be rendered on to beforehand) - uses double-buffering."""
        try:
            image = pygame.image.load(os.path.dirname(__file__) + '\images\\funtech_logo.png')
            self.__brush.draw_image((0.08, 0.87), (0.1, 0.2), image, scaled_mode=True)
        except pygame.error:
            pass
        pygame.display.flip()

    def clear(self) -> None:
        """Clears the Surface attached to this window (using the __background_colour value)."""
        self.__window.fill(self.__background_colour)


class UIElement:
    """An object (using PyGame) that can be rendered on a UIScreen

    This class acts as an **abstract** class, with its main function (used for rendering on a UIScreen
    via a UIBrush) throwing an exception if it is used directly.

    :param _position: Protected - The position of the UIElement (with the origin at its **centre**
    :param _size: Protected - The size of the UIElement - can be given in **pixels** or as a **percentage** of parent's size
    :param _surface: Protected - The PyGame Surface that the UIElement uses
    :type _position: Vector
    :type _size: Vector
    :type _surface: pygame.Surface
    """

    def __init__(self, position: Vector, size: Vector) -> None:
        """The constructor for a UIElement (run whenever a **child class** is instantiated).

        :param position: The position of the UIElement
        :param size: The size of the UIElement
        :type position: Vector
        :type size: Vector
        """
        self._position = position
        self._size = size
        self._surface = pygame.Surface(size.to_tuple(), pygame.SRCALPHA, 32)

    def render(self, brush: UIBrush) -> None:
        """Draws the UIElement onto the UIBrush's Surface.

        :param brush: The brush to draw this UIElement with
        :type brush: UIBrush
        """
        brush.draw_image(self._position.to_tuple(), self._size.to_tuple(), self._surface)

    def update(self, delta_time: float) -> None:
        """Updates the UIElement (base UIElement has no logic, while sub-classes can perform different actions in this function).

        :param delta_time: The amount of time elapsed since the previous update
        :type: delta_time: float
        """
        pass
