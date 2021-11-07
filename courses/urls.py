from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contacts', views.ContactsView.as_view(), name='contacts'),
    path('about', views.AboutView.as_view(), name='about'),
    path('courses', views.CourseListView.as_view(), name='course_list'),
    path('branches', views.BranchListView.as_view(), name='branch_list'),
    path('people', views.PeopleListView.as_view(), name='people_list'),
    path('course/<int:pk>', views.CourseDetailView.as_view(), name='course_detail'),
    path('branch/<int:pk>', views.BranchDetailView.as_view(), name='branch_detail'),
    path('application', views.ApplicationCreateView.as_view(), name='application_create'),
    path('application_confirmation', views.ApplicationConfirmation.as_view(), name='application_confirmation'),
    path('register_person', views.PersonRegister.as_view(), name='person_register'),
    path('register_success', views.PersonRegisterSuccess.as_view(), name='person_register_success'),
]
