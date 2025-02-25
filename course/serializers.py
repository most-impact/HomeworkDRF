from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from course.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    count_lessons = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ("id", "title", "description", "preview", "lessons", "count_lessons")

    def get_count_lessons(self, course):
        return course.lessons.count()


class LessonDetailSerializer(ModelSerializer):
    count_lessons_with_same_course = SerializerMethodField()

    def get_count_lessons_with_same_course(self, lesson):
        return Lesson.objects.filter(course=lesson.reference).count()

    class Meta:
        model = Lesson
        fields = ("title", "description", "get_count_lessons_with_same_course")
