import pandas as pd
import requests    
#ticker_symbol = 'AMZN'

def get_company_data(ticker_symbol):
    overview = get_overview(ticker_symbol)
    anomalies = findanomaly(ticker_symbol)
    income_statement = generate_income_statement(ticker_symbol)
    
    return {
        'Overview of the Company': overview,
        'OHLCV + Anomalies detected:': anomalies,
        'Income Statement':  income_statement
    }

def get_overview(ticker_symbol):
        api_key  = 'YOUR_KEY'
        base_url = 'https://www.alphavantage.co/query'
        function = 'OVERVIEW'
        url = f"{base_url}?function={function}&symbol={ticker_symbol}&apikey={api_key}"
        r = requests.get(url)
        data = r.json()
        df = pd.DataFrame([data])
        df_transposed = df.transpose()
        print("\n")
        return df_transposed
    
def findanomaly(ticker_symbol):    
        api_key  = 'YOUR_KEY'
        base_url = 'https://www.alphavantage.co/query'
        function = 'TIME_SERIES_DAILY'
        url = f"{base_url}?function={function}&symbol={ticker_symbol}&apikey={api_key}" 
        r = requests.get(url)
        data = r.json()
        
        time_series_data = data['Time Series (Daily)']
        df = pd.DataFrame(time_series_data).T #prints Original DataFrame
        df.index = pd.to_datetime(df.index)
        df = df.apply(pd.to_numeric)
        df['price_change'] = df['4. close']-df['1. open']
        average_volume = df['5. volume'].mean()
        df['volume_surge'] = df['5. volume'] > 1.5 * average_volume
        df['price_gap'] = df['1. open'] > df['4. close'].shift(1) * 1.02 #each closing value is now aligned with the opening price of the next day
        #1.02 represents a 2% increase over the closing price of the previous day.
        #print("DataFrame with calculated columns:")
        #print(df)
        
        anomalies = df[(df['price_change'].abs() > 2) | df['volume_surge'] | df['price_gap']]
        
        #print("\nOHLCV + Anomalies detected:")
        #print(anomalies)
        print("\n")
        return anomalies


def generate_income_statement(ticker_symbol):
    #print("\nIncome Statement:")
    api_key = 'YOUR_KEY'  # Replace 'demo' with your actual API key
    base_url = 'https://www.alphavantage.co/query'
    function = 'CASH_FLOW'
    url = f"{base_url}?function={function}&symbol={ticker_symbol}&apikey={api_key}"
    #print(url)
    r = requests.get(url)
    data = r.json()
    # Convert to DataFrame
    df = pd.DataFrame(data['annualReports'])

    # Print DataFrame
    #print(df)
    print("\n")
    return df

#print(get_company_data(ticker_symbol))
# print(get_overview(ticker_symbol))
# print(findanomaly(ticker_symbol))
# print(generate_income_statement(ticker_symbol))
