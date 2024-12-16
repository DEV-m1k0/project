from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("s", DocumentListApiView.as_view()),
    path("/<int:document_id>/Comment", CommentCreateApiView.as_view()),
    path("/<int:document_id>/Comments", CommentListApiView.as_view()),
]
