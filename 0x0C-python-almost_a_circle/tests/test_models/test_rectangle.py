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


class Test_width_initialization_and_validation(unittest.TestCase):
    """Tests width value validation during initialisation"""
    def test_width_type_validation1(self):
        """Tests type validation of the width of the rectangle object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 12)

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
    def test_heigth_type_validation1(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "12")

    def test_heigth_type_validation2(self):
        with self.assertRaises(TypeError):
            Rectangle(1, None)

    def test_heigth_type_validation3(self):
        with self.assertRaises(TypeError):
            Rectangle(1, {1, 2, 3})

    def test_heigth_type_validation4(self):
        with self.assertRaises(TypeError):
            Rectangle(1, [1, 2, 3])

    def test_heigth_type_validation5(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 12.3)

    def test_heigth_type_validation6(self):
        with self.assertRaises(TypeError):
            rect = {"height": 14}
            Rectangle(1, rect)

    def test_heigth_value_validation(self):
        """Tests value validation of the height of the rectangle object"""
        with self.assertRaises(ValueError):
            Rectangle(1, -15)

    def test_heigth_value_validation1(self):
        """Tests value validation of the height of the rectangle object"""
        with self.assertRaises(ValueError):
            Rectangle(1, -1)

    def test_heigth_value_validation2(self):
        """Tests value validation of the height of the rectangle object"""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)


class Test_x_initialization_and_validation(unittest.TestCase):
    def test_x_type_validation1(self):
        """Tests type validation of the x value of the rectangle object"""
        with self.assertRaises(TypeError):
            Rectangle(1, 1, None)

    def test_x_type_validation2(self):
        """Tests type validation of the x value of the rectangle object"""
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1.0)

    def test_x_type_validation3(self):
        """Tests type validation of the x value of the rectangle object"""
        with self.assertRaises(TypeError):
            Rectangle(1, 1, [1, 2, 3])

    def test_x_type_validation4(self):
        """Tests type validation of the x value of the rectangle object"""
        with self.assertRaises(TypeError):
            Rectangle(1, 1, (1, 2))

    def test_x_type_validation5(self):
        """Tests type validation of the x value of the rectangle object"""
        with self.assertRaises(TypeError):
            Rectangle(1, 1, {1, 2, 3})

    def test_x_type_validation6(self):
        """Tests type validation of the x value of the rectangle object"""
        with self.assertRaises(TypeError):
            rect = {"x": 12}
            Rectangle(1, 1, rect)

    def test_x_type_validation7(self):
        """Tests type validation of the x value of the rectangle object"""
        with self.assertRaises(TypeError):
            Rectangle(1, 1, "")

    def test_x_value_validation(self):
        """Tests value validation of the x value of the rectangle object"""
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -10)

    def test_x_value_validation1(self):
        """Tests value validation of the x value of the rectangle object"""
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1)

    def test_x_value_validation2(self):
        """Tests value validation of the x value of the rectangle object"""
        with self.assertRaises(ValueError):
            x = 10 - 15
            Rectangle(1, 1, x)


class Test_y_initialization_and_validation(unittest.TestCase):

    def test_y_type_validation1(self):
        """Tests type validation of the y value of the rectangle object"""
        with self.assertRaises(TypeError):
            Rectangle(1, 12, {})

    def test_y_type_validation2(self):
        """Tests type validation of the y value of the rectangle object"""
        with self.assertRaises(TypeError):
            Rectangle(1, 12, "20")

    def test_y_type_validation3(self):
        """Tests type validation of the y value of the rectangle object"""
        with self.assertRaises(TypeError):
            Rectangle(1, 12, 91.9)

    def test_y_type_validation4(self):
        """Tests type validation of the y value of the rectangle object"""
        with self.assertRaises(TypeError):
            Rectangle(1, 12, None)

    def test_y_type_validation5(self):
        """Tests type validation of the y value of the rectangle object"""
        with self.assertRaises(TypeError):
            Rectangle(1, 12, {1, 2, 3})

    def test_y_type_validation6(self):
        """Tests type validation of the y value of the rectangle object"""
        with self.assertRaises(TypeError):
            Rectangle(1, 12, ())

    def test_y_type_validation7(self):
        """Tests type validation of the y value of the rectangle object"""
        with self.assertRaises(TypeError):
            Rectangle(1, 12, y={"y": 12})

    def test_y_value_validation(self):
        """Tests value validation of the y value of the rectangle object"""
        with self.assertRaises(ValueError):
            Rectangle(1, 12, -1)

    def test_y_value_validation1(self):
        """Tests value validation of the y value of the rectangle object"""
        with self.assertRaises(ValueError):
            Rectangle(1, 12, y=1 - 12)


class TestRectangle_order_of_initialization(unittest.TestCase):
    """Unittests for testing Rectangle order of attribute initialization."""

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, "invalid x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, 3, "invalid y")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", "invalid x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", 2, "invalid y")

    def test_x_before_y(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "invalid x", "invalid y")


class TestRectangle_area(unittest.TestCase):
    """Unittests for testing the area method of the Rectangle class."""

    def test_area_small(self):
        r = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())

    def test_area_large(self):
        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())

    def test_area_changed_attributes(self):
        r = Rectangle(2, 10, 1, 1, 1)
        r.width = 7
        r.height = 14
        self.assertEqual(98, r.area())

    def test_area_one_arg(self):
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)


class TestRectangle_stdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Rectangle class."""

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout.

        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture_stdout = StringIO()
        sys.stdout = capture_stdout
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture_stdout

    # Test __str__ method
    def test_str_method_print_width_height(self):
        r = Rectangle(4, 6)
        capture = TestRectangle_stdout.capture_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_width_height_x(self):
        r = Rectangle(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)
        self.assertEqual(correct, r.__str__())

    def test_str_method_width_height_x_y(self):
        r = Rectangle(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(correct, str(r))

    def test_str_method_width_height_x_y_id(self):
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

    def test_str_method_changed_attributes(self):
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

    def test_str_method_one_arg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    # Test display method
    def test_display_width_height(self):
        r = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        r = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_width_height_y(self):
        r = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_width_height_x_y(self):
        r = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)


class TestRectangle_update_args(unittest.TestCase):
    """Unittests for testing update args method of the Rectangle class."""

    # Test args
    def test_update_args_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_args_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

    def test_update_args_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_args_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_args_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

    def test_update_args_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_more_than_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None, 4, 5, 2)
        correct = "[Rectangle] ({}) 2/10 - 4/5".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        r.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(r))

    def test_update_args_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def test_update_args_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)

    def test_update_args_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, -5)

    def test_update_args_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "invalid")

    def test_update_args_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, 0)

    def test_update_args_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, -5)

    def test_update_args_invalid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(89, 2, 3, "invalid")

    def test_update_args_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 1, 2, -6)

    def test_update_args_invalid_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(89, 2, 3, 4, "invalid")

    def test_update_args_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 1, 2, 3, -6)

    def test_update_args_width_before_height(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", "invalid")

    def test_update_args_width_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, "invalid")

    def test_update_args_width_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, 2, "invalid")

    def test_update_args_height_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", "invalid")

    def test_update_args_height_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", 1, "invalid")

    def test_update_args_x_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(89, 1, 2, "invalid", "invalid")


class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of the Rectangle class."""

    def test_update_kwargs_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_kwargs_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_kwargs_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def test_update_kwargs_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def test_update_kwargs_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(r))

    def test_update_kwargs_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def test_update_kwargs_inavlid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_args_and_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_kwargs_some_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(r))


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Rectangle class."""

    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
