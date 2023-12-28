from django.db import models

class DragonType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Dragon(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    type = models.ForeignKey(DragonType, on_delete=models.CASCADE, related_name="dragons")
    fire_breathing = models.BooleanField(default=False)
    wing_span = models.FloatField(help_text="Wing span in meters")

    def __str__(self):
        return self.name

class Treasure(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    guarded_by = models.ForeignKey(Dragon, on_delete=models.SET_NULL, null=True, related_name="treasures")

    def __str__(self):
        return self.name

