from telnetlib import STATUS
from timeit import repeat
from django.shortcuts import render
# modulos de DRF

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (RetrieveAPIView,ListAPIView)


class HelloWorld(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
    
        return Response(data="Estoy en el get", status=200) # respuesta del servicio
    def patch(self,request):
        return Response(data="Estoy en el partch", status=200) # respuesta del servicio
    def delete (self,request):
        return Response(data="Estoy en el delete", status=200) # respuesta del servicio
    def post(self, equest):
        return Response(data="Estoy en el post", status=200) # respuesta del servicio
    

#class HelloWorkOnlyGet(RetrieveAPIView):
class PEtLustAPIView(ListAPIView):
  def get(self, request): # verbo de la peticion como un metodo
    # logica asociada al endpoint
        return Response(data="Mi lista de mascota", status=200) # respuesta del servicio    
    
class PetAPIView(RetrieveAPIView):
    def get(self, request): # verbo de la peticion como un metodo
    # logica asociada al endpoint
        return Response(data="Estoy en el get de petApiview", status=200) # respuesta del servicio


class PersonApiView(APIView):
    def get(self,request):
        return Response(data= "Estoy en el get del PersonApiView",status=200)
    def patch(self,request):
        return Response(data= "Estoy en el get del PersonApiView",status=200)
    def delete(self,request):
        return Response(data= "Estoy en el get del PersonApiView",status=200)
    def post(self,request):
        return Response(data= "Estoy en el get del PersonApiView",status=200)



class PetApiView(APIView):
    def get(self,request):
        return Response(data= "Estoy en el get del PetApiView",status=200)
    def patch(self,request):
        return Response(data= "Estoy en el get del PetApiView",status=200)
    def delete(self,request):
        return Response(data= "Estoy en el get del PetApiView",status=200)
    def post(self,request):
        return Response(data= "Estoy en el get del PetApiView",status=200)