from django.db.models import fields
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
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


class CourseDetailView(DetailView):
    model = models.Course
    template_name = "course_detail.html"


class BranchDetailView(DetailView):
    model = models.Branch
    template_name = "branch_detail.html"


class ApplicationCreateView(CreateView):
    model = models.Application
    template_name = "application_create.html"
    fields = ["email", "first_name", "last_name", "motivation", "course"]
    success_url = reverse_lazy("application_confirmation")


class ApplicationConfirmation(TemplateView):
    template_name = 'application_confirmation.html'


class PersonRegister(CreateView):
    model = models.People
    template_name = "person_register.html"
    fields = ["first_name", "family_name", "email"]
    success_url = reverse_lazy("person_register_success")

class PersonRegisterSuccess(TemplateView):
    template_name = 'person_register_success.html'

