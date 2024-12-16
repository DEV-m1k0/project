from rest_framework import serializers
from models.models import *


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentComment
        fields = "__all__"


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentComment
        fields = ["text", "author"]