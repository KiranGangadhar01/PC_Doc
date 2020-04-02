from django.views.generic import TemplateView

#Creating what the user wants to see
class HomeView(TemplateView):
    template_name = 'index.html'
