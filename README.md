# Stock-data-finding-Python-Package-
Data Retrieval upon a method passing. Thats what packages are about. Also it fosters Code-Reproducability

# 1. Introduction: 
In this project, we aimed to analyze financial time series data for detecting anomalies using Python. We utilized 
historical daily stock data from Alpha Vantage API and implemented anomaly detection techniques to identify 
significant deviations in price changes, volume surges, and price gaps.
Also it returns a Description of the Stock along with the Income Statements over the past few years.
 
# 2. Data Retrieval: 
We used the Alpha Vantage API to fetch historical daily stock data for a given ticker symbol. The `findanomaly` 
function was developed to construct the API query and retrieve the data. This function also incorporated error 
handling to manage API request failures.

# To reproduce the output, follow the following steps:
1. directory-structure:
stock-
 setup.py
 stock_data-
  company.py
  __init__.py

2. replace YOUR_KEY in company.py with your own api_key which can be obtained from its website (https://www.alphavantage.co/support/#api-key)

3.after replacement, run these commands in terminal
 a. python setup.py sdist bdist_wheel
 b. pip install path-to-.whl-file
 c. open powershell and type these commands
  c1. python
  c2. from stock_data import get_company_data
  c3. get_company_data('AAPL') #You can choose any ticker symbol here, just google the ticker symbols for NASDAQ traded stocks
