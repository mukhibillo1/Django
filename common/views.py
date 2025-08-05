from django.shortcuts import render
from django.views import View
from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from helpers import pagination
from common import models, serializers
from rest_framework.views import APIView
from datetime import date, timedelta
from django.db.models import Sum
from rest_framework.response import Response
from django.db.models import Q
from .models import Visitor, PageCount  # <-- model nomlaringga qarab to'g'rilang



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


class ContactCreateAPIView(generics.CreateAPIView):
    queryset = models.ContactCreate.objects.all()
    serializer_class = serializers.ContacCreateSerializer
    parser_classes = (MultiPartParser, )




class TeamsListAPIView(generics.ListAPIView):
    queryset = models.Teams.objects.all()
    serializer_class = serializers.TeamsSerializer
    pagination_class = pagination.ByThree

class SearchAPIView(generics.ListAPIView):
    serializer_class = serializers.NewsListSerializer
    def get_queryset(self):
        object_list = models.News.objects.all()
        search = self.request.GET.get("search", None)
        if search:
            object_list = object_list.filter(Q(title__icontains=search) | Q(category__title__icontains=search)| Q(content__icontains=search) | Q(slug__icontains=search) | Q(region__title__icontains=search) | Q(tags__title__icontains=search))
        return object_list



class SiteStatsAPIView(APIView):
    def get(self, request):
        today = date.today()
        month_ago = today - timedelta(days=30)

        daily_visitors = Visitor.objects.filter(date=today).count()
        monthly_visitors = Visitor.objects.filter(date__gte=month_ago).count()

        daily_pageviews = PageCount.objects.filter(date=today).aggregate(total=Sum('count'))['total'] or 0
        monthly_pageviews = PageCount.objects.filter(date__gte=month_ago).aggregate(total=Sum('count'))['total'] or 0

        return Response({
            'daily_visitors': daily_visitors,
            'monthly_visitors': monthly_visitors,
            'daily_pageviews': daily_pageviews,
            'monthly_pageviews': monthly_pageviews,
        })
