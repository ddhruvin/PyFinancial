from setuptools import setup, find_packages

setup(
    name='stock_data',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'requests',
    ],
    description='A package to fetch stock data including overview, income statement, and anomalies',
    author='Dhruvin Dholakia',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
