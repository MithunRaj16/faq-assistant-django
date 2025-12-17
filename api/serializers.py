
from rest_framework import serializers
from .models import FAQ, Category, Tag, User

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class FAQSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = FAQ
        fields = '__all__'
