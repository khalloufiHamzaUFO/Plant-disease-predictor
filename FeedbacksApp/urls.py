from django.urls import path
from .views import (
    feedback_list,
    FeedbackUpdateView,
    FeedbackDeleteView,
    feedback_all
)

urlpatterns = [
    path('feedbacks/<int:prevention_id>/', feedback_list, name='feedback_list'),
    path('feedback/all/', feedback_all, name='feedback_all'),  # New URL pattern
    path('feedback/update/<int:pk>/', FeedbackUpdateView.as_view(), name='feedback_update'),
    path('feedback/delete/<int:pk>/', FeedbackDeleteView.as_view(), name='feedback_delete'),


]
