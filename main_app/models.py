from django.db import models
from datetime import datetime, date

# Create your models here.

MEALS= (
    ('B','Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')




)





class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
    



class Feeding(models.Model): 
    date = models.DateTimeField("Feeding Date and Time")
    meal = models.CharField(
    max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
      
        return f"{self.get_meal_display()} on {self.date}"
    class Meta:
        ordering = ['-date']


class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return self.name