from django.urls import path
from .views import *

urlpatterns = [
    path("all_interviews/", FetchInterviews.as_view(), name="interviews"),
    path("<int:id>/interview_detail/", InterviewDetail.as_view(), name="interview_detail")
]