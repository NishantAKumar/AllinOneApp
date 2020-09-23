import requests
import json


possible_news_domains = {'HEALTH':'http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=4bf0060d24ae4d4a874ecdd28c891b95', 'BUSINESS': 'http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=4bf0060d24ae4d4a874ecdd28c891b95', 'ENTERTAINMENT': 'http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=4bf0060d24ae4d4a874ecdd28c891b95', 'SCIENCE': 'http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=4bf0060d24ae4d4a874ecdd28c891b95', 'TECHNOLOGY': 'http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=4bf0060d24ae4d4a874ecdd28c891b95',	'SPORTS': 'http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=4bf0060d24ae4d4a874ecdd28c891b95', 'TOP_HEADLINES': 'http://newsapi.org/v2/top-headlines?country=in&apiKey=4bf0060d24ae4d4a874ecdd28c891b95'}

def NewsFinder(choice_of_news):
	news_des = []
	news_author = []
	news_title = []
	news_image = []
	news_article = []
	published_at = []
	each_domain = ''

	for each_domain in possible_news_domains:
		if each_domain == choice_of_news:
			break
	
	required_domain = each_domain
	req = requests.get(possible_news_domains[required_domain])
	data = req.json()
	for each in data["articles"]:
		news_title.append(each['title']),                                
		news_article.append(each['url']),
		news_image.append(each['urlToImage']),
		news_des.append(each['description']),
		news_author.append(each['author']),
		published_at.append(each['publishedAt'])

	data_packet = zip(news_title, news_author, news_des, news_image, published_at, news_article)

	return data_packet