from django.db import models


class Group(models.Model):
    FUCKULT = (
        ('ФІ', '0'),
        ('ФІТ', '1'),
        ('ФІЕТ', '2'),
        ('ФІКТ', '3'),
    )


    id = models.IntegerField(primary_key=True, unique=True)
    group = models.CharField(max_length=20, unique=True)
    fuck = models.CharField(choices=FUCKULT, max_length=4)
    subgroups = models.SmallIntegerField()
    class Meta:
       managed = False
       db_table = 'groups'

class User(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    subgroup = models.SmallIntegerField()

class Teacher(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    full_name = models.CharField(max_length=150)
    rating = models.IntegerField(default=0)
    count = models.IntegerField(default=0)

class Lesson(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    lesson = models.CharField(max_length=300)


class Timetable(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    day_week = models.CharField(max_length=10)
    lesson_time = models.CharField(max_length=20)
    lesson_num = models.SmallIntegerField()
    week = models.CharField(max_length=10)
    subgroup = models.SmallIntegerField()
    lesson_kind = models.CharField(max_length=10)
    group_id = models.ForeignKey('Group', on_delete=models.CASCADE)
    lesson_id = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    teacher_id = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True)