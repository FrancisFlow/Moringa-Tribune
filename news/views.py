from django.shortcuts import render, redirect
from .models import Article
import datetime as dt
from django.http import Http404
# Create your views here.

def news_today(request):
    date=dt.date.today()
    news=Article.todays_news()
    return render(request, 'all-news/today-news.html', {"date":date, "news":news})


def news_of_day(request):
    date=dt.date.today()
    day=convert_dates(date)
    return render(request, 'all-news/today-news.html', {"date":date, "day":day})
def convert_dates(dates):
    #function that gets the weekday number for the date
    day_number=dt.date.weekday(dates)
    days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]

    #Returning the actual day of the week
    day=days[day_number]
    return day
def past_days_news(request, past_date):
    #Converts data from the string Url

    try:
        #Converts data from the sting Url
        date=dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        #Raise 404 error when ValueError is thrown
        raise Http404()
        assert False
    if date==dt.date.today():
        return redirect(news_today)
    news=Article.days_news(date)
    return render(request, 'all-news/past-news.html', {{"date":date, "news":news}})

    # date=dt.datetime.striptime(past_date, '%Y-%m-%d').date()

    # day= convert_dates(date)
   
def search_results(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term=request.GET.get("article")
        searched_articles=Article.search_by_title(search_term)
        message=f"{search_term}"

        return render(request, 'all-news/search.html', {"message":message, "articles":searched_articles})
    else:
        message="You haven't searched for any term"
        return render(request, 'all-news/search.html', {"message":message})

def article(request, article_id):
    try:
        article=Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404()
    return render(request, "all-news/article.html", {"article":article})
