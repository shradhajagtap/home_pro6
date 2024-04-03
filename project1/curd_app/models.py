from django.db import models


class CJC(models.Model):
    COURSE = [("Python", "Python"), ("Java", "Java"), ("C", "C"), ("C+", "C+")]
    stu_first_name = models.CharField(max_length=20)
    stu_last_name = models.CharField(max_length=20)
    stu_qualification = models.CharField(max_length=20)
    course = models.CharField(max_length=20, choices=COURSE)
    stu_address = models.CharField(max_length=20)


