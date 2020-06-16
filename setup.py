try:
    from setuptools import setup
except ImportError:
    raise ImportError(
        "setuptools module required, please go to "
        "https://pypi.python.org/pypi/setuptools and follow the instructions "
        "for installing setuptools"
    )


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    version='0.1.0',
    author='DataMade',
    url='https://github.com/dedupeio/dedupe-variable-ilcs',
    description='Dedupe variable for Illinois Compiled Statute (ILCS) codes',
    long_description=readme(),
    long_description_content_type='text/markdown',
    name='dedupe-variable-ilcs',
    packages=['dedupe.variables'],
    license='The MIT License: http://www.opensource.org/licenses/mit-license.php',
    install_requires=[
        'ilcs-parser',
        'parseratorvariable'
    ],
    extras_require={'tests': ['pytest', 'parserator']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis']
)
