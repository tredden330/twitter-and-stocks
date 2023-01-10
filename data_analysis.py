import json
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def readJSON():
	file = open("results.json")

	data = json.load(file)
	x = pd.DataFrame()

	for i in data['data']:
		print('id: ', i['id'],'date: ', i['created_at'], 'likes: ', i['public_metrics']['like_count'],'impressions: ', i['public_metrics']['impression_count'])
		x = x.append({"id" : i['id'], "created_at" : i['created_at'], "likes" : i['public_metrics']['like_count'],'impressions' : i['public_metrics']['impression_count']}, ignore_index = True)
	file.close()

	print(x)

def fetchStockPrices():
	start_date = '2023-01-01'
	end_date = '2023-01-07'

	# Set the ticker
	ticker = 'TSLA'
	# Get the data
	data = yf.download(ticker, start_date, end_date)
	# Print the last 5 rows
	print(data)

def graphTrend():
	print("hi")
	x = np.linspace(0, 10, 100)
	y = 4 + 2 * np.sin(2 * x)

	fig, ax = plt.subplots()
	ax.plot(x, y, linewidth=2.0)

	plt.show()

readJSON()
