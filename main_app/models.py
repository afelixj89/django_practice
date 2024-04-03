from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
MEALS= (
    ('B','Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')




)
    

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