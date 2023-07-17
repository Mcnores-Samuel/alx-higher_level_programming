#!/usr/bin/python3
"""This module define the Test_base class for test base.py module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_base_class_instatiation(unittest.TestCase):
    """Test_base_class_instatiation tests the instatiation of the Base class"""
    def test_base_id_value(self):
        """Tests Base id value if it increament if None value is passed"""
        base1 = Base()
        base2 = Base(None)
        base3 = Base()
        base4 = Base(12)
        base5 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)
        self.assertEqual(base4.id, 12)
        self.assertEqual(base5.id, 4)

    def test_object_value_true(self):
        """Tests the truthy of the id value"""
        base1 = Base()
        base2 = Base(9)
        self.assertNotEqual(base1.id, base2.id)
        self.assertTrue(base1.id)
        self.assertTrue(Base(None))

    def test_access_attributes(self):
        """Tries to access a pricvate class  attribute"""
        with self.assertRaises(AttributeError):
            print(Base(1).__nb_objects)

    def test_rectangle_id(self):
        """Tests the value of the id from Rectangle class a subclass of Base
        class

        Rectangle(width, height, x=0, y=0, id=None) is inherits from the base
        class and the following test cases tries to access the ability of the
        id public instance attribute
        """
        rbase1 = Rectangle(1, 2, 0, 0)
        rbase2 = Rectangle(1, 2, 0, 0)
        rbase3 = Rectangle(1, 2, 0, 0, 10)
        self.assertEqual(rbase1.id, 7)
        self.assertEqual(rbase2.id, 8)
        self.assertEqual(rbase3.id, 10)


if __name__ == "__main__":
    unittest.main()
