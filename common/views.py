from django.shortcuts import render
from django.views import View
from rest_framework import generics

from helpers import pagination
from common import models, serializers


class BasicNewsListAPIView(generics.ListAPIView):
    def filter_queryset(self, queryset):
        category = self.request.query_params.get("category")
        region = self.request.query_params.get("region")
        if category:
            queryset = queryset.filter(category__id=category)
        if region:
            queryset = queryset.filter(region__id=region)
        return queryset

class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')


class AddListAPIView(generics.ListAPIView):
    queryset = models.Add.objects.all().order_by("?")[:1]
    serializer_class = serializers.AddsSerializer
    pagination_class = pagination.ByOne


class NewsCategoryListAPIView(generics.ListAPIView):
    queryset = models.NewsCategory.objects.all().order_by("-id")
    serializer_class = serializers.NewsCategorySerializer
    pagination_class = None


class NewsTagListAPIView(generics.ListAPIView):
    queryset = models.NewsTag.objects.all().order_by("-id")
    serializer_class = serializers.NewsTagSerializer
    pagination_class = None


class RegionListAPIView(generics.ListAPIView):
    queryset = models.Region.objects.all().order_by("-id")
    serializer_class = serializers.RegionSerializer
    pagination_class = None


class NewsListAPIView(BasicNewsListAPIView):
    queryset = models.News.objects.all().order_by("published_at")
    serializer_class = serializers.NewsListSerializer
    pagination_class = None 
    

class NewsRetrieveAPIView(BasicNewsListAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsDetailSerializer
    pagination_class = None
    lookup_field = "slug"

class SuperTopNewsListAPIView(BasicNewsListAPIView):
    queryset = models.News.objects.filter(type="supertop").order_by("-id")[:1]
    serializer_class = serializers.NewsListSerializer
    pagination_class = None 


class TopNewsListAPIView(BasicNewsListAPIView):
    queryset = models.News.objects.filter(type="top").order_by("-id")[:1]
    serializer_class = serializers.NewsListSerializer
    pagination_class = None 


class LatestNewsListAPIView(BasicNewsListAPIView):
    queryset = models.News.objects.all().order_by("published_at")
    serializer_class = serializers.NewsListSerializer
    pagination_class = pagination.PageTwelve
    lookup_field = "slug"


class ActualNewsListAPIView(BasicNewsListAPIView):
    queryset = models.News.objects.filter(type="actual").order_by("published_at")
    serializer_class = serializers.NewsListSerializer
    pagination_class = pagination.BySix


class VideoNewsListAPIView(BasicNewsListAPIView):
    queryset = models.News.objects.filter(type="video").order_by("published_at")
    serializer_class = serializers.NewsListSerializer
    pagination_class = pagination.PageTwelve


class InterviewNewsListAPIView(BasicNewsListAPIView):
    queryset = models.News.objects.filter(type="interview").order_by("published_at")
    serializer_class = serializers.NewsListSerializer
    pagination_class = pagination.BySix
    

class AnnouncementNewsListAPIView(BasicNewsListAPIView):
    queryset = models.News.objects.filter(type="announcement").order_by("published_at")
    serializer_class = serializers.NewsListSerializer
    pagination_class = pagination.BySix



class MotivationNewsListAPIView(generics.ListAPIView):
    queryset = models.News.objects.filter(type="motivation").order_by("published_at")
    serializer_class = serializers.NewsListSerializer
    pagination_class = pagination.ByFour


class PhotoNewsListAPIView(generics.ListAPIView):
    queryset = models.News.objects.filter(type="photo").order_by("published_at")
    serializer_class = serializers.NewsListSerializer
    pagination_class = pagination.ByEight


class EditorsChoiceNewsList(generics.ListAPIView):
    queryset = models.News.objects.filter(type="editors choice").order_by("published_at")
    serializer_class = serializers.NewsListSerializer
    pagination_class = pagination.ByThree



