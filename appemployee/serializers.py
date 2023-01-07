from rest_framework import serializers
from appemployee.models import EmployeeModel,DepartmentModel
        
class EmployeeSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)
    employee_dept = serializers.CharField(source='employee_position.name',read_only=True)
    class Meta:
        model = EmployeeModel
        fields = ['id','name','email','employee_level','employee_position','employee_dept']

        # def to_representation(self, instance):
        #     rep = super(EmployeeSerializer, self).to_representation(instance)
        #     rep['EmpLevel'] = instance.EmpLevel
        #     rep['emp_dept'] = instance.emp_dept.DeptName
        #     print(rep)
        #     return rep