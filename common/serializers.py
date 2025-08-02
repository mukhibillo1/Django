from rest_framework import serializers

from common import models



class AddsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Add
        fields = ["file_url", "url"]


class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewsCategory
        fields = ["id", "title"]


class NewsTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewsTag
        fields = ["id", "title"]


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = ["id", "title"]

class NewsListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    region = serializers.StringRelatedField()
    class Meta:
        model = models.News
        fields = ["slug", "title", "cover_url", "category", "region", "published_at"]


class NewsDetailSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    region = serializers.StringRelatedField()
    class Meta:
        model = models.News
        fields = ["slug", "title", "cover_url", "video_url", "file_url", "content", "category", "region", "published_at", "time_to_read", "views"]




