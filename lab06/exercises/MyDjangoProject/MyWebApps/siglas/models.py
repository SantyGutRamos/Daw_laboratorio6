from django.db import models


class Users(models.Model):
    username = models.CharField(
        max_length=50,
        db_column='username'
    )

    email = models.CharField(
        max_length=100,
        db_column='email'
    )

    password = models.CharField(
        max_length=255,
        db_column='password'
    )

    status = models.BooleanField(
        default=True,
        db_column='status'
    )

    created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
        db_column='created'
    )

    modified = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
        db_column='modified'
    )

    created_0 = models.ForeignKey(
        'self',
        models.DO_NOTHING,
        db_column='created_id',
        blank=True,
        null=True
    )

    modified_0 = models.ForeignKey(
        'self',
        models.DO_NOTHING,
        db_column='modified_id',
        related_name='users_modified_0_set',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username


class Student(models.Model):
    names = models.CharField(
        max_length=100,
        db_column='names'
    )

    fathersurname = models.CharField(
        max_length=100,
        db_column='fathersurname'
    )

    mothersurname = models.CharField(
        max_length=100,
        db_column='mothersurname'
    )

    gender = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        db_column='gender'
    )

    address = models.TextField(
        blank=True,
        null=True,
        db_column='address'
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        db_column='phone'
    )

    note = models.TextField(
        blank=True,
        null=True,
        db_column='note'
    )

    user = models.ForeignKey(
        'Users',
        models.DO_NOTHING,
        blank=True,
        null=True,
        db_column='user_id'
    )

    status = models.BooleanField(
        default=True,
        db_column='status'
    )

    created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
        db_column='created'
    )

    modified = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
        db_column='modified'
    )

    created_0 = models.ForeignKey(
        'Users',
        models.DO_NOTHING,
        db_column='created_id',
        related_name='students_created_0_set',
        blank=True,
        null=True
    )

    modified_0 = models.ForeignKey(
        'Users',
        models.DO_NOTHING,
        db_column='modified_id',
        related_name='students_modified_0_set',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = 'students'
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return f"{self.fathersurname} {self.mothersurname}, {self.names}"


class Courses(models.Model):
    coursename = models.CharField(
        max_length=150,
        db_column='coursename'
    )

    credits = models.IntegerField(
        db_column='credits'
    )

    description = models.TextField(
        blank=True,
        null=True,
        db_column='description'
    )

    status = models.BooleanField(
        default=True,
        db_column='status'
    )

    created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
        db_column='created'
    )

    modified = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
        db_column='modified'
    )

    created_0 = models.ForeignKey(
        'Users',
        models.DO_NOTHING,
        db_column='created_id',
        blank=True,
        null=True
    )

    modified_0 = models.ForeignKey(
        'Users',
        models.DO_NOTHING,
        db_column='modified_id',
        related_name='courses_modified_0_set',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = 'courses'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.coursename


class CoursesStudents(models.Model):
    student = models.ForeignKey(
        'Student',
        models.DO_NOTHING,
        db_column='student_id'
    )

    course = models.ForeignKey(
        'Courses',
        models.DO_NOTHING,
        db_column='course_id'
    )

    enrollmentdate = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
        db_column='enrollmentdate'
    )

    status = models.BooleanField(
        default=True,
        db_column='status'
    )

    created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
        db_column='created'
    )

    modified = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
        db_column='modified'
    )

    created_0 = models.ForeignKey(
        'Users',
        models.DO_NOTHING,
        db_column='created_id',
        blank=True,
        null=True
    )

    modified_0 = models.ForeignKey(
        'Users',
        models.DO_NOTHING,
        db_column='modified_id',
        related_name='coursesstudents_modified_0_set',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = 'courses_students'
        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollments'
        unique_together = (('course', 'student'),)

    def __str__(self):
        return f"{self.student} - {self.course}"