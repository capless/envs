import os
import ast

VALID_TYPES = (
    'string','boolean',
    'list','tuple','integer',
    'float','dict'
)

class Env(object):

    def __call__(self, key, default=None, var_type='string'):
        value = os.getenv(key,default)
        if not var_type in VALID_TYPES:
            raise ValueError(
                'The var_type argument should be one of the following {0}'.format(','.join(VALID_TYPES)))
        validate = getattr(self,'validate_{0}'.format(var_type))
        return validate(value)

    def validate_boolean(self,value):
        true_vals = ('True', 'true', 1, '1')
        false_vals = ('False', 'false', 0, '0')
        if value in true_vals:
            value = True
        elif value in false_vals:
            value = False
        else:
            raise ValueError('This value is not a boolean value.')
        return value

    def validate_string(self,value):
        return value

    def validate_integer(self,value):
        return int(value)

    def validate_list(self,value):
        return list(ast.literal_eval(value))

    def validate_tuple(self,value):
        return tuple(ast.literal_eval(value))

    def validate_dict(self, value):
        return dict(ast.literal_eval(value))

    def validate_float(self,value):
        return float(value)


env = Env()