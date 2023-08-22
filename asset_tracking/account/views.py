from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.views import APIView


class SignupViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User successfully created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        #basic authentication
        user = authenticate(username=username, password=password)

        if user:
            return JsonResponse({'message': 'Authentication successful', 'user_id': user.id})
        else:
            return JsonResponse({'message': 'Authentication failed'}, status=401)
