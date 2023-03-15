"""View module for handling requests about events"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from checkoutapi.models import Property, CheckoutUser


class PropertyView(ViewSet):
    """rare property view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single property
        Returns:
            Response -- JSON serialized property
        """
        property = Property.objects.get(pk=pk)
        serializer = PropertySerializer(property)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        """Handle GET requests to get all categories
        Returns:
            Response -- JSON serialized list of categories
        """
        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        """Handle Post operations
            returns
                Response -- JSON serialized property instance with 
                status code 201"""
        checkout_user = CheckoutUser.objects.get(user=request.auth.user)

        property = Property.objects.create(
            user=checkout_user,
            name=request.data["name"],
            address=request.data["address"],
            size=request.data["size"],
            image_url=request.data["image_url"]
        )
        serializer = PropertySerializer(property)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a property
        Returns:
            Response -- Empty body with 204 status code
        """

        property = Property.objects.get(pk=pk)
        property.name = request.data["name"]
        property.address = request.data["address"]
        property.size=request.data["size"]
        property.image_url = request.data["image_url"]

        checkout_user = CheckoutUser.objects.get(user=request.auth.user)
        property.user = checkout_user
        
        property.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        property = Property.objects.get(pk=pk)
        property.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)



class PropertySerializer(serializers.ModelSerializer):
    """JSON serializer for propertys
    """
    class Meta:
        model = Property
        fields = ('id', 'user', 'name', 'address', 'size', 'image_url',)

