# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Courses(models.Model):
    coursename = models.CharField(max_length=150)
    credits = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # <-- Automático al crear
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)     # <-- Automático al editar
    created_0 = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_id', blank=True, null=True)  # Field renamed because of name conflict.
    modified_0 = models.ForeignKey('Users', models.DO_NOTHING, db_column='modified_id', related_name='courses_modified_0_set', blank=True, null=True)  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'courses'


class CoursesStudents(models.Model):
    student = models.ForeignKey('Student', models.DO_NOTHING) 
    course = models.ForeignKey('Courses', models.DO_NOTHING)
    enrollmentdate = models.DateTimeField(auto_now_add=True, blank=True, null=True) # <-- Automático al matricular
    status = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # <-- Automático al crear
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)     # <-- Automático al editar
    created_0 = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_id', blank=True, null=True)  # Field renamed because of name conflict.
    modified_0 = models.ForeignKey('Users', models.DO_NOTHING, db_column='modified_id', related_name='coursesstudents_modified_0_set', blank=True, null=True)  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'courses_students'
        unique_together = (('course', 'student'),)


class Student(models.Model):
    names = models.CharField(max_length=100)
    fathersurname = models.CharField(max_length=100)
    mothersurname = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # <-- Automático al crear
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)     # <-- Automático al editar
    created_0 = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_id', related_name='students_created_0_set', blank=True, null=True)  # Field renamed because of name conflict.
    modified_0 = models.ForeignKey('Users', models.DO_NOTHING, db_column='modified_id', related_name='students_modified_0_set', blank=True, null=True)  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'students'


class Users(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    status = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # <-- Automático al crear
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)     # <-- Automático al editar
    created_0 = models.ForeignKey('self', models.DO_NOTHING, db_column='created_id', blank=True, null=True)  # Field renamed because of name conflict.
    modified_0 = models.ForeignKey('self', models.DO_NOTHING, db_column='modified_id', related_name='users_modified_0_set', blank=True, null=True)  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'users'