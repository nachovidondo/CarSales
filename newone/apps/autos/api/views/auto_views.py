from django.utils.module_loading import autodiscover_modules
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from apps.autos.api.serializers.auto_serializers import CarSerializer

class CarListCreateAPIVIew(generics.ListCreateAPIView):
    serializer_class = CarSerializer
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(estado = True)
    def post(self,request):
        auto = self.serializer_class(data =request.data)
        if auto.is_valid():
            auto.save()
            return Response({'message':'Elemento Creado correctamente'},status =status.HTTP_201_CREATED)
        return Response ({'message':'Error al crear elemento'},status=status.HTTP_409_CONFLICT)
    
class CarRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CarSerializer
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(estado =True)
    
class CarDestroyAPIView(generics.DestroyAPIView):
    serializer_class = CarSerializer
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(estado =True)
    def delete(self,request,pk =None):
        auto = self.get_queryset().filter(id = pk ).first()
        if auto:
            auto.estado = False
            auto.save()
            return Response({'message':'Elemento eliminado correctamente!'},status = status.HTTP_200_OK)
        return Response ({'message':'Error al intentar eliminar'},status  = status.HTTP_400_BAD_REQUEST)
    
    
class CarUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CarSerializer
    def get_queryset(self,pk=None):
        return self.get_serializer().Meta.model.objects.filter(estado = True).filter(id = pk).first()
    def patch(self,request,pk=None):
        if self.get_queryset(pk):
            auto_serializer = self.serializer_class(self.get_queryset(pk))
            
            return Response(auto_serializer.data,status= status.HTTP_202_ACCEPTED)
        return Response({'message':'Error al editar'}, status = status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk=None):
        if self.get_queryset(pk):
            auto_serializer= self.serializer_class(self.get_queryset(pk),data = request.data)
            if auto_serializer.is_valid():
                auto_serializer.save()
                return Response({'message':'Editado Correctamente'},status = status.HTTP_200_OK)
            return Response(auto_serializer.errors,status = status.HTTP_409_CONFLICT)
        
        
    