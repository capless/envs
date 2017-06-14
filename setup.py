from setuptools import setup, find_packages

from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session=False)

setup(
    name='envs',
    description='Easy access of environment variables from Python with support for strings, booleans, list, tuples, and dicts.',
    url='https://github.com/bjinwright/envs',
    author='Brian Jinwright',
    license='GNU GPL v3',
    keywords='environment variables',
    install_requires=[str(ir.req) for ir in install_reqs],
    packages=find_packages(),
    py_modules=['envs.cli'],
    include_package_data=True,
    zip_safe=True,
    version='1.2.0',
    entry_points='''
        [console_scripts]
        envs=envs.cli:envs
        ''',
)

