#!/usr/bin/env python
try:
    import sys
    from pygame_cards import card_sprite
except ImportError as err:
    print "Fail loading a module: %s", err
    sys.exit(2)


class Card:
    """ This class represents a card. """

    def __init__(self, suit, rank, pos, back_up = False):
        self.suit = suit
        self.rank = rank
        self.sprite = card_sprite.CardSprite(suit, rank, pos, back_up)
        #self.back_sprite = card_sprite.CardBackSprite(pos)
        self.back_up = back_up

    def get_sprite(self):
        """ Returns card's spite object
        :return: card's sprite object
        """
        return self.sprite

    # def get_back_sprite(self):
    #     return self.back_sprite

    def render(self, screen):
        """ Renders the card's sprite on a screen passed in argument
        :param screen: screen to render the card's sprite on
        """
        self.sprite.render(screen)

    def flip(self):
        """ Flips the card from face-up to face-down and vice versa """
        self.back_up = not self.back_up
        self.sprite.flip()

    def check_mouse(self, pos, down):
        """ Checks if mouse event affects the card and if so processes the event.
        :param pos: tuple with coordinates of mouse event (x, y)
        :param down: boolean, should be True for mouse down event, False for mouse up event
        :return: True if passed mouse event affects the card, False otherwise.
        """
        return self.sprite.check_mouse(pos, down)

    def check_collide(self, card):
        """ Checks if current card's sprite collides with other card's sprite
        :param card: Card object to check collision with
        :return: True if cards collide, False otherwise
        """
        return self.sprite.check_collide(card.sprite)

    def set_pos(self, pos):
        """ Sets position of the card's sprite
        :param pos: tuple with coordinates (x, y) where the top left corner of the card should be placed
        :return:
        """
        self.sprite.pos = pos
        #self.back_sprite.set_pos(pos)

    def offset_pos(self, pos):
        """ Move the card's position by the specified offset
        :param pos: tuple with coordinates (x, y) of the offset to move card
        """
        self.sprite.offset_pos(pos)
        #self.back_sprite.offset_pos(pos)
