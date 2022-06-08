from rest_framework import serializers
from .models import Videos
import os
import base64

class Base64ImageField(serializers.FileField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from mimetypes import guess_extension, guess_type
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Get the file name extension:
            file_extension = guess_extension(guess_type(data)[0])
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
        

            complete_file_name = "%s.%s" % (file_name, file_extension[1::], )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr
        print(decoded_file)
        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension
class VideoSerializer(serializers.ModelSerializer):
    video = Base64ImageField()

    class Meta:
        model = Videos
        fields = ('id', 'video', 'title', 'description', 'golfclub', 'golfbaan', 'datum', 'rpm', 'height', 'travel', 'angle', 
        'xas', 'airtime', 'simulatie')
