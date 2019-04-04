
## P3: Analyze Twitter Data

### Prerequisites

Additional installations: 

* [Missingno](https://github.com/ResidentMario/missingno)
* [Tweepy](http://www.tweepy.org/)
* [Requests](http://docs.python-requests.org/en/master/)

## Project Overview

### Data Sources

**Name: WeRateDogs™ Twitter Archive (twitter-archive-enhanced.csv)**

- Source: Udacity
- Version: Latest (Download 09.02.2019)
- Method of gathering: Manual download

**Name: Tweet image predictions (image_predictions.tsv)**

- Source: Udacity
- Version: Latest (Download 09.02.2019)
- Method of gathering: Programmatical download via Requests

**Name: Additional Twitter data (tweet_json.txt)**

- Source: WeRateDogs™
- Version: Latest (Gathered 09.02.2019)
- Method of gathering: API via Tweepy

### Wrangling

**Cleaning steps:**

- Merge the tables together
- Drop the replies, retweets and the corresponding columns and also drop the tweets without an image or with images which don't display doggos
- Clean the datatypes of the columns
-Clean the wrong numerators - the floats on the one hand (replacement), the ones with multiple occurence of the pattern on the other (drop)
- Extract the source from html code
- Split the text range into two separate columns
- Remove the "None" out of the doggo, floofer, pupper and puppo column and merge them into one column
- Remove the wrong names of name column
- Reduce the prediction columns into two - breed and conf
- Clean the new breed column by replacing the "_" with a whitespace and make them all lowercase

### Summary

**Questions:**

> Based on the predicted, most likely dog breed: Which breed gets retweeted and favorited the most overall?
- The winner for our analysis was the labrador retriever.
> How did the account develop (speaking about number of tweets, retweets, favorites, image number and length of the tweets)?
- We found, that the number of tweets per month decreased, while the retweets and favorites show an uptrend. For the image numbers there is no clear trend visible, the length of the tweets got a little bit closer to the maximum of 130 in the second half of the dataset.
> Is there a pattern visible in the timing of the tweets?
- there are nearly no tweets at all between 5 and 15 'o clock . The most tweets are during the time from 0 - 4 and then again from 15 - 23 'o clock

### Authors

* Christoph Lindstädt
* Udacity

## License

* <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"> Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>

<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">
	<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" />
</a>

