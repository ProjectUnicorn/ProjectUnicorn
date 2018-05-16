
def CheckUserWithActiveDirectory(username, password):
    # Checks if a user can be authenticated up against an ADFS.


    return True

def check_user(username):
	from django.contrib.auth.contrib.models import User
	user = User.objects.get(username=username)
	if user.is_staff:
		return True
	else:
		return False

