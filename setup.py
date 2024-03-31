from setuptools import find_packages, setup
from pathlib import Path

from mfdfa_toolkit import __version__

long_description = Path('README.md').read_text(encoding='utf8')

setup(
    name="mfdfa_toolkit",
    version=__version__,
    description="Multi-Fractal Detrended Fluctuation Analysis (MFDFA)",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/mohsenim/Multifractality",
    author="Mahdi Mohseni",
    author_email="mohsnei.cs@gmail.com",
    packages=find_packages(exclude=["tests", "tests.*"]),
    
    install_requires=[
        "numpy",
        "scikit-learn",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
