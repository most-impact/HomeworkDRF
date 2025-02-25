from django.urls import path
from rest_framework.routers import SimpleRouter
from course.views import CourseViewSet, LessonCreateApiView, LessonUpdateApiView, LessonDestroyAPIView, LessonListApiView, LessonRetrieveAPIView
from course.apps import CourseConfig

app_name = CourseConfig.name


router = SimpleRouter()
router.register('', CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListApiView.as_view(), name='lessons_list'),
    path("lessons/<int:pk>", LessonRetrieveAPIView.as_view(), name='lessons_retrieve'),
    path("lessons/create/", LessonCreateApiView.as_view(), name='lessons_create'),
    path("lessons/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name='lessons_destroy'),
    path("lessons/<int:pk>/update/", LessonUpdateApiView.as_view(), name='lessons_update'),
]


urlpatterns += router.urls