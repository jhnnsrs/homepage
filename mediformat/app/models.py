from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Name(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Disease(models.Model):
    name = models.ForeignKey(Name)

    def __str__(self):
        return self.name.__str__()


class Symptom(models.Model):
    name = models.CharField(max_length=100) # ie headache
    abstract = models.CharField(max_length=100) # a painful sensation affecting the head
    description = models.CharField(max_length=300)
    associateddiseases = models.ManyToManyField(Disease)
    # MANY TO MANY RELATIONSHIP BUT WITH LIKELINESS

    def __str__(self):
        return self.name

class Location(models.Model):
    description = models.CharField(max_length=100) # tibia
    basicdescription = models.CharField(max_length=100) # lower foot

class Pain(Symptom):
    location = models.ForeignKey(Location)