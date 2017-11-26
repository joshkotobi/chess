# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 19:06:37 2017

@author: josh
"""
from ChessPiece import ChessPiece

class King(ChessPiece):
    def __init__(self, position, color, board, image=None):
        super().__init__(position=position, color=color, board=board, image=image)
        # other initializations
    def _check_legal_move(self, new_location):
        x2,y2 = new_location
        x1,y1 = self._position
        if self._castle(x1,y1,x2,y2):
            self._board.castle()
            return True
        if self._board._is_check():  # can't move into check
            return False
        
        return self._check_move_distance(x1,y1,x2,y2)
    
    def _check_move_distance(self,x1,y1,x2,y2):
        x_moved = abs(x2-x1)
        y_moved = abs(y2-y1)
        if x_moved or y_moved > 1:
            return False
        else:
            return True
                
    def _castle(self,x1,y1,x2,y2):
        if abs(x1-x2) == 2 and y1 == y2 and self._has_moved == True:
            pass
    
    def _is_check(self,x2,y2):
        self._board._is_check([x2,y2],self._color)
    
    
class Queen(ChessPiece):
    def __init__(self, position, color, board, image=None):
        super().__init__(position=position, color=color, board=board, image=image)
    def _check_legal_move(self, new_location):
        if self.is_straight_line(self.get_position(), new_location) or self.is_diagonal(self.get_position(), new_location):
            if self._board.was_piece_jumped(self.get_position(), new_location):
                return True
        return False
    

class Rook(ChessPiece):
    def __init__(self, position, color, board, image=None):
        super().__init__(position=position, color=color, board=board, image=image)
    def _check_legal_move(self, new_location):
        if self.is_straight_line(self.get_position(), new_location):
            if self._board.was_piece_jumped(self.get_position(), new_location):
                return True
        return False
        
        # check for straight movements
        # ask ChessBoard if any pieces were jumped


class Knight(ChessPiece):
    def __init__(self, position, color, board, image=None):
        super().__init__(position=position, color=color, board=board, image=image)
    def _check_legal_move(self, new_location):
        x2,y2 = new_location
        x1,y1 = self._position
        if abs(x1-x2) == 2 and abs(y1-y2) == 1:
            return True
        elif abs(x1-x2) == 1 and abs(y1-y2) == 2:
            return True
        else:
            return False


class Bishop(ChessPiece):
    def __init__(self, position, color, board, image=None):
        super().__init__(position=position, color=color, board=board, image=image)
    def _check_legal_move(self, new_location):
        if self.is_diagonal(self.get_position(), new_location):
            if self._board.was_piece_jumped(self.get_position(), new_location):
                return True
        return False


class Pawn(ChessPiece):
    def __init__(self, position, color, board, image=None):
        super().__init__(position=position, color=color, board=board, image=image)
    def _check_legal_move(self, new_location):
        pass

    