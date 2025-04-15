from datetime import timezone
import stripe
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    get_object_or_404,
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from course.models import Course, Lessons
from course.serializers import CourseSerializer, LessonsSerializer
from users.permissions import IsModer, IsOwner


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="description from swagger_auto_schema via method_decorator"))
class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.action in ["create"]:
            self.permission_classes = (~IsModer,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsModer | IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (IsOwner | ~IsModer,)
        return super().get_permissions()


class LessonsViewSet(ModelViewSet):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
    permission_classes = (~IsModer, IsAuthenticated)


class LessonsCreateApiView(CreateAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
    permission_classes = (IsAuthenticated,)


class LessonsListAPIView(ListAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


class LessonsRetrieveAPIView(RetrieveAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
    permission_classes = (IsAuthenticated, IsModer | IsOwner)


class LessonsUpdateAPIView(UpdateAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
    permission_classes = (IsAuthenticated, IsModer | IsOwner)


class LessonsDestroyAPIView(DestroyAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
    permission_classes = (IsAuthenticated, IsOwner | ~IsModer)
