import json
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def readJSON():
	file = open("elon_tweets.json")

	data = json.load(file)
	x = pd.DataFrame()

	for i in data['data']:
#		print('id: ', i['id'],'date: ', i['created_at'], 'likes: ', i['public_metrics']['like_count'],'impressions: ', i['public_metrics']['impression_count'])
		row_vector = pd.DataFrame([[i['id'], i['created_at'], i['public_metrics']['like_count'], i['public_metrics']['impression_count']]], columns=['id', 'date', 'likes', 'impressions'])
		x = pd.concat([x, row_vector])
	file.close()

	dates = x.loc[:, 'date']
	likes = x.loc[:, 'likes']


	fig, ax = plt.subplots()
	ax.plot(dates, likes)

	every_nth = 20
	for n, label in enumerate(ax.xaxis.get_ticklabels()):
		if n % every_nth != 0:
			label.set_visible(False)

	plt.show()

	print(likes)

def fetchStockPrices():

	tsla = yf.Ticker('TSLA')

	hist = tsla.history(period='max')

	data = pd.DataFrame(hist)
	print(data.index)

	x = data.index
	y = data.loc[:,'Open']

	fig, ax = plt.subplots()
	ax.plot(x, y)

	plt.show()

def graphTrend():

	x = np.linspace(0, 10, 100)
	y = 4 + 2 * np.sin(2 * x)

	fig, ax = plt.subplots()
	ax.plot(x, y, linewidth=2.0)

	plt.show()

readJSON()
