from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements_list()->List[str]:
    """This function returns a list of packages from requirements.txt

    Returns:
        List[str]: List of the packages to be installed
    """
    with open('requirements.txt') as f:
        requirements_list = f.read().splitlines()
        if HYPHEN_E_DOT in requirements_list:
            requirements_list.remove(HYPHEN_E_DOT)
        return requirements_list

PROJECT_NAME = 'housing-price-predictor'
VERSION = '0.1.0'
AUTHOR = 'Sathish'
AUTHOR_EMAIL = 'mail2sathish11@gmail.com'
DESCRIPTION = 'Housing price prediction using machine learning'
PACKAGES = find_packages() #['housing']


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    packages=PACKAGES,
    include_package_data=True,
    install_requires=get_requirements_list(),
    license='GNU General Public License v3.0',
    keywords='machine learning, housing price prediction',
    url=''
)
