from django.shortcuts import render
from django.views import generic
from .models import EmployeeInfo, Project, Leave

# Create your views here.

def index(request):
    # Generate counts of some of the main objects
    num_employees = EmployeeInfo.objects.all().count()
    num_projects = Project.objects.all().count()
    num_general_employees = EmployeeInfo.objects.filter(employeeRole__exact='e').count()
    num_managers = EmployeeInfo.objects.filter(employeeRole__exact='m').count()
    num_HR = EmployeeInfo.objects.filter(employeeRole__exact='h').count()

    data = {
        'num_employees': num_employees,
        'num_projects': num_projects,
        'num_general_employees': num_general_employees,
        'num_managers': num_managers,
        'num_HR': num_HR
    }

    return render(request, 'index.html', data)

class EmployeeListView(generic.ListView):
    model = EmployeeInfo
    template_name = 'Employee/EmployeeInfo_list.html' 

class ProjectListView(generic.ListView):
    model = Project
    template_name = 'Employee/project_list.html'

class EmployeeDetailView(generic.DetailView):
    model = EmployeeInfo
    template_name = 'Employee/employee_detail.html'

class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'Employee/project_detail.html'