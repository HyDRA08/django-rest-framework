from appemployee.models import EmployeeModel, DepartmentModel
from appemployee.serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class EmployeeTable(APIView):

    def get(self,request):
        try:
            emp_obj = EmployeeModel.objects.select_related('employee_position').all()
            empserializer = EmployeeSerializer(emp_obj,many=True)
        except Exception as err:
            return Response(err)
        return Response(empserializer.data)
        

    def post(self,request):
        empserializer = EmployeeSerializer(data = request.data)
        if empserializer.is_valid():
            empserializer.save()
            return Response(empserializer.data,status=status.HTTP_201_CREATED)
        return Response(empserializer.errors,status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetails(APIView):

    def get_details(self,pk):
        try:
            return EmployeeModel.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request,pk):
        embObj = self.get_details(pk)
        serializerObj = EmployeeSerializer(embObj)
        return Response(serializerObj.data)

    def put(self,request,pk):
        empObj = self.get_details(pk)
        serializerObj = EmployeeSerializer(empObj,data = request.data)
        if serializerObj.is_valid():
            serializerObj.save()
            return Response(serializerObj.data,status=status.HTTP_200_OK)
        return Response(serializerObj.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        empObj = self.get_details(pk)
        empObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


