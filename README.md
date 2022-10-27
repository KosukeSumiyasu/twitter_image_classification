# Twitterの画像探索

## 概要

ワードを入れると、そのワードと分類される画像付きのツイートを出力するよ！！！

## 動機

友人と会話している際に、パグとブルドッグの違いってなんだ？？となり、Twitterで調べた経験があります。その際にキャラクターやユーザーの名前に犬種が入っていたりで求めている犬のパグやブルドックが得られにくく、探すのに手間がかかりました。
この経験から、検索した名前と紐づく画像が出力される機能はニーズがありそう！と考えました。
個人的には、下手な検索機能よりもニーズは高そうだと感じました。（Googleとかで正しく検索した方がもちろん良い...）

<table>
<tr>
<td><img src="https://user-images.githubusercontent.com/77134522/198298559-252dff87-5f00-4c15-a94e-be67b76d5ccf.png" width="500"></td>
<td><img src="https://user-images.githubusercontent.com/77134522/198299375-e55f5d58-b53a-4a3c-90e6-462ff4b480d3.png" width="500"></td>
</tr>
</table>

<table>
<tr>
<td><img src="https://user-images.githubusercontent.com/77134522/198299748-12fcabf6-0a5d-440a-b23f-0483a551c7ff.png" width="500"></td>
<td><img src="https://user-images.githubusercontent.com/77134522/198299569-da755942-e838-478f-869d-43c8d5ae11cf.png" width="500"></td>
</tr>
</table>

## 使用した技術

[Twitter API](https://developer.twitter.com/ja/docs)

[学習済みモデル（今回はResNet34のアーキテクチャでImageNetを学習したモデルを使用）](https://github.com/rwightman/pytorch-image-models)

[ImageNetのラベルとインデックスをまとめたテキスト（検索ワードとインデックスを紐づけるために使用）](https://gist.github.com/yrevar/942d3a0ac09ec9e5eb3a)

[canva(スライド作成)](https://www.canva.com/)


## 使用方法

Twitter APIを用いるため、APIにアクセスするための4つのトークン(CONSUMER_KEY、CONSUMER_SECRET、ACCESS_TOKEN_KEY、ACCESS_TOKEN_SECRET)を入手する。


Twitterのデータ取得（ツイート内容や画像）

```
python get_twitter_image_url.py --consumer_key $CONSUMER_KEY --consumer_secret $CONSUMER_SECRET --access_token_key $ACCESS_TOKEN_KEY --access_token_secret $ACCESS_TOKEN_SECRET
```

画像を分類し、正解したツイートをcsvに出力

```
python image_classification.py
```
