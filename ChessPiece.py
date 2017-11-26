# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 19:02:17 2017

@author: josh
"""

class ChessPiece(object):
    def __init__(self, position, color, board, image=None):
        self._color = color
        self._position = position    # 2 element list with (x,y)
        self._image = image
        self._captured_bool = False
        self._board = board
        self._has_moved = False

    def move(self, new_location):
        legal_move_bool = self.check_legal_move(new_location)
        if legal_move_bool:
            self._position = new_location
            self.set_moved(True)

    def _check_legal_move(self, new_location):
        pass

#    def capture(self, new_location):
#        pass

    def _draw(self):
        pass

    # accessors
    def get_captured(self):
        return self._captured_bool

    # mutators
    def set_captured(self, captured_bool):
        self._captured_bool = captured_bool
        if captured_bool == True:
            self._position = None   # Captured pieces don't have a position

    def is_same_point(self, loc1, loc2):
        x1,y1 = loc1
        x2,y2 = loc2
        if x1 == x2 and y1 == y2:
            return True
        else:
            return False

    def is_straight_line(self, loc1, loc2):
        if self.is_same_point(loc1, loc2):
            raise ValueError('loc1 and loc2 are the same point')
        x1,y1 = loc1
        x2,y2 = loc2
        if x1 == x2 or y1 == y2:
            return True
        else:
            return False

    def is_diagonal(self, loc1, loc2):
        if self.is_same_point(loc1, loc2):
            raise ValueError('loc1 and loc2 are the same point')
        x1,y1 = loc1
        x2,y2 = loc2
        if x1-x2 == y1-y2:
            return True
        else:
            return False

    def get_position(self):
        return self._position

    def set_moved(self, has_moved):
        self._has_moved = has_moved
