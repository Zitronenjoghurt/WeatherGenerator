from setuptools import find_packages, setup
setup(
    name='lemon-weather-generator',
    packages=find_packages(),
    version='0.1.0',
    description='A tool for randomly generating weather with python. Good for e.g. roleplaying or storywriting.',
    author='Zitronenjoghurt',
    license='Apache 2.0',
    install_requires=[],
    setup_requires=['pytest-runner', 'matplotlib'],
    tests_require=['pytest==7.3.1'],
    test_suite='tests',
)