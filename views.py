from flask import Flask,render_template,request,redirect,url_for
# from app import app
from newsapi import NewsApiClient


app =Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')
# bcc news page

@app.route('/bbc')
def bbc():
    newapi = NewsApiClient(api_key="7497b8a3477240c181b4b85f120d9d24") 
    topheadlines = newapi.get_top_headlines(sources="bbc-news")
    articles = topheadlines['articles']


    news = []
    description = []
    link = []
    image = []
    time = []
    content = []

    for i in range(len(articles)):
        myarticles = articles [i]
        news.append(myarticles['title'])
        description.append(myarticles['description'])
        link.append(myarticles['url'])
        image.append(myarticles['urlToImage'])
        time.append(myarticles['publishedAt'])
        content.append(myarticles ['content'])

    my_list = zip( news,description,link,image,time,content)

    return render_template('bbc.html',context=my_list)

    # cnn news page
@app.route('/cnn')
def cnn():
    newapi = NewsApiClient(api_key="7497b8a3477240c181b4b85f120d9d24") 
    topheadlines = newapi.get_top_headlines(sources="CBC-News")
    articles = topheadlines['articles']


    news = []
    description = []
    link = []
    image = []
    time = []
    content = []

    for i in range(len(articles)):
        myarticles = articles [i]
        news.append(myarticles['title'])
        description.append(myarticles['description'])
        link.append(myarticles['url'])
        image.append(myarticles['urlToImage'])
        time.append(myarticles['publishedAt'])
        content.append(myarticles ['content'])

    my_list = zip( news,description,link,image,time,content)

    return render_template('cnn.html',context=my_list)

    # google news
@app.route('/google')
def google():
    newapi = NewsApiClient(api_key="7497b8a3477240c181b4b85f120d9d24") 
    topheadlines = newapi.get_top_headlines(sources="google-news")
    articles = topheadlines['articles']


    news = []
    description = []
    link = []
    image = []
    time = []
    content = []

    for i in range(len(articles)):
        myarticles = articles [i]
        news.append(myarticles['title'])
        description.append(myarticles['description'])
        link.append(myarticles['url'])
        image.append(myarticles['urlToImage'])
        time.append(myarticles['publishedAt'])
        content.append(myarticles ['content'])

    my_list = zip( news,description,link,image,time,content)

    return render_template('google.html',context=my_list)
    




if __name__=='__main__':
    app.run (debug = True)

