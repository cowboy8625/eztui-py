import unittest
import clitui


class TestDisplayFunctions(unittest.TestCase):
    def test_is_pressed(self):
        self.assertEqual(clitui.is_pressed("UP", "\x1b[A"), True)
        self.assertEqual(clitui.is_pressed("DOWN", "\x1b[B"), True)
        self.assertEqual(clitui.is_pressed("RIGHT", "\x1b[C"), True)
        self.assertEqual(clitui.is_pressed("LEFT", "\x1b[D"), True)
        self.assertEqual(clitui.is_pressed("ESC", "\x1b"), True)
        self.assertEqual(clitui.is_pressed("ENTER", "\n"), True)
        self.assertEqual(clitui.is_pressed("TAB", "\t"), True)
        self.assertEqual(clitui.is_pressed("BAR", " "), True)
        self.assertEqual(clitui.is_pressed("Fail", "Fail"), True)
        self.assertEqual(clitui.is_pressed("Key", "Fail"), False)

    def test_boarder_char_h(self):
        self.assertEqual(clitui.display.boarder_char("h", style=0), chr(9552))
        self.assertEqual(clitui.display.boarder_char("h", style=1), chr(9472))
        self.assertEqual(clitui.display.boarder_char("h", style=2), chr(9473))

    def test_boarder_char_v(self):
        self.assertEqual(clitui.display.boarder_char("v", style=0), chr(9553))
        self.assertEqual(clitui.display.boarder_char("v", style=1), chr(9474))
        self.assertEqual(clitui.display.boarder_char("v", style=2), chr(9475))

    def test_boarder_char_lt(self):
        self.assertEqual(clitui.display.boarder_char("lt", style=0), chr(9571))
        self.assertEqual(clitui.display.boarder_char("lt", style=1), chr(9508))
        self.assertEqual(clitui.display.boarder_char("lt", style=2), chr(9515))

    def test_boarder_char_rt(self):
        self.assertEqual(clitui.display.boarder_char("rt", style=0), chr(9568))
        self.assertEqual(clitui.display.boarder_char("rt", style=1), chr(9500))
        self.assertEqual(clitui.display.boarder_char("rt", style=2), chr(9507))

    def test_boarder_char_tt(self):
        self.assertEqual(clitui.display.boarder_char("tt", style=0), chr(9574))
        self.assertEqual(clitui.display.boarder_char("tt", style=1), chr(9516))
        self.assertEqual(clitui.display.boarder_char("tt", style=2), chr(9523))

    def test_boarder_char_bt(self):
        self.assertEqual(clitui.display.boarder_char("bt", style=0), chr(9577))
        self.assertEqual(clitui.display.boarder_char("bt", style=1), chr(9524))
        self.assertEqual(clitui.display.boarder_char("bt", style=2), chr(9531))

    def test_boarder_char_tlc(self):
        self.assertEqual(clitui.display.boarder_char("tlc", style=0), chr(9556))
        self.assertEqual(clitui.display.boarder_char("tlc", style=1), chr(9581))
        self.assertEqual(clitui.display.boarder_char("tlc", style=2), chr(9487))

    def test_boarder_char_trc(self):
        self.assertEqual(clitui.display.boarder_char("trc", style=0), chr(9559))
        self.assertEqual(clitui.display.boarder_char("trc", style=1), chr(9582))
        self.assertEqual(clitui.display.boarder_char("trc", style=2), chr(9491))

    def test_boarder_char_blc(self):
        self.assertEqual(clitui.display.boarder_char("blc", style=0), chr(9562))
        self.assertEqual(clitui.display.boarder_char("blc", style=1), chr(9584))
        self.assertEqual(clitui.display.boarder_char("blc", style=2), chr(9495))

    def test_boarder_char_brc(self):
        self.assertEqual(clitui.display.boarder_char("brc", style=0), chr(9565))
        self.assertEqual(clitui.display.boarder_char("brc", style=1), chr(9583))
        self.assertEqual(clitui.display.boarder_char("brc", style=2), chr(9499))

    def test_boarder_char_ls(self):
        self.assertEqual(clitui.display.boarder_char("ls", style=0), "/")
        self.assertEqual(clitui.display.boarder_char("ls", style=1), "/")
        self.assertEqual(clitui.display.boarder_char("ls", style=2), "/")

    def test_boarder_char_rs(self):
        self.assertEqual(clitui.display.boarder_char("rs", style=0), "\\")
        self.assertEqual(clitui.display.boarder_char("rs", style=1), "\\")
        self.assertEqual(clitui.display.boarder_char("rs", style=2), "\\")

    def test_boarder_char_plus(self):
        self.assertEqual(clitui.display.boarder_char("+", style=0), chr(9580))
        self.assertEqual(clitui.display.boarder_char("+", style=1), chr(9532))
        self.assertEqual(clitui.display.boarder_char("+", style=2), chr(9547))

    def test_gen_points(self):
        points = clitui.display.gen_points(0, 0, 5, 0,)
        self.assertEqual(
            tuple(points), ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)),
        )

    def test_cirlce_points(self):
        points = set(clitui.display._create_points(10, 10, 3, 1, 360))
        self.assertEqual(
            tuple(points),
            (
                (12, 7),
                (12, 13),
                (8, 12),
                (13, 11),
                (13, 8),
                (7, 10),
                (12, 12),
                (9, 7),
                (8, 8),
                (11, 7),
                (9, 13),
                (11, 13),
                (13, 10),
                (7, 9),
                (7, 12),
                (12, 8),
                (8, 7),
                (10, 7),
                (10, 13),
                (8, 13),
                (13, 9),
                (13, 12),
                (7, 11),
                (7, 8),
            ),
        )


if __name__ == "__main__":
    unittest.main()
