from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def DrinksList(request):
    if request.method == 'GET':
        # get all the drinks
        drinks = Drink.objects.all()
        # serialize them, many=true to serial all the list
        serializer = DrinkSerializer(drinks, many=True)
        # return json
        return JsonResponse({'drinks': serializer.data}, safe=False)

    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


