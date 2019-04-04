
## P0: Explore Weather Trends

### Prerequisites

Additional installations: 

* [Missingno](https://github.com/ResidentMario/missingno)
* [sklearn](https://scikit-learn.org/)

## Project Overview

This first project required the following steps:
* Extract data from a database using a SQL query
* Calculate a moving average
* Create a line chart 

I analyzed local and global temperature data and compared the temperature trends in three german cities to overall global temperature trends. After some data cleaning I created a function to assist the data processing and visualization with some options to play around with. This included also the calculation of a simple linear regression to visualize trends.

![Global Weather Trend](https://github.com/DataLind/Udacity-Data-Analyst-Nanodegree/blob/master/global_weather_trend.png)

### Data Sources

**Name:** city_data.csv
* Definition: Overall city temperature data
* Source: Udacity
* Version: 1
* Method of gathering: SQL

**Name:** global_data.csv
* Definition: Global temperature data
* Source: Udacity
* Version: 1
* Method of gathering: SQL

**Name:** city_list.csv
* Definition: List of cities in this dataset
* Source: Udacity
* Version: 1
* Method of gathering: SQL

### Wrangling
* Cut data to years 1750 - 2013

### Summary

> To conclude, there is a clear overall uptrend visible, what means, that the average global temperature is increasing, with an also increasing tempo.

The german cities Hamburg, Berlin and Munich got compared to the global data (1750 - 2013):

- The slope of the global trend is higher than compared to the german cities, so the global average temperature is increasing faster (looking at this long time period)
- Berlin has the highest average temperature among the german cities, making Berlin the only city that has a higher average temperature than the global
- Hamburg is the closest to the global average temperature, while Munich has the lowest average temperature, but also the highest correlation to the global data compared to the other two german cities

### Authors

* Christoph Lindstädt
* Udacity

## License

* <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"> Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>

<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">
	<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" />
</a>
