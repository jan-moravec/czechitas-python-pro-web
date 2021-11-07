from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contacts', views.ContactsView.as_view(), name='contacts'),
    path('about', views.AboutView.as_view(), name='about'),
    path('courses', views.CourseListView.as_view(), name='course_list'),
    path('branches', views.BranchListView.as_view(), name='branch_list'),
    path('people', views.PeopleListView.as_view(), name='people_list'),
]
