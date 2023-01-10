numTweets="99"
user="elonmusk"


fullURL=https://api.twitter.com/2/tweets/search/recent?query=from:$user"&max_results="$numTweets"&tweet.fields=public_metrics,created_at"

curl $fullURL --header 'Authorization: Bearer '$BEARER_TOKEN > elon_tweets.json

#echo $BEARER_TOKEN

wait

jq . elon_tweets.json > elon_tweets_pretty.json


