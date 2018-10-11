# Python / Matplotlib Stock Price Visualization

## Discovery
I started off by researching American tech stocks, and after a good bit of searching I decided upon five of the major players in the tech/electronic entertainment industry, listed as follows: Take-Two Interactive (which owns Bethesda, Rockstar, and 2K Games), Electronic Arts, Activision-Blizzard, Microsoft, and Nvidia.

## Collection
Using the abilities of Alpha Vantage, the free and open-source stock price tracking system, I constructed multiple query strings to pull sets of CSV data from the markets. I pulled one set, structured into monthly records, for each stock symbol. The following are the query strings I used:

https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=MSFT&apikey=my-api-key&datatype=csv
https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=TTWO&apikey=my-api-key&datatype=csv
https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=EA&apikey=my-api-key&datatype=csv
https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=ATVI&apikey=my-api-key&datatype=csv
https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=NVDA&apikey=my-api-key&datatype=csv

## Data Prep / Cleaning
Now that I had CSV files of each stock symbol, I had to break them down into only the monthly-close price, remove the unnecessary columns, and collate the separate data into a single file.

## Exploration / Planning
To keep the five separate stock symbols from over-cluttering the visualization, I decided to cut the time length displayed to only account for January of 2010 until now. While not as predictive as the full data set, this sectioned version should provide with enough trend detail to allow for a notion of how each symbol has fared in the recent past, and hopefully how it will fare in coming years.

## Modeling
The data would look best on a line chart of connected values to display each stock symbol. There will be a legend in the upper-left corner to denote which color represents which stock at a glance.

## Automation
Using Matplotlib, I was able to create a simple line graph showing the individual stock prices over time in comparison to the others.

## Findings / Review
