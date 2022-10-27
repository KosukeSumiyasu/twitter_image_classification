import pandas as pd

# csvへの保存
def save_data(path, data):
	labels=[
		'tweet_id',
		'text',
		'good_num',
		'retweet_num',
		'user_id',
		'user_name',
		'image_url'
		]
	df = pd.DataFrame(data, columns=labels)
	df.to_csv(path, encoding='utf-8', index=False)