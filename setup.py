from distutils.core import setup


setup(
  name='eloquentarduino',
  packages=['eloquent_edgeimpulse'],
  version='1.0.0',
  license='MIT',
  description='A wrapper for Edge Impulse Linux package',
  author='Simone Salerno',
  author_email='eloquentarduino@gmail.com',
  url='https://github.com/eloquentarduino/eloquent-edge-impulse-python',
  keywords=[
    'ML',
    'Edge Impulse',
    'Edge AI'
  ],
  install_requires=[
    'numpy',
  ]
)