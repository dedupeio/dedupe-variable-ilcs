try:
    from setuptools import setup
except ImportError:
    raise ImportError(
        "setuptools module required, please go to "
        "https://pypi.python.org/pypi/setuptools and follow the instructions "
        "for installing setuptools"
    )

setup(
    version='0.0.0',
    url='https://github.com/dedupeio/dedupe-variable-ilcs',
    description='Dedupe variable for Illinois Compiled Statute (ILCS) codes',
    name='dedupe-variable-ilcs',
    packages=['dedupe.variables'],
    license='The MIT License: http://www.opensource.org/licenses/mit-license.php',
    install_requires=[
        'ilcs-parser @ https://github.com/datamade/ilcs-parser/archive/master.zip#egg=ilcs-parser-0.0.0',
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
