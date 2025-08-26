import setuptools
from distutils.util import convert_path

main_ns = {}
ver_path = convert_path('wqp/__init__.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

setuptools.setup(
    name='wqp',
    version=main_ns['__version__'],
    author='sega.ndiaye.pro@gmail.com',
    description='Wine quality predictor - a packaged machine learning algorithm to predict wine quality',
    packages=setuptools.find_packages(),
    install_requires=[
        "scikit-learn==1.7.1",
        "pandas==2.3.2",
        "click==8.2.1",
        "numpy==2.2.6",
        "pandas==2.3.2",
        "scikit-learn==1.7.1",
        "typing==3.7.4.3",
        "click==8.2.1"
    ],
    entry_points='''
    [console_scripts]
    wqp=wqp.cli:wqp
    '''
)