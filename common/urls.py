from django.urls import path
from common import views
app_name = "common"

urlpatterns = [
    path("add/", views.AddListAPIView.as_view(), name="add-list"),
    path("news-category/", views.NewsCategoryListAPIView.as_view(), name="news-category-list"),
    path("news-tag/", views.NewsTagListAPIView.as_view(), name="news-tag-list"),
    path("region/", views.RegionListAPIView.as_view(), name="region-list"),
    path("news/", views.NewsListAPIView.as_view(), name="news-list"),
    path("news/<str:slug>", views.NewsRetrieveAPIView.as_view(), name="news-detail"),
    path("news/latest/", views.LatestNewsListAPIView.as_view(), name="latest-news-list"),
    path("news/top/", views.TopNewsListAPIView.as_view(), name="top-news-list"),
    path("news/supertop/", views.SuperTopNewsListAPIView.as_view(), name="supertop-news-list"),
    path("news/actual/", views.LatestNewsListAPIView.as_view(), name="latest-news-list"),
    path("news/video/", views.VideoNewsListAPIView.as_view(), name="video-news-list"),
    path("news/photo/", views.PhotoNewsListAPIView.as_view(), name="photo-news-list"),
    path("news/motivation/", views.MotivationNewsListAPIView.as_view(), name="motivation-news-list"),
    path("news/announcement/", views.AnnouncementNewsListAPIView.as_view(), name="announcement-news-list"),
    path("news/interview/", views.InterviewNewsListAPIView.as_view(), name="interview-news-list"),
    path("news/edtors-choice/", views.EditorsChoiceNewsList.as_view(), name="edtors-choice-news-list"),
]
