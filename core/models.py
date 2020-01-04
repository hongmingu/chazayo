from django.contrib.auth.models import User
from django.db import models

# Create your models here.

MAN = 2002
WOMAN = 2001

SEX_CHOICES = (
    (MAN, "man"),
    (WOMAN, "woman"),
)

APPEARANCE_CHOICES = (
    (MAN, "man"),
    (WOMAN, "woman"),
)


class InfoBase(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nickname = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=30, unique=True)
    telephone = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)

    name = models.CharField(max_length=30, unique=True)
    sex = models.PositiveSmallIntegerField(choices=SEX_CHOICES, default=2002)
    is_married = models.BooleanField(null=True, blank=True, default=False)
    born = models.PositiveSmallIntegerField(default=1950)
    country = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    school_base = models.CharField(max_length=255, null=True, blank=True)  # 학력 - 졸업유형

    school_kinder = models.CharField(max_length=255, null=True, blank=True)
    school_kinder_in = models.CharField(max_length=255, null=True, blank=True)
    school_kinder_out = models.CharField(max_length=255, null=True, blank=True)
    school_middle = models.CharField(max_length=255, null=True, blank=True)
    school_middle_in = models.CharField(max_length=255, null=True, blank=True)
    school_middle_out = models.CharField(max_length=255, null=True, blank=True)
    school_high = models.CharField(max_length=255, null=True, blank=True)
    school_high_in = models.CharField(max_length=255, null=True, blank=True)
    school_high_out = models.CharField(max_length=255, null=True, blank=True)
    school_university = models.CharField(max_length=255, null=True, blank=True)
    school_university_in = models.CharField(max_length=255, null=True, blank=True)
    school_university_out = models.CharField(max_length=255, null=True, blank=True)
    school_graduate = models.CharField(max_length=255, null=True, blank=True)
    school_graduate_in = models.CharField(max_length=255, null=True, blank=True)
    school_graduate_out = models.CharField(max_length=255, null=True, blank=True)

    appearance = models.PositiveSmallIntegerField(choices=APPEARANCE_CHOICES, default=2002)
    appearance_explanation = models.TextField(max_length=5000, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "UserUsername for %s" % self.user


class ArmyPhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    file_50 = models.ImageField(null=True, blank=True, default=None, upload_to=get_file_path, max_length=1000)
    file_300 = models.ImageField(null=True, blank=True, default=None, upload_to=get_file_path_50, max_length=1000)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "UserPhoto pk: %s, username: %s" % (self.pk, self.user.userusername.username)


class FamilyPhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    file_50 = models.ImageField(null=True, blank=True, default=None, upload_to=get_file_path, max_length=1000)
    file_300 = models.ImageField(null=True, blank=True, default=None, upload_to=get_file_path_50, max_length=1000)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "UserPhoto pk: %s, username: %s" % (self.pk, self.user.userusername.username)


class SchoolPhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    file_50 = models.ImageField(null=True, blank=True, default=None, upload_to=get_file_path, max_length=1000)
    file_300 = models.ImageField(null=True, blank=True, default=None, upload_to=get_file_path_50, max_length=1000)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "UserPhoto pk: %s, username: %s" % (self.pk, self.user.userusername.username)


class SchoolInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    school_kinder = models.CharField(max_length=255, null=True, blank=True)
    school_kinder_in = models.CharField(max_length=255, null=True, blank=True)
    school_kinder_out = models.CharField(max_length=255, null=True, blank=True)
    school_middle = models.CharField(max_length=255, null=True, blank=True)
    school_middle_in = models.CharField(max_length=255, null=True, blank=True)
    school_middle_out = models.CharField(max_length=255, null=True, blank=True)
    school_high = models.CharField(max_length=255, null=True, blank=True)
    school_high_in = models.CharField(max_length=255, null=True, blank=True)
    school_high_out = models.CharField(max_length=255, null=True, blank=True)
    school_university = models.CharField(max_length=255, null=True, blank=True)
    school_university_in = models.CharField(max_length=255, null=True, blank=True)
    school_university_out = models.CharField(max_length=255, null=True, blank=True)
    school_graduate = models.CharField(max_length=255, null=True, blank=True)
    school_graduate_in = models.CharField(max_length=255, null=True, blank=True)
    school_graduate_out = models.CharField(max_length=255, null=True, blank=True)

    story = models.TextField(max_length=5000, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "UserUsername for %s" % self.user


class FamilyInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    break_address = models.CharField(max_length=255, null=True, blank=True)
    break_type = models.CharField(max_length=255, null=True, blank=True)
    break_date = models.DateField(max_length=255, null=True, blank=True) #없는건 1월, 1일로 지정.

    story = models.TextField(max_length=5000, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "UserUsername for %s" % self.user


class ArmyInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    army_sort = models.CharField(max_length=255, null=True, blank=True)
    army_in = models.DateField(max_length=255, null=True, blank=True)
    army_out = models.DateField(max_length=255, null=True, blank=True) #없는건 1월, 1일로 지정.
    army_address = models.CharField(max_length=255, null=True, blank=True) #없는건 1월, 1일로 지정.

    army_name = models.CharField(max_length=255, null=True, blank=True)

    story = models.TextField(max_length=5000, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "UserUsername for %s" % self.user
