from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import *
from .serializers import *


class ExpensesView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]
    @swagger_auto_schema(
        request_body=ExpenseSerializer,
        responses={201: ExpenseSerializer}
    )

    def post(self,request): # For creating an expense
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
            "message": "Expense saved",
            "expense": serializer.data
        }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "Invalid inputs, please try again",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'start_date',
                openapi.IN_QUERY,
                description="Start date (YYYY-MM-DD)",
                type=openapi.TYPE_STRING,
                format='date'
            ),
            openapi.Parameter(
                'end_date',
                openapi.IN_QUERY,
                description="End date (YYYY-MM-DD)",
                type=openapi.TYPE_STRING,
                format='date'
            )
        ],
        responses={200: ExpenseSerializer(many=True)}
    )
    
    def get(self, request):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        queryset = Expense.objects.filter(user=request.user)
        if start_date:
            queryset = queryset.filter(date__gte=start_date)
        if end_date:
            queryset = queryset.filter(date__lte=end_date)
        serializer = ExpenseSerializer(queryset, many=True)
        return Response(serializer.data)



class AnalyticsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request): # For overall Analytics

        data = Expense.objects.all()
        serializer = ExpenseSerializer(data,many=True)
        return Response(serializer.data)

