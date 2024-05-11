from django.urls import path

from apps.views import DashboardListView

urlpatterns = [
    path('', DashboardListView.as_view(), name='base_dashboard_page'),
    path('news/<str:slug>', DashboardListView.as_view(), name='new_detail_page')
]
