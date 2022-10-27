# IMPORT
import tweepy
import time 
import urllib.request, urllib.error
import pandas as pd
import argparse
from parser import parse_option, config
from util import save_data


# Twitterの画像をダウンロードするクラス
class imageDownloader(object):
	def __init__(self, args):
		# initilize
		super(imageDownloader, self).__init__()
		self.args = args
		self.set_api()
		
	# 画像やツイートをダウンロード
	def run(self):
		# 1. twitterページを指定数取得
		# 2. ページ内のツイートのうち、キーワードがあるtweetのみ取得
		# 3. 画像URLを取得
		# 4. ダウンロード実行
		self.max_id = None # ページを跨ぐ検索対象IDの初期化
		all_data = []
		for page in range(self.args.search_pages_number):
			ret_url_list, tweet_data = self.search(self.args.search_name , self.args.per_page_number)
			all_data.extend(tweet_data)
			for url in ret_url_list:
				print('OK ' + url)
				self.download(url)
			time.sleep(0.1) # TimeOut防止
		save_data(args.sample_file, all_data)

	# apiの設定
	def set_api(self):
		auth = tweepy.OAuthHandler(self.args.consumer_key, self.args.consumer_secret)
		auth.set_access_token(self.args.access_token_key, self.args.access_token_secret)
		self.api = tweepy.API(auth)

	# ツイートの検索
	def search(self, target, rpp):
		ret_url_list = []
		tweet_data = []
		try:
			# 検索実行
			if self.max_id:
				# q: query, rpp: ツイート数, max_id: より小さい（古い）IDを持つステータスのみを返す
				res_search = self.api.search_tweets(q=target, lang='en', rpp=rpp, max_id=self.max_id)
			else:
				res_search = self.api.search_tweets(q=target, lang='en', rpp=rpp)
			
			for result in res_search:
				if 'media' not in result.entities: continue
				for media in result.entities['media']:
					# print(media)
					url = media['media_url_https']
					if url not in ret_url_list: 
						ret_url_list.append(url)
						tweet_data.append([
							result.id,
							result.text,
							result.favorite_count, 
							result.retweet_count, 
							result.user.id, 
							result.user.name,
							url
						])
			# 検索済みidの更新し、より古いツイートを検索させる
			self.max_id = result.id
			# 検索結果の返却
			return ret_url_list, tweet_data
		except Exception as e:
			self.error_catch(e)

	# 画像のダウンロード
	def download(self, url):
		url_orig = '%s?name=orig' % url
		path = self.args.image_dir + "/" + url.split('/')[-1]
		try:
			response = urllib.request.urlopen(url=url_orig)
			with open(path, "wb") as f:
				f.write(response.read())
		except Exception as e:
			self.error_catch(e)

	# エラー処理
	def error_catch(self, error):
		print("NG ", error)

def main(args):
	try:
		downloader = imageDownloader(args)
		downloader.run()
	except KeyboardInterrupt:
		# Ctrl-Cで終了
		pass

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	args = parse_option()
	args = config(args)
	main(args)