from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class EmployeeInfo(models.Model):
    employeeId = models.AutoField(
        primary_key=True
    )

    employeeName = models.CharField(
        max_length=50
    )

    availableRoles = (
        ('e', 'General Employee'),
        ('m', 'Manager'),
        ('h', 'Human Resource')
    )

    employeeRole = models.CharField(
        max_length=1,
        choices=availableRoles,
        default='e',
    )

    projectId = models.ForeignKey('Project', null=True, on_delete=models.RESTRICT, blank=True)
    
    managerId = models.ForeignKey('EmployeeInfo', null=True, on_delete=models.RESTRICT, blank=True)
    
    class Meta:
        ordering = ['employeeId']

    def __str__(self):
        return self.employeeName

    def get_absolute_url(self):
        return reverse('EmployeeInfo-detail', args=[self.employeeId])
    
class Project(models.Model):
    projectId = models.AutoField(primary_key=True)
    projectTitle = models.CharField(max_length = 100)
    dateOfStart = models.DateField(null= True, blank=True)

    def __str__(self):
        return self.projectTitle

    def get_absolute_url(self):
        return reverse('project-detail', args=[str(self.projectId)])
    
    class Meta:
        ordering = ['-dateOfStart']

class Leave(models.Model):
    leaveId = models.UUIDField(primary_key=True, default=uuid.uuid4)
    reason = models.TextField(max_length=100, blank=True, null=False)
    startDate = models.DateField(null=True, blank=True)
    endDate = models.DateField(null=True, blank=True)
    employeeId = models.ForeignKey(EmployeeInfo, null=True, on_delete=models.RESTRICT)

    def __UUID__(self):
        return self.leaveId