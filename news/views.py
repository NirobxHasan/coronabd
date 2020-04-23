from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


pl_source = requests.get('https://www.prothomalo.com/topic/করোনা-বাংলাদেশ/').text
pl_soup = BeautifulSoup(pl_source,'lxml')
pl_articles = pl_soup.find_all('div',class_='col')
pl_heading_list = []
pl_link_list = []
for pl_article in pl_articles:
    try:
        pl_headline = pl_article.find('div',class_='info').h2.text
        pl_link = pl_article.a['href']
        pl_news_link = f'https://www.prothomalo.com{pl_link}'
       
    except Exception as e:
        pl_headline =None
        pl_news_link =None
    pl_heading_list.append(pl_headline)
    pl_link_list.append(pl_news_link)
        
           


shamakal_source = requests.get('https://samakal.com/corona/').text
shamakal_soup = BeautifulSoup(shamakal_source,'lxml')
sk_articles = shamakal_soup.find_all('div',class_='col-md-6 flex-col')
sk_heading_list = []
sk_link_list = []
for sk_article in sk_articles:
    try:
        sk_headline = sk_article.find('div',class_='media-body').h4.text
        sk_link = sk_article.find('div',class_='media news-content child-cat-list').a['href']
        sk_news_link_split = sk_link.split('/')[5]
        sk_news_link = f'https://samakal.com/bangladesh/article/{sk_news_link_split}/'
    except Exception as e:
        sk_headline=None
        sk_news_link=None
    sk_heading_list.append(sk_headline)
    sk_link_list.append(sk_news_link)    
    
pl_list = zip(pl_heading_list, pl_link_list)
sk_list = zip(sk_heading_list, sk_link_list)
def news(request):
    context={
        'pl_list':pl_list,
        'sk_list':sk_list,
        'pl_heading_list':pl_heading_list,
        'pl_link_list': pl_link_list,
        'sk_heading_list':sk_heading_list,
        'sk_link_list': sk_link_list,
    } 
    return render(request, 'news/news.html',context)