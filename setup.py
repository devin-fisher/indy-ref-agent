from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='indy-ref-agent',
    version='0.1.0',
    description='reference implementation of agent protocol',
    long_description=readme,
    author='Devin Fisher',
    author_email='devin.fisher@evernym.com',
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
    python_requires='>3.5',
    install_requires=['python3-indy']
)
