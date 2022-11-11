from setuptools import setup, find_packages
from typing import List

def get_requirements()-> List[str]:
    '''Returns a list of requirements'''
    requirement_list = []
    return requirement_list

setup(
    name='sensor',
    version='0.0.1',
    author='Prabhu',
    author_email='prabhupannase7@gmail.com',
    packages= find_packages(),
    install_requires= get_requirements()

)