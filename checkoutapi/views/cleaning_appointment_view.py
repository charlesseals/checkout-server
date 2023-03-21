from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from checkoutapi.models import CleaningAppointment, CheckoutUser, Cleaner, Property


class CleaningAppointmentView(ViewSet):
    # def retrieve(self, request, pk):
    #     cleaningAppointment = CleaningAppointment.objects.get(pk=pk)
    #     serializer = CleaningAppointmentSerializer(cleaningAppointment)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # def list(self, request):
    #     if "user" in request.query_params:
    #         checkoutUser = CheckoutUser.objects.get(user=request.query_params['user'])
    #         property = Property.objects.get(user_id=checkoutUser.id)
    #         cleaningAppointments = CleaningAppointment.objects.filter(property_id=property.id)
    #     else:
    #         cleaningAppointments = CleaningAppointment.objects.all()
    #     serializer = CleaningAppointmentSerializer(cleaningAppointments, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)


    def list(self, request):
        user_id = request.query_params.get('user')
        co_user_id = CheckoutUser.objects.get(user_id = user_id)
        if co_user_id is not None:
            appointments = CleaningAppointment.objects.filter(property__user_id=co_user_id)
        else:
            appointments = CleaningAppointment.objects.all()

        serializer = CleaningAppointmentSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        """Handle POST operations
            Returns
                Response -- JSON serialized post instance
        """
        cleaner = Cleaner.objects.get(pk=request.data["cleaner"])
        property = Property.objects.get(pk=request.data["property"])

        cleaningAppointments = CleaningAppointment.objects.create(
            date_time=request.data["date_time"],
            progress=request.data["progress"],
            cleaner= cleaner,
            property=property
        )
        serializer = CleaningAppointmentSerializer(cleaningAppointments)
        return Response(serializer.data, status=status.HTTP_201_CREATED)




class CleanerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaner
        fields = ( 'id', 'name', 'phone_number',)

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ( 'id', 'name', 'address', 'size', 'image_url',)


class CleaningAppointmentSerializer(serializers.ModelSerializer):
    cleaner = CleanerSerializer()
    property = PropertySerializer()
    class Meta:
        model = CleaningAppointment
        fields = ('id', 'cleaner', 'property', 'date_time', 'progress',)