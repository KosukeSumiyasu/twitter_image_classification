import os
import torch
from torchvision import transforms
import argparse
from parser import parse_option, config
import timm
from ast import literal_eval
import pandas as pd
from mydataset import MyDataset
from util import save_data

# 探索している名前と同一のimagenetのラベルを探索
def get_search_label(args):
	with open(args.class_txt, "r") as f:
		data = f.read()
	data = literal_eval(data)
	for k, v in data.items():
		if v == args.search_name:
			key = k
	return key

def set_transform(args):
	data_transform = {
		'val': transforms.Compose([
			transforms.Resize(224),
			transforms.CenterCrop(224),
			transforms.ToTensor(),
		])
	}
	return data_transform

def main(args):
	# ツイート内容を得る
	df = pd.read_csv(args.sample_file)

	# 画像分類の設定
	transform = set_transform(args)
	dataset = MyDataset(args, df, transform['val'])
	dataLoader = torch.utils.data.DataLoader(dataset, args.batch_size, shuffle=False)
	model = timm.create_model(model_name="resnet34", pretrained=True)
	model.eval()
	true_label = get_search_label(args)

	# 分類に正解するツイートを取得
	correct_data = []
	for data in dataLoader:
		# data -> images, labels
		images, tweet_data = data
		outputs = model(images)
		predict = outputs.argmax(dim=1)

		for label in predict:
			if label.item() == true_label:
				correct_data.append(([data.item() if type(data) == torch.Tensor else data[0] for data in tweet_data]))
	path = os.path.join(args.output_dir, args.search_name, 'correct.csv')

	# ツイートの保存
	save_data(path, correct_data)
	
		

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	args = parse_option()
	args = config(args)
	main(args)