numTweets="26"
user="elonmusk"


fullURL=https://api.twitter.com/2/tweets/search/recent?query=from:$user"&max_results="$numTweets"&tweet.fields=public_metrics,created_at"

curl $fullURL --header 'Authorization: Bearer '$BEARER_TOKEN > results.json

echo $BEARER_TOKEN

jq . results.json

#jq .id results.json > id_results.json


