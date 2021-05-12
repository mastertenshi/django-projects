from django.db import models

from datetime import time


class Room(models.Model):
    name = models.CharField(max_length=200)
    room_number = models.IntegerField()
    floor = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} | Floor: {self.floor} | Room: {self.room_number}"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} | Time: {self.start_time} | Date: {self.date} || Room: {self.room.name}"
