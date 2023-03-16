from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from checkoutapi.models import Cleaner


class CleanerView(ViewSet):
    def list(self, request):
        """Handle GET requests to get all categories
        Returns:
            Response -- JSON serialized list of categories
        """
        cleaners = Cleaner.objects.all()
        serializer = CleanerSerializer(cleaners, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CleanerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaner
        fields = ('id', 'name', 'phone_number', )

