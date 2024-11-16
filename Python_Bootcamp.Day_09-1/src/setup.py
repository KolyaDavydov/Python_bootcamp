from distutils.core import setup, Extension


module = Extension('calculator', sources=['calculator.c'])


setup(name='Calculator',
      version='1.0',
      description='This is a simple calculator module',
      ext_modules=[module])
