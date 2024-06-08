from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView

from apps.forms import RegisterForm
from apps.mixins import NotLoginRequiredMixin
from apps.models import New, Category


class DashboardListView(ListView):
    queryset = New.objects.order_by('-id')
    template_name = 'index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class NewDetailView(DetailView):
    queryset = New.objects.all()
    template_name = 'detail.html'
    context_object_name = 'new'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class RegisterFormView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login_view')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CustomLoginView(NotLoginRequiredMixin, LoginView):
    template_name = 'register.html'
    next_page = 'base_dashboard_view'
