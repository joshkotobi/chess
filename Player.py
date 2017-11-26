# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 20:56:23 2017

@author: josh
"""

class Player(object):
    def __init__(self):
        pass
        self._selected_piece = None
        self._color = None
        self._turn = False
        self._pieces = None
        
    def reset_game(self):
        pass    
    
    def select_piece(self, location):
        pass
        # return the piece        
        
    def assign_pieces(self, list_of_pieces):
        self._pieces = list_of_pieces
        
        
    # accessors
    def get_color(self):
        return self._color

    def get_turn(self):
        return self._turn

    def get_pieces(self):
        return self._pieces

    # mutators
    def set_color(self, color):
        self._color = color        
        
    def set_turn(self, turn_bool):
        self._turn = turn_bool
        
        