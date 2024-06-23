from rest_framework import views, status
from rest_framework.response import Response
from .models import Foodtruck
from .serializers import FoodtruckSerializer

class NearbyFoodtrucksView(views.APIView):
    """
    API endpoint that returns a list of nearby food trucks based on provided latitude and longitude.
    """

    def get(self, request):
        """
        Handles GET requests to fetch nearby food trucks.
        """
        # Retrieve latitude and longitude from query parameters
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')

        # Check if latitude and longitude are provided
        if not latitude or not longitude:
            return Response({'error': 'Latitude and longitude are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Convert latitude and longitude to float
            latitude = float(latitude)
            longitude = float(longitude)
        except ValueError:
            # Return an error response if conversion fails
            return Response({'error': 'Invalid latitude or longitude values.'}, status=status.HTTP_400_BAD_REQUEST)

        # Define a simple radius for nearby food trucks (~0.01 degrees, roughly 1 km)
        nearby_radius = 0.01

        # Filter food trucks within the defined radius
        nearby_trucks = Foodtruck.objects.filter(
            latitude__range=(latitude - nearby_radius, latitude + nearby_radius),
            longitude__range=(longitude - nearby_radius, longitude + nearby_radius)
        )

        # Serialize the queryset to JSON format
        serializer = FoodtruckSerializer(nearby_trucks, many=True)

        # Return the serialized data in the response
        return Response(serializer.data)
