# [Udacity Data Analyst Nanodegree](https://www.udacity.com/course/data-analyst-nanodegree--nd002)

> Discover insights from data via Python and SQL.

## Skills Acquired (Summary)


### Prerequisites

You'll need to install:

* [Python (3.x or higher)](https://www.python.org/downloads/)
* [Jupyter Notebook](https://jupyter.org/)
* [Numpy](http://www.numpy.org/)
* [Pandas](http://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)

And additional libraries defined in each project.

Recommended:

* [Anaconda](https://www.anaconda.com/distribution/#download-section)

## Project Overview
### P0: Explore Weather Trends

This first chapter was an introduction to the following projects of the Data Analyst Nanodegree.

The project of this chapter was about weather trends - it required (atleast) the following steps:
* Extract data from a database using a SQL query
* Calculate a moving average
* Create a line chart 

I analyzed local and global temperature data and compared the temperature trends in three german cities to overall global temperature trends. After a bit of data cleaning I created a function, which is supposed to handle all the tasks that are needed to plot the data - for example calculating the linear trend and calculating the rolling average. Also the function has some options for the visualization to play around with.

**Key findings**: the average global temperature is increasing, with an also increasing tempo and Berlin is the only city in Germany in this dataset which has a higher average temperature than the global average.

![Global Weather Trend](https://github.com/DataLind/Udacity-Data-Analyst-Nanodegree/blob/master/global_weather_trend.png)

### P1: Investigate a Dataset (Gapminder World Dataset)

This chapter was all about the data analysis process as whole. From gathering to cleaning, assessing and wrangling to exploring and visualizing the data over the programming workflow and communication was everything included. 

This project involved therefore also all steps needed in a typical data analysis process. This includes posing questions, gather, wrangle and clean data and communicate answers to the questions assisted through visualizations and statistics. 

Out of the project:

> This project will examine datasets available at Gapminder. To be more specific, it will take a closer look on the life expectancy of the population from different countries and the influences from other variables. It will also take a look on the development of these variables over time.
>
>**What is Gapminder?**
"Gapminder is an independent Swedish foundation with no political, religious or economic affiliations. Gapminder is a fact tank, not a think tank. Gapminder fights devastating misconceptions about global development." (https://www.gapminder.org/about-gapminder/)

Here we were confronted with the full joy of a real-life dataset: from hard-to-analyze structure, missing, messy, dirty data to real and - after finally being done with data wrangling - the reward of interesting insights. 

![Life Expectancy To Income 2018](https://github.com/DataLind/Udacity-Data-Analyst-Nanodegree/blob/master/life_expectancy_to_income_2018.png)

### P2: Analyze A/B Test Results

This chapter was filled with *a lot* of information. We talked about: Data Types, Notation, Mean, Standard Deviation, Correlation, Data Shapes, Outliers, Bias, Dangers, Probability and Bayes, Distributions, Central Limit Theorem, Bootstrapping, Confidence Intervals, Hypothesis Testing, A/B Tests, Linear Regression, Logistic Regression and more.. *heavy breathing

To goal of the project in this chapter was then to get experience with A/B testing and the difficulties and drawbacks of it. At first we learned what A/B testing is all about - including different metrics like the Click Through Rate (CTR) and how to analyze these metrics properly. We also learned about the drawbacks like the novelty effect or change aversion. 

Overall we brought everything we've learned together to analyze this A/B test properly.

![Sampling distribution](https://github.com/DataLind/Udacity-Data-Analyst-Nanodegree/blob/master/sampling_dist.png)

### P3: Gather, Clean and Analyze Twitter Data (WeRateDogs™ (@dog_rates))

This chapter was a deep dive into the data wrangling part of the data analysis process. We learned about the difference between messy and dirty data, how tidy data is defined, about the assessing, defining, cleaning and testing process and more. Also we talked about many different file types and different methods of gathering data. 

In this project we had to deal with the reality of dirty and messy data (again). We gathered data from different sources (for example the Twitter API), identified issues with the dataset in terms of tidiness and quality and solved this problems while documenting each step. At the end followed the exploration of the data. 

![Mean of retweets](https://github.com/DataLind/Udacity-Data-Analyst-Nanodegree/blob/master/mean_of_retweets_per_month-year_combination.png)

### P4: Communicate Data Findings

![Relative Userfrequncy by gender and area](https://github.com/DataLind/Udacity-Data-Analyst-Nanodegree/blob/master/rel_userfreq_by_gender_and_area.png)
Notes to be added:

- chart junk
- data types
- univariate, bivariate, multivariate
- use of color
- data ink/ratio
- lie factor

## License

* <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"> Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>

<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">
	<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" />
</a>
