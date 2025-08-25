import setuptools

setuptools.setup(
    name='wqp',
    version='1.0.0',
    author='sega.ndiaye.pro@gmail.com',
    description='Wine quality predictor - a packaged machine learning algorithm to predict wine quality',
    packages=setuptools.find_packages(),
    install_requires=[
        "scikit-learn==0.22.1",
        "pandas==1.0.1"
    ]
)