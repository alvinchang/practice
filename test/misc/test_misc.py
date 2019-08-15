import unittest

from misc.print_matrix_spiral import matrix_spiral


class TestMatrixSpiral(unittest.TestCase):

    def test_basic_matrix_empty(self):
        matrix = [[]]

        spiral_path = matrix_spiral(matrix)
        expected_path = []
        self.assertEqual(spiral_path, expected_path)

    def test_basic_matrix_spiral_1x1(self):
        matrix = [[1]]

        spiral_path = matrix_spiral(matrix)
        expected_path = [1]
        self.assertEqual(spiral_path, expected_path)

    def test_basic_matrix_spiral_2x2(self):
        matrix = [
            [1, 2],
            [3, 4]
        ]

        spiral_path = matrix_spiral(matrix)
        expected_path = [1, 2, 4, 3]
        self.assertEqual(spiral_path, expected_path)

    def test_basic_matrix_spiral_3x3(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        spiral_path = matrix_spiral(matrix)
        expected_path = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(spiral_path, expected_path)

    def test_basic_matrix_spiral_4x4(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]

        spiral_path = matrix_spiral(matrix)
        expected_path = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
        self.assertEqual(spiral_path, expected_path)

    def test_basic_matrix_spiral_2x4(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]

        spiral_path = matrix_spiral(matrix)
        expected_path = [1, 2, 3, 4, 8, 7, 6, 5]
        self.assertEqual(spiral_path, expected_path)

    def test_basic_matrix_spiral_4x2(self):
        matrix = [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8]
        ]

        spiral_path = matrix_spiral(matrix)
        expected_path = [1, 2, 4, 6, 8, 7, 5, 3]
        self.assertEqual(spiral_path, expected_path)
