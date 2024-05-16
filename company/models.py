from django.db import models

class Teachers(models.Model):
    teacher_name = models.CharField(max_length=25)
    subject = models.CharField(max_length=50)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        return self.image.url

    def __str__(self):
        return f"{self.id}--{self.teacher_name}"
