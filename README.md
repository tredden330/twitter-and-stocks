# twitter-and-stocks
Can stock prices be predicted from twitter data?

Using [Twitter's API](https://developer.twitter.com/en/docs/twitter-api) tweets can be accessed and analyzed programatically

Currently I am looking at how likes from [Elon Musk](https://twitter.com/elonmusk/with_replies) influence Tesla stock

## Current Program
- [x] Retrieves all tweets from Elon Musk in the past 7 days, including like_count, impression_count, and creation_time
- [x] Fetch Tesla high-low-closing stock value each day
- [ ] Normalize and graph data
- [ ] Fetch longer history
- [ ] Fetch more detailed stock data (stocks by minute/hour not by day)

### Limitations
- Currently only works on linux (specifically "curl" command in bash script does not work on windows)
- Twitter does not give access to full archive search for free accounts 
  - Looking in to [twitter timeline](https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/introduction) instead -- seems to allow 3,200 tweets from any user
