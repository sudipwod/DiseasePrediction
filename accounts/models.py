from django.db import models



class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70, default="")
    subject = models.CharField(max_length=100, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

