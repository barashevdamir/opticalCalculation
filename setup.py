from setuptools import setup, find_packages

setup(
    name='opticalCalculation',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'scipy',
        'scikit-image',
        'plotly',
    ],
    author='Damir Barashev',
    author_email='barashevdamir@yandex.ru',
    description='A library for creating and analyzing gratings',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/barashevdamir/opricalCalculation',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
