from rest_framework import generics
from .serializers import *
from models.models import *
from rest_framework.response import Response
from datetime import datetime
import random
from rest_framework.request import Request

# Create your views here.


class DocumentListApiView(generics.ListAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()


class CommentListApiView(generics.ListAPIView):
    queryset = DocumentComment.objects.all()
    serializer_class = CommentListSerializer

    def list(self, request, document_id: int, *args, **kwargs):
        try:
            comments = DocumentComment.objects.filter(document_id=document_id)
            response = {}
            for i in range(comments.count()):
                response[f"{i}"] = {
                    "document_id": comments[i].document_id.pk,
                    "text": comments[i].text,
                    "date_created": comments[i].date_created,
                    "date_updated": comments[i].date_updated,
                    "author": comments[i].author.pk
                }
            return Response(response)
        except:
            return Response({
                "timestamp": datetime.now(),
                "message": "Не найден документ с таким id",
                "errorCode": random.randint(1001, 9999)
            })


class CommentCreateApiView(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer
    queryset = DocumentComment.objects.all()

    def create(self, request: Request, document_id: int, *args, **kwargs):
        try:
            document = Document.objects.get(pk=document_id)
            if document:
                document.has_comment = True
                document.save()
                try:
                    employee = Employee.objects.get(pk=request.data['author'])
                    if employee:
                        comment = DocumentComment.objects.create(
                            document_id=document,
                            text=request.data["text"],
                            author=employee
                        )
                        print(comment)
                        return Response({
                            "document_id": document_id,
                            "date_created": comment.date_created,
                            "date_updated": comment.date_updated,
                            "author_id": employee.pk
                        })
                    else:
                        raise Exception()
                except:
                    return Response({
                        "timestamp": datetime.now(),
                        "message": "Такого сотрудника не существует",
                        "errorCo`de": random.randint(1001, 9999)
                    })
            else:
                raise Exception()
        except Exception as e:
            return Response({
                "timestamp": datetime.now(),
                "message": "Не найден документ с таким id",
                "errorCode": random.randint(1001, 9999)
            })
