
def check_user(username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    if user.is_staff:
        return True
    else:
        return False
