from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employee/', views.EmployeeListView.as_view(), name='employee'),
    path('project/', views.ProjectListView.as_view(), name='project'),
    path('employee/<int:pk>', views.EmployeeDetailView.as_view(), name='EmployeeInfo-detail'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
]