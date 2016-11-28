from setuptools import setup

setup(name='CalCalc',
      version='1.0',
      description='Wolfram Alpha queries in Python',
      url='http://github.com/'
      author='Caroline Sofiatti'
      author_email='sofiatti@berkeley.edu',
      license='None',
      packages=['CalCalc'],
      install_requires=['requests'],
      tests_require=['pytest']
      )
