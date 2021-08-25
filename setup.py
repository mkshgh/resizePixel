import setuptools
from packagename.version import Version


setuptools.setup(name='resizePixel',
                 version=Version('1.0.0').number,
                 description='Python Resize Pixel',
                 long_description=open('README.md').read().strip(),
                 author='mkshgh',
                 author_email='mukesh.ghimire@outlook.com',
                 url='mghimire.com.np',
                 py_modules=['packagename'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords='resize image',
                 classifiers=['Packages', 'ResizePixel'])
