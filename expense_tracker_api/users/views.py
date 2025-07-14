from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer 



# CBV for registration
class RegisterView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'User registered'}, status=201)
        return Response(serializer.errors, status= 400)
    
# CBV for Logout
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        return Response({'message': 'Logged out on client'}, status=status.HTTP_200_OK)
        
