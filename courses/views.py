from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from . import models


class IndexView(TemplateView):
    template_name = 'index.html'


class ContactsView(TemplateView):
    template_name = 'contacts.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class CourseListView(ListView):
    model = models.Course
    template_name = "course_list.html"


class BranchListView(ListView):
    model = models.Branch
    template_name = "branch_list.html"

class PeopleListView(ListView):
    model = models.People
    template_name = "people_list.html"
