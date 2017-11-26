# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 19:04:23 2017

@author: josh
"""
from Player import Player
from ChessPieces import *
import numpy as np

class ChessBoard(object):
    # Column locations for each piece
    PAWNS_LOC = (0,1,2,3,4,5,6,7)
    ROOKS_LOC = (0,7)
    KNIGHTS_LOC = (1,6)
    BISHOPS_LOC = (2,5)
    QUEEN_LOC = (3,)
    KING_LOC = (4,)

    X_LEN = Y_LEN = 8   # shape of the board

    def __init__(self):
        self.board = [[None for _ in range(self.Y_LEN)] for _ in range(self.X_LEN)]
        self._players = [Player(), Player()]
#        self._white_player = None
#        self._black_player = None

        self.reset_game()

    def reset_game(self):
        self._assign_colors()
        self._create_place_pieces()
        self._populate_board(self.get_white_player().get_pieces())  # place white pieces
        self._populate_board(self.get_black_player().get_pieces())  # place black pieces

    def _assign_colors(self):
        # 50% chance of player 1 being white
        if np.random.rand() >= 0.5:
            self.set_white_player(self._players[0])
            self.set_black_player(self._players[1])
        else:
            self.set_white_player(self._players[1])
            self.set_black_player(self._players[0])

    def _create_place_pieces(self):
        back_row = None
        pawn_row = None
        colors = ['white','black']
        for i, color in enumerate(colors):
            if color == 'white':
                back_row = 0
                pawn_row = 1
            else: # if color is 'black'
                back_row = 7
                pawn_row = 6

            pieces = []
            pieces = pieces + self._create_pieces(King, self.KING_LOC, back_row, color, self)
            pieces = pieces + self._create_pieces(Queen, self.QUEEN_LOC, back_row, color, self)
            pieces = pieces + self._create_pieces(Knight, self.KNIGHTS_LOC, back_row, color, self)
            pieces = pieces + self._create_pieces(Bishop, self.BISHOPS_LOC, back_row, color, self)
            pieces = pieces + self._create_pieces(Rook, self.ROOKS_LOC, back_row, color, self)
            pieces = pieces + self._create_pieces(Pawn, self.PAWNS_LOC, pawn_row, color, self)

            if color == 'white':
                p = self.get_white_player()
            else:
                p = self.get_black_player()
            p.assign_pieces(pieces)

    def _create_pieces(self, piece_class, location_list, row, color, board):
            pieces = []
            for loc in location_list:
                pieces.append(piece_class([row, loc], color, board))
            return pieces
    def castle(self):
        pass

    def _cross_check(self):
        """ check if the castle move is going to cross check """
        pass

    def _is_check(self, location, player):
        pass
        # see who's turn it is so that we only have to check one side
        # check legal move on each opponent piece to see if they can capture the king

    def _populate_board(self, chess_piece_list):
        for chess_piece in chess_piece_list:
            x,y = chess_piece._position
            self.board[x][y] = chess_piece

    def _are_squares_empty(self, list_of_locations):
        """ pass a list of locations (as lists) to this function
            and return a bool of True if all locations are empty,
            False otherwise
        """
        for location in list_of_locations:
            x,y = location
            if self.board[x][y] == None:
                continue
            else:  # if any square is not empty, return False
                return False
        return True

    def _was_piece_jumped(self, loc1, loc2):
        x1, y1 = loc1
        x2, y2 = loc2

        if x1 == x2 and y1 == y2:
            raise ValueError('loc1 and loc2 are the same point')

        x_larger = max(x1,x2)
        x_smaller = min(x1,x2) + 1  # don't count the start or finish location (non-inclusive)
        y_larger = max(y1,y2)
        y_smaller = min(y1,y2) + 1 # don't count the start or finish location (non-inclusive)
        x_list = [x for x in range(x_smaller, x_larger)]
        y_list = [y for y in range(y_smaller, y_larger)]

        if x2 == x1:
            x_list = [x1]*len(y_list)
        elif y2 == y1:
            y_list = [y1]*len(x_list)

        return not self._are_squares_empty( zip(x_list,y_list) )

    # accessors
    def get_white_player(self):
        color = 'white'
        return self._get_player(color)

    def get_black_player(self):
        color = 'black'
        return self._get_player(color)

    def _get_player(self, color):
        player_specified_color = []
        for player in self._players:
            if player.get_color() == color:
                player_specified_color.append(player)
        if len(player_specified_color) > 1:
            raise ValueError('Both players are ' + color)
        if len(player_specified_color) == 0:
            raise ValueError('Neither player is ' + color)
        else:
            return player_specified_color[0]

    # mutators
    def set_white_player(self, player):
#        self._white_player = player
        player.set_color('white')

    def set_black_player(self, player):
#        self._black_player = player
        player.set_color('black')
