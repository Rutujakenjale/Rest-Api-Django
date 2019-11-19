from django.shortcuts import render,HttpResponse
from .models import Article
from rest_framework import viewsets
from .serializers import ArticleSerializer
from rest_framework import routers, serializers, viewsets
from rest_framework.views import APIView







class ArticleView(viewsets.ModelViewSet):
	queryset=Article.objects.all()
	serializer_class=ArticleSerializer


# def home(request):
# 	article_list=Article.objects.all()
	
# 	return render (request,'home.html',{"article_list":article_list})

