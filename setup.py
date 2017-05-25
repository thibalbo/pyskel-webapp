from setuptools import setup, find_packages

setup(name='pyskel-webapp',
      packages=find_packages(),
      entry_points={
        'console_scripts': [
            'rwebapp = webapp.__main__:main',
        ]}
      )
