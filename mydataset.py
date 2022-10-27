import torch
import cv2
from PIL import Image
import os

# データセットのクラス
class MyDataset(torch.utils.data.Dataset):
	def __init__(self, args, df, transform):
		self.args = args
		self.df = df
		self.transform = transform
		self.image_url = df['image_url']

	def __len__(self):
		return len(self.image_url)

	def __getitem__(self, idx):
		path = os.path.join(self.args.image_dir, self.image_url[idx].split('/')[-1])
		img = cv2.imread(path, cv2.IMREAD_COLOR | cv2.IMREAD_IGNORE_ORIENTATION)
		img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
		if self.transform is not None:
			img = self.transform(img)
		return img, self.df[idx:idx+1].values[0].tolist()