from setuptools import setup, find_packages

setup(
    name = 'slepy',
    version = '0.1',
    packages = find_packages(),
    install_requires=['pytz>=2024.2', 'tqdm>=4.67.1'],
)
