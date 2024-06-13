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
stock-<br />
 setup.py<br />
 stock_data-<br />
  company.py<br />
  __init__.py
build files will be generated later on:
![image](https://github.com/ddhruvin/Stock-data-finding-Python-Package-/assets/120237476/31f212d6-f9a3-4e9f-bea1-8ce98c4fa945)


2. replace YOUR_KEY in company.py with your own api_key which can be obtained from its website (https://www.alphavantage.co/support/#api-key)

3.after replacement, run these commands in terminal
 a. python setup.py sdist bdist_wheel<br />
 b. pip install path-to-.whl-file<br />
 c. open powershell and type these commands<br />
  c1. python<br />
  c2. from stock_data import get_company_data<br />
  c3. get_company_data('AAPL') <br />
#You can choose any ticker symbol here, just google the ticker symbols for NASDAQ traded stocks<br />

# 4. IMPORTANT NOTE
Alphavantage has a limit of 25 requests in a day. in the company.py there are 3 requests going to fetch the data, so you can use only /*8 times a day*/ or modify the code to use it more number of times<br />

# Output
![image](https://github.com/ddhruvin/Stock-data-finding-Python-Package-/assets/120237476/27a1c0a5-6579-4aa7-a815-2eff3eeac590)
<br />

<img width="875" alt="image" src="https://github.com/ddhruvin/Stock-data-finding-Python-Package-/assets/120237476/ab49b5a9-5409-48e5-a418-8612f31d5b39">

