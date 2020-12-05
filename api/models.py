from django.db import models
import string
import  random
def generate_room_code():
    length = 10
    while True:
        code = ''.join(random.choice(string.ascii_uppercase,k=length))
        if Room.objects.filter(code=code).count() ==0:
            break
    return code

class Room(models.Model):
    code = models.CharField(max_length=20,default="main_room",unique=True)
    host = models.CharField(max_length=50,unique=True)
    guest_conrtol = models.BooleanField(default=False,null=False)
    skip_votes = models.IntegerField(null=False,default=1)
    created_at = models.DateTimeField(auto_now_add=True)


