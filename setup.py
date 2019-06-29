from setuptools import setup, find_packages


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


setup(
    name='envs',
    description='Easy access of environment variables from Python with support for strings, booleans, list, tuples, and dicts.',
    url='https://github.com/bjinwright/envs',
    author='Brian Jinwright',
    license='GNU GPL v3',
    keywords='environment variables',
    extras_require={
        'cli': parse_requirements('requirements_cli.txt'),
    },
    packages=find_packages(),
    py_modules=['envs.cli'],
    include_package_data=True,
    zip_safe=True,
    version='1.3',
    entry_points='''
        [console_scripts]
        envs=envs.cli:envs
        ''',
)

