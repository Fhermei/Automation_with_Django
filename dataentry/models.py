from django.db import models

class Student(models.Model):
    """
    The Student model represents a student with:
    - roll_no: A unique identifier for each student (maximum length 10).
    - name: The student's name (maximum length 20).
    - age: The student's age (integer value).
    """

    roll_no = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    # In this case, it returns the student's name.
    def __str__(self):
        return self.name

class Customer(models.Model):
    customer_name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.customer_name