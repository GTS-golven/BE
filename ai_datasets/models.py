from django.db import models


# Create your models here.
class DataSetVideo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.created


class Output(models.Model):
    speed = models.IntegerField()
    angle = models.DecimalField(max_digits=5, decimal_places=2)
    spinAxis = models.DecimalField(max_digits=5, decimal_places=2)
    distance = models.IntegerField
    rpm = models.IntegerField
    dataSetVideo = models.ForeignKey(DataSetVideo, on_delete=models.CASCADE, related_name='outputs')


class ResultData(models.Model):
    time = models.IntegerField()
    output = models.ForeignKey(Output, on_delete=models.CASCADE, related_name='resultData')


class CoordinatesOutput(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    resultData = models.ForeignKey(ResultData, on_delete=models.CASCADE, related_name='coordinatesOutputs')


class Input(models.Model):
    time = models.IntegerField()
    dataSetVideo = models.ForeignKey(DataSetVideo, on_delete=models.CASCADE, related_name='inputs')


class CoordinatesInput(models.Model):
    x1 = models.IntegerField()
    x2 = models.IntegerField()
    y1 = models.IntegerField()
    y2 = models.IntegerField()
    input = models.ForeignKey(Input, on_delete=models.CASCADE, related_name='coordinatesInputs')
