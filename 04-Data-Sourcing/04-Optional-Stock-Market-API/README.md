# Stock Market API

In this exercice, we are going to play around with the stock market API [iexcloud.io](https://iexcloud.io/).

The goal here is to get comfortable reading API documentation.

---

## Apple stock for the last 3 months

Let's find the API documentation page of [iexcloud.io](https://iexcloud.io/)

<details><summary markdown='span'>Solution
</summary>
Documentation pages are often hidden in the footer or in some menu.<br/>
Typing <i>'the_website_name API documentation'</i> in the google search bar is a quick way to find it too.
<br>
solution: <a href="https://iexcloud.io/docs/api/">https://iexcloud.io/docs/api/</a>
</details>

### API setup

The endpoints of the API we want to use are protected behind a paywall.

As Le Wagon, we kindly provide you with a proxy to that API for you to use only during the challenge today. We trust you!

Here’s how it works:

1. API would say: use https://cloud.iexapis.com/stable/stock/aapl/stats?token=...
1. Copy this URL, and replace `cloud.iexapis.com` with `iex.lewagon.com`
1. You can [try it now](https://iex.lewagon.com/stable/stock/aapl/stats)

### Using the API

Now let's find in the IEXCloud API the **URL** for the last 3 months of Apple stock prices.

When you find the URL copy and paste it in a new tab and look at the data you get from the API.
It should be a JSON looking like that:
<details><summary markdown='span'>Show example
</summary>

```json
[
    {
        date: "2014-04-17",
        open: 68.2926,
        high: 69.3117,
        low: 68.1875,
        close: 68.9414,
        volume: 71106721,
        unadjustedVolume: 10158103,
        change: 0.778798,
        changePercent: 1.143,
        vwap: 68.8375,
        label: "Apr 17, 14",
        changeOverTime: 0
    },
    {
        date: "2014-04-21",
        open: 68.9939,
        high: 69.8869,
        low: 68.8127,
        close: 69.7596,
        volume: 45668931,
        unadjustedVolume: 6524133,
        change: 0.8182,
        changePercent: 1.187,
        vwap: 69.5143,
        label: "Apr 21, 14",
        changeOverTime: 0.011868050257174998
    },
...
]
```
</details>

⚠️ Take your time before reading the solution, finding what we want in API documentations can usually take **10 to 15 minutes of reading**

<details><summary markdown='span'>Solution
</summary>
You can find this information here in the documentation:
<a href="https://iexcloud.io/docs/api/#historical-prices">https://iexcloud.io/docs/api/#historical-prices</a>
<br>
The URL is:
<pre>
https://iex.lewagon.com/stable/stock/aapl/chart/3m
</pre>
</details>

You've probably noticed that urls provided in the documentation often include `{symbol}`. This dynamic parameter refers to the `symbol` or `ticker` of a listed company stock. To find this unique identifier, you can type the name of the company in [Google Finance's search bar](https://www.google.com/finance). The `symbol` (usually 2 to 4 letters long) will appear next to the name of the stock exchange (e.g. `NASDAQ`).

------

## Using API data in pandas

### Setup
For this exercise we will work in a Notebook.

```sh
jupyter notebook
```

Go ahead and create a new Python Notebook in the `04-Data-Sourcing/01-Stock-Market-API` folder of your python-challenges repository.

Start with the usual imports in the first cell:

```python
%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib
```

We will reuse the **API URL** for the **last 3 months of Apple stock prices** here.<br>
To make a **call** to the API you can use the following code:

```python
import requests

url = "YOUR_API_URL"
api_data = requests.get(url).json()
```

You can now **create a dataframe** from this data.

<br>
<details><summary markdown='span'>Solution
</summary>
<code>apple_stock_df = pd.DataFrame.from_dict(api_data)</code>
</details>

With this dataframe we can **plot** the evolution of the stock price.
But before that we need to do 2 things:
- Convert 'date' column to datetime object
- Set the date column as the index

### Converting date to datetime object

To do that you can use Pandas.to_datetime()

- **pd.to_datetime** documentation: [http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html#pandas.to_datetime](http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html#pandas.to_datetime)
- **Format** documentation: [http://strftime.org/](http://strftime.org/)

<details><summary markdown='span'>Solution
</summary>
<code>apple_stock_df['date'] = pd.to_datetime(apple_stock_df['date'], format="%Y-%m-%d")</code>
</details>

### Set the date column as the index

To do that you can use the DataFrame method **set_index**

- documentation: [https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html)


<details><summary markdown='span'>Solution
</summary>
<code>apple_stock_df = apple_stock_df.set_index('date')</code>
</details>

### Now we can plot 🎉

First let's plot with only the values in the **'close'** column

<details><summary markdown='span'>Solution
</summary>
<code>apple_stock_df['close'].plot()</code>
</details>

Now we can make a plot with the values in **'open', 'close', 'high', 'low'**

<details><summary markdown='span'>Solution
</summary>
<code>apple_stock_df[['open', 'close', 'high', 'low']].plot()</code>
</details>

As we can see our plot is really hard to read. We can improve its readability with the **figsize** argument of the `plot()` method.
- documentation: [https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html)

<details><summary markdown='span'>Solution
</summary>
<code>apple_stock_df[['open', 'close', 'high', 'low']].plot(figsize=(12,4))</code>
</details>

---

## Back to the API

Let's find out what kind of data we can get from this API 🕵️‍♂️

### What is the URL for:

1) Amazon stock prices since last year?
2) Facebook market cap?
3) Apple research and development spendings quarterly?
4) The last news about Tesla?
5) The performance of the 'Energy' sector?

<details><summary markdown='span'>All Solutions
</summary>
<ol>
        <li>https://iex.lewagon.com/stable/stock/amzn/chart/1y</li>
        <li>https://iex.lewagon.com/stable/stock/fb/stats</li>
        <li>https://iex.lewagon.com/stable/stock/aapl/financials</li>
        <li>https://iex.lewagon.com/stable/stock/tsla/news/last/1</li>
        <li>https://iex.lewagon.com/stable/stock/market/sector-performance</li>
</ol>
</details>

---

:bulb: Don't forget to **push your code to GitHub**

# (Optional) Plotting _multiple_ line charts

We'd like to **compare** the evolution of the GAFA stocks (Google, Apple, Facebook, Amazon) by plotting them on the _same_ chart. Reuse the code from above to build a dataframe with one column per stock and keeping the dates as the index. Maybe you can use some normalization technique at `t = 0` to compare better the relative performance of each stock!

:warning: **DON'T LOOP OVER THE API CALL, GET THE DATA ONCE AND THEN STOP** :warning:

Or you will block the API for your buddies, thank you 🙏

### 1. Retrieve Data for Each Company

First, we need to retrieve the historical stock prices for each of these companies over the same time period. As per the exercise setup, we use the IEX Cloud API proxy provided by Le Wagon, with URLs customized for each stock symbol. 
Given the instruction not to loop over API calls to avoid rate limiting, please ensure to make these calls carefully and save your data before proceeding with further analysis.

For each company, you would use a URL pattern like this, replacing {symbol} with the company's stock symbol (`GOOGL` for Google, `AAPL` for Apple, `META` for Meta, `AMZN` for Amazon, `MSFT` for Microsoft):

```bash
https://iex.lewagon.com/stable/stock/{symbol}/chart/3m
```

### 2. Data Preprocessing

After fetching the data, the next steps would involve:

- Converting the 'date' column to datetime objects.
- Setting the 'date' column as the index.
- Normalizing the stock prices to compare their relative performance from a common starting point. A common approach is to divide all prices by the first price in the dataset, effectively starting each stock's performance from 1 (or 100 if you prefer percentage terms) at t = 0.

### 3. Plotting the Data
Once the data is prepared, you can plot it using pandas' `.plot()` method, specifying `figsize` for better readability, as discussed in the initial setup.

### Example Code for Preprocessing and Plotting
Below is a simplified example code structure that outlines these steps. 

<details><summary markdown='span'>View Solution
</summary>

```python
import pandas as pd
import requests


apple_url = "https://iex.lewagon.com/stable/stock/aapl/chart/3m"
apple_api_data = requests.get(apple_url).json()
apple_stock_df = pd.DataFrame.from_dict(apple_api_data)
apple_stock_df['date'] = pd.to_datetime(apple_stock_df['date'], format="%Y-%m-%d")
df_apple = apple_stock_df.set_index('date')

microsoft_url = "https://iex.lewagon.com/stable/stock/msft/chart/3m"
microsoft_api_data = requests.get(microsoft_url).json()
microsoft_stock_df = pd.DataFrame.from_dict(microsoft_api_data)
microsoft_stock_df['date'] = pd.to_datetime(microsoft_stock_df['date'], format="%Y-%m-%d")
df_microsoft = microsoft_stock_df.set_index('date')

meta_url = "https://iex.lewagon.com/stable/stock/meta/chart/3m"
meta_api_data = requests.get(meta_url).json()
meta_stock_df = pd.DataFrame.from_dict(meta_api_data)
meta_stock_df['date'] = pd.to_datetime(meta_stock_df['date'], format="%Y-%m-%d")
df_meta = meta_stock_df.set_index('date')

amzn_url = "https://iex.lewagon.com/stable/stock/amzn/chart/3m"
amzn_api_data = requests.get(amzn_url).json()
amzn_stock_df = pd.DataFrame.from_dict(amzn_api_data)
amzn_stock_df['date'] = pd.to_datetime(amzn_stock_df['date'], format="%Y-%m-%d")
df_amzn = amzn_stock_df.set_index('date')

google_url = "https://iex.lewagon.com/stable/stock/googl/chart/3m"
google_api_data = requests.get(google_url).json()
google_stock_df = pd.DataFrame.from_dict(google_api_data)
google_stock_df['date'] = pd.to_datetime(google_stock_df['date'], format="%Y-%m-%d")
df_google = google_stock_df.set_index('date')


# Normalize each dataframe's 'close' column at t=0
# Example normalization for one dataframe
df_apple['close_normalized'] = df_apple['close'] / df_apple['close'].iloc[0]
df_microsoft['close_normalized'] = df_microsoft['close'] / df_microsoft['close'].iloc[0]
df_google['close_normalized'] = df_google['close'] / df_google['close'].iloc[0]
df_amzn['close_normalized'] = df_amzn['close'] / df_amzn['close'].iloc[0]
df_meta['close_normalized'] = df_meta['close'] / df_meta['close'].iloc[0]

# You would then merge these normalized columns into a single dataframe for plotting
# Assuming all dataframes have the same date range, you could do something like this:
df_combined = pd.DataFrame({
    "GOOGL": df_google['close_normalized'],
    "AAPL": df_apple['close_normalized'],
    "FB": df_meta['close_normalized'],
    "AMZN": df_amzn['close_normalized'],
    "MSFT": df_microsoft['close_normalized']
})

# Plot the combined dataframe
df_combined.plot(figsize=(12,6), title="GAFAM Performance Over 3 Months")
```

</details>

This code is a starting point. You'd need to adapt it to match how you're fetching and storing your data, including handling any potential issues with date ranges or missing values. Remember, the goal here is to compare the stocks' performance relative to their value at the start of the period, giving insight into their relative gains or losses over time.
