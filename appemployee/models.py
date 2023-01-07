from django.db import models

class DepartmentModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Department Table'

class EmployeeModel(models.Model):
    level_types = (
        ('Genin', 'Genin'),
        ('Chunin', 'Chunin'),
        ('Jonin', 'Jonin'),
    )

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,null=True)
    employee_level = models.CharField(max_length=20, default="Genin", choices=level_types)
    employee_position = models.ForeignKey(DepartmentModel, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Employee Table'  # Easy readable tablename - verbose_name

    def __str__(self):
        return self.name

