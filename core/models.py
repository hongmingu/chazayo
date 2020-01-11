
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

# -------------------------------------------------------------------------------------------------------------------------

# 가오정에서 쓰게 될 정보가 무엇인지, 어떤식으로 저장할지를 고민하는 단계가 필요함. 다양한 필드 용도가 있음. 필터랑 여기 공부도 필요할 것.
# 가오정에서 쓰게 될 모델은 무엇인지 상의하고 상의한 내용을 바탕으로 만들어가면 될거임 형 나중에 모델링 리셋하고 그럴때 제대로 안되면
# 검색해도 되지만 나한테 물어보면 그 때 더 알려줄거 있을거임. 우선은 여기서부터 views.py 에서 필터링하는 과정까지가 첫 학습 과정이 아닐까 싶음.
# 기본설명 끝~화이팅

# -------------------------------------------------------------------------------------------------------------------------

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


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    # 파일의 확장자를 빼낸다.
    usernum = instance.user.username
    # 그 인스턴스의 유저고유 ID number 를 가져온다.

    from django.utils.timezone import now
    now = now()
    # 현재시간을 가져온다.

    now_date = now.strftime('%Y-%m-%d-%H-%M-%S')

    # 현재시간을 스트링포맷으로 잡아준다.
    import uuid
    import os

    filename = "300_%s_%s.%s" % (now_date, uuid.uuid4().hex, ext)
    # uuid 는 랜덤 스트링 뽑아낼 때 씀

    return os.path.join('photo/%s/userphoto' % usernum, filename)
