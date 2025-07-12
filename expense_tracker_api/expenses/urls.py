from django.urls import path
from .views import AnalyticsView, ExpensesView

urlpatterns = [
    path('expenses/', ExpensesView.as_view()),
    path('expenses/analytics/', AnalyticsView.as_view())
]