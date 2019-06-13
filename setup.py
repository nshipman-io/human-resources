from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read() 

setup(
    name='human-resources',
    version='0.1.0',
    description='Commandline user management utility',
    long_description=readme,
    author='Norman',
    author_email='norman@nshipman.io',
    install_requires=[],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': 'hr=hr.cli:main',
    },
)