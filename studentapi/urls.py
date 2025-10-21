from django.urls import path
from .views import StudentAPIView

urlpatterns = [
    path('api/view/students/', StudentAPIView.as_view(), name='student-list'),
    path('api/add/students/', StudentAPIView.as_view(), name='student-add'),
]