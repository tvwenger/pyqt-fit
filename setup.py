#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup

setup(name='PyQt-Fit',
      version='1.0.1',
      description='Last-square fitting of user-defined functions',
      author='Pierre Barbier de Reuille',
      author_email='pierre.barbierdereuille@gmail.com',
      url=['https://code.google.com/p/pyqt-fit/'],
      packages= ['pyqt_fit', 'pyqt_fit/functions', 'pyqt_fit/residuals'],
      package_data = {'pyqt_fit': ['qt_fit.ui']},
      scripts=['pyqt_fit1d.py'],
      requires=['setuptools', 'scipy', 'numpy', 'cython', 'pylab', 'PyQT4', 'matplotlib'],
     )
