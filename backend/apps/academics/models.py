from django.db import models
from django.conf import settings

# Create your models here.

class Faculty(models.Model):
    name=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE,related_name="department")
    name=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(unique=True)

    class Meta:
        constraints=[
            models.UniqueConstraint(
                fields=["faculty","name"],
                name="unique_department_per_faculty"
            )
        ]
    def __str__(self):
        return self.name

class Level(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE,related_name="level")
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(unique=True)

    class Meta:
        constraints=[
            models.UniqueConstraint(
                fields=["department","name"],
                name="unique_level_per_department"
            )
        ]

    def __str__(self):
        return self.name

class Semester(models.Model):
    level=models.ForeignKey(Level,on_delete=models.CASCADE,related_name="semester")
    name=models.CharField(max_length=100,unique=True)

    class Meta:
        constraints=[
            models.UniqueConstraint(
                fields=["level","name"],
                name="unique_semester_per_level"
            )
        ]

    def __str__(self):
        return self.name

class Course(models.Model):
    semester=models.ForeignKey(Semester,on_delete=models.CASCADE,related_name="course")
    title=models.CharField(max_length=100,unique=True)
    code=models.CharField(max_length=20)

    class Meta:
        constraints=[
            models.UniqueConstraint(
                fields=["semester","title","code"],
                name="unique_course_per_semester"
            )
        ]

    def __str__(self):
        return f"{self.code} - {self.title}"

class Material(models.Model):
    course=models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='course'
    )
    title=models.CharField(
        max_length=100
    )
    description=models.TextField(
        blank=True,
        null=True,
    )
    file=models.FileField(
        upload_to="materials/"
    )
    uploaded_by=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT, 
        related_name="uploaded_materials"
    )

    uploaded_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
