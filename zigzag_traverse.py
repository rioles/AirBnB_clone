#!/usr/bin/env python3
"""Class solution"""


class Solution(object):
    """ Class that contain algo solution """

    def zig_zag_traverse(self, matrix=[][]):
        """ method zizagging through an array and returning
        a  list containing the values

        Args:
            matrix (list[][]): The matrix given

        Return:
            list that contain all value
            """
        width = len(matrix[0]) - 1
        height = len(matrix) - 1
        row, col = 0, 0
        is_down = True
        result = []
        atr = MatrixAtribute(row, col, width, height)
        while not self.matrix_boundary(atr):
            result.append(matrix[atr.row][atr.col])
            if is_down:
                if atr.col == 0 or atr.row == atr.height:
                    is_down = False
                    if atr.row == atr.height:
                        atr.col += 1
                    else:
                        atr.row += 1
                else:
                    atr.col -= 1
                    atr.row += 1
            else:
                if atr.row == 0 or atr.col == atr.width:
                    is_down = True
                    if atr.col == atr.width:
                        atr.row += 1
                    else:
                        atr.col += 1
                else:
                    atr.row -= 1
                    atr.col += 1
        return result

    def matrix_boundary(self, atr):
        return atr.col > atr.width or atr.col < 0
        or atr.row < 0 or atr.row > atr.height


class MatrixAtribute:
    """ class that contain matrix attribute"""

    def __init__(self, row, col, width, height):
        self.row = row
        self.col = col
        self.width = width
        self.height = height
