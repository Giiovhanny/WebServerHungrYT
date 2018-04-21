from django.db import models

# Create your models here.

class Calification (models.Model):
    id_delivery= models.IntegerField()
    score= models.IntegerField()
    comment= models.IntegerField()

    def __string__(self):
        return (self.id_delivery
                + "\nScore: " + self.score
                +"\nComment: " + self.comment
                )
