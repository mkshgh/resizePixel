from setuptools import setup, find_packages
from resizePixel.version import Version
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.13'
DESCRIPTION = 'Python Resize Pixel'
LONG_DESCRIPTION = open('README.md').read().strip()

# Setting up
setup(
    name='resizePixel',
    version=Version('1.0.0').number,
    author="mkshgh",
    author_email="<mukesh.ghimire@outlook.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    url='mghimire.com.np',
    packages=find_packages(),
    package_dir={'','src'},
    install_requires=['pytest', 'pytest-cov', 'PIL'],
    keywords=['python', 'image', 'image quality', 'reduce', 'increase', 'frustrated'],
    classifiers=[
        "Development Status :: 1 - Testing",
        "Intended Audience :: Dreamers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)