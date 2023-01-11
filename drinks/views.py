from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def DrinksList(request):
    # get all the drinks
    drinks = Drink.objects.all()
    # serialize them, many=true to serial all the list
    serializer = DrinkSerializer(drinks, many=True)
    # return json
    return JsonResponse({'drinks': serializer.data}, safe=False)
    


