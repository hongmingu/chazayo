


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

    filename = "%s_%s_%s.%s" % ("300", now_date, uuid.uuid4().hex, ext)
    # uuid 는 랜덤 스트링 뽑아낼 때 씀

    return os.path.join('photo/%s/userphoto' % usernum, filename)

def get_file_path_50(instance, filename):
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

    filename = "%s_%s_%s.%s" % ("50", now_date, uuid.uuid4().hex, ext)
    # uuid 는 랜덤 스트링 뽑아낼 때 씀

    return os.path.join('photo/%s/userphoto' % usernum, filename)