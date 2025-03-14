from django.shortcuts import render
from .models import Interview
from .serializers import InterviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

# Create your views here.

# @api_view(["GET"])
# def fetach_interviews(request):
#     all_post = Interview.objects.all()
#     serialized_data = InterviewSerializer(all_post, many=True)
#     return Response(serialized_data.data)


# @api_view(["GET"])
# def api_post_detail(request, id):
#     post_detail = Interview.objects.get(id=id)
#     serialized_detail = InterviewSerializer(post_detail)
#     return Response(serialized_detail.data)

class FetchInterviews(ListCreateAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    pagination_class = PageNumberPagination


class InterviewDetail(RetrieveAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    lookup_field = "id"