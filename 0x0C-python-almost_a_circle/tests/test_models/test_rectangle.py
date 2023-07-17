#!/usr/bin/python3

"""This module define a unittest for the rectangle.py module"""
import sys
from io import StringIO
import unittest
from models.rectangle import Rectangle


class Test_rectangle_module_instatiation(unittest.TestCase):
    """Defines Test_rectangle_module for instatiation and test the module"""
    def test_rectangle_id(self):
        """Tests the value of the id from Rectangle class a subclass of Base
        class

        Rectangle(width, height, x=0, y=0, id=None) is inherits from the base
        class and the following test cases tries to access the ability of the
        id public instance attribute
        """
        rbase1 = Rectangle(1, 2,)
        rbase2 = Rectangle(1, 2,)
        rbase3 = Rectangle(1, 2, 0, 0, 10)
        self.assertEqual(rbase1.id, rbase2.id - 1)
        rbase1.id = rbase2.id
        self.assertEqual(rbase2.id, rbase1.id)
        self.assertEqual(rbase3.id, 10)

    def test_obj_automation(self):
        """Automates object creation and also access the id attribute"""
        test_list = []
        objs = [chr(n) for n in range(65, 91)]
        for item in objs:
            item = Rectangle(1, 2)
            test_list.append(item.id)
        expects = [id for id in range(test_list[0], test_list[-1] + 1)]
        self.assertEqual(test_list, expects)

    def test_x_type_validation(self):
        """Tests type validation of the x value of the rectangle object"""
        with self.assertRaises(TypeError):
            Rectangle(1, 1, [])

    def test_y_type_validation(self):
        """Tests type validation of the y value of the rectangle object"""
        with self.assertRaises(TypeError):
            Rectangle(1, 12, {})

    def test_heigth_value_validation(self):
        """Tests value validation of the height of the rectangle object"""
        with self.assertRaises(ValueError):
            Rectangle(1, -15)

    def test_x_value_validation(self):
        """Tests value validation of the x value of the rectangle object"""
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -10)

    def test_y_value_validation(self):
        """Tests value validation of the y value of the rectangle object"""
        with self.assertRaises(ValueError):
            Rectangle(1, 12, -1)


class Test_width_initialization_and_validation(unittest.TestCase):
    """Tests width value validation during initialisation"""
    def test_width_type_validation1(self):
        """Tests type validation of the width of the rectangle object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 12)

    def test_width_type_validation2(self):
        """Tests type validation of the width of the rectangle object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 12)

    def test_width_type_validation3(self):
        """Tests type validation of the width of the rectangle object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 12)

    def test_width_type_validation4(self):
        """Tests type validation of the width of the rectangle object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 12)

    def test_width_type_validation5(self):
        """Tests type validation of the width of the rectangle object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(12.34, 12)

    def test_width_type_validation6(self):
        """Tests type validation of the width of the rectangle object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 12)

    def test_width_type_validation7(self):
        """Tests type validation of the width of the rectangle object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            test = {"width": int("12")}
            Rectangle(test, 12)

    def test_width_value_validation(self):
        """Tests value validation of the width of the rectangle object"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 12)

    def test_width_value_validation1(self):
        """Tests value validation of the width of the rectangle object"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-124, 12)


class Test_heigth_initialization_and_validation(unittest.TestCase):
    """Tests type validation of the height of the rectangle object"""
    def test_heigth_type_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "12")


class Test_rectangle_area_mothod(unittest.TestCase):

    def test_area_using_list_automation(self):
        width_n = [n + 3 for n in range(2, 22)]
        height_n = [n for n in range(2, 100, 5)]
        for x in width_n:
            for y in height_n:
                rect = Rectangle(x, y)
                self.assertEqual(rect.area(), x * y)


if __name__ == "__main__":
    unittest.main()
