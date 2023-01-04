"""
TestMaxInteger testing max integer class
"""
import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_default_list(self):
        self.assertEqual(max_integer(), None)

        def test_max_list_first(self):
            list = [55, 5, 3, 44]
            self.assertEqual(max_integer(list), 55)

            def test_max_list_last(self):
                list = [0, 1, 3, 55]
                self.assertEqual(max_integer(list), 55)

                def test_max_mixed_list(self):
                    list = [-1, -4, 0, 4, -6]
                    self.assertEqual(max_integer(list), 4)

                    def test_max_list_with_string(self):
                        list = ['issam', 5, 6, 9]
                        with self.assertRaises(TypeError):
                            max_integer(list)

                            if __name__ = "__main__":
                                unittest.main()
