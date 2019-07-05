from django.db import models

class Make(models.Model):
    name = models.CharField(
            max_length=200,
            help_text='Enter a make of a car'
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Auto(models.Model) :
    nickname = models.CharField(
            max_length=200
    )
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)
    make = models.ForeignKey('Make', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname
