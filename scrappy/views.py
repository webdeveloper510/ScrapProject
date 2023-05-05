from rest_framework.response import Response
from rest_framework.views import APIView
from bs4 import BeautifulSoup
import requests
from .models import *
from .serializers import *
import re
from django.utils import timezone


class ScrapDataView(APIView):
 def post(self, request, format=None):

    url = 'https://www.topgear.com/car-news'
    base_url = 'https://www.topgear.com'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url,headers=headers)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    article_data=[]

    compactgrid = soup.find_all('div', {'class': 'sc-beqWaB hipSxQ'})
    for article in compactgrid[0].find_all('article'):
        a_tag = article.find('a')
        img_tag = article.find('img')
        h3_tag = article.h3.text
        if a_tag and img_tag and h3_tag:
            article_data.append({
                'Link': a_tag['href'],
                'Image source': base_url+img_tag['src'],
                'Title':article.h3.text
            })

  
    for i in range(1,500):
       url = 'https://www.topgear.com/car-news?page='+str(i)
       base_url = 'https://www.topgear.com'
       headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
       response = requests.get(url,headers=headers)
       html_content = response.content
       soup = BeautifulSoup(html_content, 'html.parser')
      

       compactgrid = soup.find_all('div', {'class': 'sc-beqWaB hipSxQ'})
       for article in compactgrid[0].find_all('article'):
            a_tag = article.find('a')
            img_tag = article.find('img')
            h3_tag = article.h3.text
            if a_tag and img_tag and h3_tag:
                article_data.append({
                    'Link': a_tag['href'],
                    'Image source':base_url+img_tag['src'],
                    'Title':article.h3.text
                })
       
    # print(article_data)
    delete_Data=DataScraping.objects.all().delete()
    for data in article_data:
            title=data['Title']
            image_url=data['Image source']
            anchor=data['Link']
            scrappy=DataScraping.objects.create(image_url=image_url,anchor=anchor,title=title)
            serializers=DataScrapingSerializer(data=scrappy)
            scrappy.save()
            print(scrappy)
    return Response ({"message":"scrap data successfully","status":"200","data":article_data,"count":len(article_data)})