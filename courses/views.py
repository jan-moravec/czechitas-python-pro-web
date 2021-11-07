from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

class ContactsView(TemplateView):
    template_name = 'contacts.html'
