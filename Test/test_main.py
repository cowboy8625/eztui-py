import unittest
import env
from terminalapp.__main__ import Grid, Frame, Square


class TestMain(unittest.TestCase):
    def setUp(self):
        self.instance = Grid(char="#")

    def test_construction(self):
        self.assertEqual(
            self.instance._grid, ["#####", "#####", "#####", "#####", "#####"]
        )

    def test_parse(self):
        self.instance.grid_parse()
        self.assertEqual(
            self.instance._grid,
            [
                ["#", "#", "#", "#", "#"],
                ["#", "#", "#", "#", "#"],
                ["#", "#", "#", "#", "#"],
                ["#", "#", "#", "#", "#"],
                ["#", "#", "#", "#", "#"],
            ],
        )

    def test_list_to_box(self):
        # change name to list_to_box
        self.instance.grid_list_to_string()
        self.assertEqual(
            self.instance._grid, ["#####", "#####", "#####", "#####", "#####"]
        )

    def test_grid_clear(self):
        self.instance._grid = "This better not show up"
        self.instance.grid_clear()
        self.assertEqual(
            self.instance._grid, ["#####", "#####", "#####", "#####", "#####"]
        )

    def test_grid_get_index(self):
        index = self.instance.grid_get_index()
        self.assertEqual(
            index,
            [
                [0, 1, 2, 3, 4],
                [5, 6, 7, 8, 9],
                [10, 11, 12, 13, 14],
                [15, 16, 17, 18, 19],
                [20, 21, 22, 23, 24],
            ],
        )


class TestFrame(unittest.TestCase):
    def setUp(self):
        self.frame = Frame(char="#")

    def test_frame_grid(self):
        self.assertEqual(
            self.frame._grid, ["╔═══╗", "║###║", "║###║", "║###║", "╚═══╝"]
        )

    def test_clear_frame(self):
        # Changing back ground to 0
        self.frame.char = "0"
        # Back ground still in gird as #
        self.assertNotEqual(
            self.frame._grid, ["╔═══╗", "║000║", "║000║", "║000║", "╚═══╝"]
        )
        # clear resets or rebuild a blank screen/canvas
        self.frame.clear()
        self.assertEqual(
            self.frame._grid, ["╔═══╗", "║000║", "║000║", "║000║", "╚═══╝"]
        )


class TestShape(unittest.TestCase):
    def setUp(self):
        self.root = Frame(cols=10, rows=10, char="#")
        self.square = Square(self.root, char="0")

    def test_root(self):
        self.assertEqual(
            self.root._grid,
            [
                "╔════════╗",
                "║########║",
                "║########║",
                "║########║",
                "║########║",
                "║########║",
                "║########║",
                "║########║",
                "║########║",
                "╚════════╝",
            ],
        )

    def test_square_construction(self):
        self.assertEqual(
            self.square._grid,
            [
                "000000000000",
                "000000000000",
                "000000000000",
                "000000000000",
                "000000000000",
            ],
        )

    def test_square_pack(self):
        self.square.pack()
        self.assertEqual(
            self.square._grid,
            [
                "╔══════════╗",
                "║0000000000║",
                "║0000000000║",
                "║0000000000║",
                "╚══════════╝",
            ],
        )

    def test_square_grid_size(self):
        self.assertEqual(self.square.size.x, int(5 * 2.5))
        self.assertEqual(self.square.size.y, 5)

    def test_square_on_root(self):
        self.assertEqual(self.root._grid, "[0000]")


if __name__ == "__main__":
    unittest.main()
