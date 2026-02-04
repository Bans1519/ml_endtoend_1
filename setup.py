from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Returns a list of requirements from a file
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # reads all lines
    
    # Remove '\n' and empty lines
    requirements = [req.strip() for req in requirements if req.strip()]
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='ml_endtoend_proj1',
    version='0.0.1',
    author='Bansari Maru',
    author_email='bansari.gmaru@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
