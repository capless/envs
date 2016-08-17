import os
import ast


def validate_boolean(value):
    true_vals = ('True', 'true', 1, '1')
    false_vals = ('False', 'false', 0, '0')
    if value in true_vals:
        value = True
    elif value in false_vals:
        value = False
    else:
        raise ValueError('This value is not a boolean value.')
    return value


class Env(object):

    valid_types = {
        'string': None,
        'boolean': validate_boolean,
        'list':list,
        'tuple':tuple,
        'integer':int,
        'float':float,
        'dict':dict
    }

    def __call__(self, key, default=None, var_type='string'):
        value = os.getenv(key,default)
        if not var_type in self.valid_types.keys():
            raise ValueError(
                'The var_type argument should be one of the following {0}'.format(
                    ','.join(self.valid_types.keys())))
        return self.validate_type(value,self.valid_types[var_type])

    def validate_type(self,value,klass):
        if not klass:
            return value
        if klass == validate_boolean:
            return klass(value)
        if isinstance(value,klass):
            return value
        return klass(ast.literal_eval(value))


env = Env()