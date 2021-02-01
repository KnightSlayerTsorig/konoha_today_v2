from django.shortcuts import render
from main.models import Article


def news(request):
    a = Article.objects.all()
    upper_articles = a[:2]
    bottom_articles = a[2:]
    return render(request, 'main/news.html',
                  {
                      'upper_articles': upper_articles,
                      'bottom_articles': bottom_articles
                  })










