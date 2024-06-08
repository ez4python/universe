from django.urls import path

from apps.views import DashboardListView, RegisterFormView, CustomLoginView, NewDetailView

urlpatterns = [
    path('', DashboardListView.as_view(), name='base_dashboard_view'),
    path('news/<str:slug>', NewDetailView.as_view(), name='new_detail_view')
]

urlpatterns += [
    path('auth/register', RegisterFormView.as_view(), name='register_view'),
    path('auth/login', CustomLoginView.as_view(), name='login_view'),
]
