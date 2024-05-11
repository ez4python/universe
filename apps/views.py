from django.views.generic import ListView, DetailView

from apps.models import New


class DashboardListView(ListView):
    queryset = New.objects.order_by('-id')
    template_name = 'base.html'
    context_object_name = 'news'


class NewDetailView(DetailView, ListView):
    template_name = 'detail.html'
    context_object_name = 'new_details'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = New.objects.order_by('-id')[:3]
        context['main_new'] = New.objects.filter(slug=self.slug_url_kwarg)
        return context
