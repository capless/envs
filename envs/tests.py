import os
import unittest
from envs import env


class EnvTestCase(unittest.TestCase):

    def setUp(self):
        #Integer
        os.environ.setdefault('VALID_INTEGER','1')
        os.environ.setdefault('INVALID_INTEGER','["seven"]')
        #String
        os.environ.setdefault('VALID_STRING', 'seven')
        #Boolean
        os.environ.setdefault('VALID_BOOLEAN','True')
        os.environ.setdefault('VALID_BOOLEAN_FALSE', 'false')
        os.environ.setdefault('INVALID_BOOLEAN','seven')
        # List
        os.environ.setdefault('VALID_LIST', "['1','2','3']")
        os.environ.setdefault('INVALID_LIST', "1")
        # Tuple
        os.environ.setdefault('VALID_TUPLE', "('True','FALSE')")
        os.environ.setdefault('INVALID_TUPLE', '1')
        # Dict
        os.environ.setdefault('VALID_DICT', "{'first_name':'Suge'}")
        os.environ.setdefault('INVALID_DICT', 'Aaron Rogers')

        # Dict
        os.environ.setdefault('VALID_FLOAT', "5.0")
        os.environ.setdefault('INVALID_FLOAT', '[5.0]')

    def test_integer_valid(self):
        self.assertEqual(1,env('VALID_INTEGER',var_type='integer'))

    def test_integer_invalid(self):
        with self.assertRaises(TypeError) as vm:
            env('INVALID_INTEGER',var_type='integer')

    def test_wrong_var_type(self):
        with self.assertRaises(ValueError) as vm:
            env('INVALID_INTEGER',var_type='set')

    def test_string_valid(self):
        self.assertEqual('seven',env('VALID_STRING'))

    def test_boolean_valid(self):
        self.assertEqual(True, env('VALID_BOOLEAN', var_type='boolean'))

    def test_boolean_valid_false(self):
        self.assertEqual(False, env('VALID_BOOLEAN_FALSE', var_type='boolean'))

    def test_boolean_invalid(self):
        with self.assertRaises(ValueError) as vm:
            env('INVALID_BOOLEAN', var_type='boolean')

    def test_list_valid(self):
        self.assertEqual(['1', '2', '3'], env('VALID_LIST', var_type='list'))

    def test_list_invalid(self):
        with self.assertRaises(TypeError) as vm:
            env('INVALID_LIST', var_type='list')

    def test_tuple_valid(self):
        self.assertEqual(('True','FALSE'), env('VALID_TUPLE', var_type='tuple'))

    def test_tuple_invalid(self):
        with self.assertRaises(TypeError) as vm:
            env('INVALID_TUPLE', var_type='tuple')

    def test_dict_valid(self):
        self.assertEqual({'first_name':'Suge'}, env('VALID_DICT', var_type='dict'))

    def test_dict_invalid(self):
        with self.assertRaises(SyntaxError) as vm:
            env('INVALID_DICT', var_type='dict')

    def test_float_valid(self):
        self.assertEqual(5.0, env('VALID_FLOAT', var_type='float'))

    def test_float_invalid(self):
        with self.assertRaises(TypeError) as vm:
            env('INVALID_FLOAT', var_type='float')

    def test_defaults(self):
        self.assertEqual(env('HELLO',5,var_type='integer'),5)
        self.assertEqual(env('HELLO', 5.0, var_type='float'),5.0)
        self.assertEqual(env('HELLO', [], var_type='list'),[])
        self.assertEqual(env('HELLO', {}, var_type='dict'),{})
        self.assertEqual(env('HELLO', (), var_type='tuple'),())
        self.assertEqual(env('HELLO', 'world'),'world')
        self.assertEqual(env('HELLO', False, var_type='boolean'),False)
        self.assertEqual(env('HELLO', 'False', var_type='boolean'),False)
        self.assertEqual(env('HELLO', 'true', var_type='boolean'), True)

if __name__ == '__main__':
    unittest.main()