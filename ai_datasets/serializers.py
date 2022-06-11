from rest_framework import serializers
from .models import *


class CoordinatesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoordinatesInput
        fields = ('id', 'x1', 'x2', 'y1', 'y2')


class InputSerializer(serializers.ModelSerializer):
    coordinatesInput = CoordinatesInputSerializer(many=False, required=True)

    def create(self, validated_data):
        coordinatesInput_data = validated_data.pop('coordinatesInput')
        coordinatesInput = CoordinatesInput.objects.create(**coordinatesInput_data)
        return Input.objects.create(**validated_data)

    class Meta:
        model = Input
        fields = ('id', 'time', 'coordinatesInput')


class CoordinatesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoordinatesOutput
        fields = ('id', 'x', 'y', 'z')


class ResultDataSerializer(serializers.ModelSerializer):
    coordinatesOutput = CoordinatesOutputSerializer(many=False, required=True)

    def create(self, validated_data):
        coordinatesOutput_data = validated_data.pop('coordinatesOutput')
        coordinatesOutput = CoordinatesOutput.objects.create(**coordinatesOutput_data)
        return ResultData.objects.create(**validated_data)

    class Meta:
        model = ResultData
        fields = ('id', 'time', 'coordinatesOutput')


class OutputSerializer(serializers.ModelSerializer):
    resultData = ResultDataSerializer(many=True, required=True)

    def create(self, validated_data):
        resultData_data = validated_data.pop('resultData')
        output = Output.objects.create(**validated_data)
        for resultData in resultData_data:
            ResultData.objects.create(output=output, **resultData)
        return output

    class Meta:
        model = Output
        fields = ('id', 'speed', 'angle', 'spinAxis', 'distance', 'rpm', 'resultData')


class DataSetVideoSerializer(serializers.ModelSerializer):
    inputs = InputSerializer(many=True, required=True)
    outputs = OutputSerializer(many=False, required=True)

    def create(self, validated_data):
        inputs_data = validated_data.pop('inputs')
        outputs_data = validated_data.pop('outputs')

        data_set = DataSetVideo.objects.create(**validated_data)
        for input_data in inputs_data:
            Input.objects.create(**input_data)
        for output_data in outputs_data:
            Output.objects.create(**output_data)
        return validated_data

    class Meta:
        model = DataSetVideo
        fields = ('id', 'inputs', 'outputs', 'created', 'updated')
