from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from .models import Login
from .serializers import LoginSerializer


class LoginView(
    APIView,
    UpdateModelMixin,
    DestroyModelMixin,
):

    def get(self, request, id=None):
        if id:
            try:
                queryset = Login.objects.get(id=id)
            except Login.DoesNotExist:
                # If the Login item does not exist, return an error response
                return Response({'errors': 'This Login item does not exist.'}, status=400)

            # Serialize Login item from Django queryset object to JSON formatted data
            read_serializer = LoginSerializer(queryset)
            
            return Response(read_serializer.data)

        else:
            # Get all Login items from the database using Django's model ORM
            queryset = Login.objects.all()

            # Serialize list of Logins item from Django queryset object to JSON formatted data
            read_serializer = LoginSerializer(queryset, many=True)

            # Return a HTTP response object with the list of Login items as JSON
            return Response(read_serializer.data)


    def post(self, request):
        # Pass JSON data from user POST request to serializer for validation
        create_serializer = LoginSerializer(data=request.data)

        # Check if user POST data passes validation checks from serializer
        if create_serializer.is_valid():

            # If user data is valid, create a new Login item record in the database
            login_item_object = create_serializer.save()

            # Serialize the new Login item from a Python object to JSON format
            read_serializer = LoginSerializer(login_item_object)

            # Return a HTTP response with the newly created Login item data
            return Response(read_serializer.data, status=201)

        # If the users POST data is not valid, return a 400 response with an error message
        return Response(create_serializer.errors, status=400)


    def put(self, request, id=None):
        try:
            # Check if the Login item the user wants to update exists
            login_item = Login.objects.get(id=id)
        except Login.DoesNotExist:
            # If the Login item does not exist, return an error response
            return Response({'errors': 'This Login item does not exist.'}, status=400)

        # If the Login item does exists, use the serializer to validate the updated data
        update_serializer = LoginSerializer(login_item, data=request.data)

        # If the data to update the Login item is valid, proceed to saving data to the database
        if update_serializer.is_valid():

            # Data was valid, update the Login item in the database
            login_item_object = update_serializer.save()

            # Serialize the Login item from Python object to JSON format
            read_serializer = LoginSerializer(login_item_object)

            # Return a HTTP response with the newly updated Login item
            return Response(read_serializer.data, status=200)
    
        # If the update data is not valid, return an error response
        return Response(update_serializer.errors, status=400)


    def delete(self, request, id=None):
        try:
            # Check if the Login item the user wants to update exists
            login_item = Login.objects.get(id=id)
        except Login.DoesNotExist:
            # If the Login item does not exist, return an error response
            return Response({'errors': 'This Login item does not exist.'}, status=400)

        # Delete the chosen Login item from the database
        login_item.delete()

        # Return a HTTP response notifying that the Login item was successfully deleted
        return Response(status=204)
