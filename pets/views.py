from rest_framework.views import APIView, Request, Response, status
from django.forms.models import model_to_dict
from pets.serializers import PetSerializer
from .models import Pet
from django.shortcuts import get_object_or_404

class PetsView(APIView):
    
        def post(self, req:Request) -> Response:
            serializer = PetSerializer(data = req.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, 201)
            
        def get(self, req:Request) -> Response:
            pets = Pet.objects.all()
            serializer = PetSerializer(pets, many=True)
            return Response(serializer.data, 200)


class PetsDetails(APIView):
       
        def get(self, request: Request, pet_id: int) -> Response:
            pet = get_object_or_404(Pet, id=pet_id)
            serializer = PetSerializer(pet)
            return Response(serializer.data)

        def patch(self, request: Request, pet_id: int) -> Response:
            pet = get_object_or_404(Pet, id=pet_id)
            serializer = PetSerializer(pet, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data)
        
        def delete(self, request: Request, pet_id: int) -> Response:
            pet = get_object_or_404(Pet, id=pet_id)
            pet.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)