from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect


def login(request):
	return render(request, 'seller/login.html')


def facebook_login(request):
	params = _verify_signature(request.COOKIES)
	if params:
		user = authenticate(uid=params['user'])
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect(settings.LOGIN_REDIRECT_URL, {}, ())
			else:
				# Disabled account, redirect and notify?
				return redirect('/', {}, ())
		else:
			# Invalid user, redirect and notify?
			return redirect('/', {}, ())
	elif request.user.is_authenticated ():
		return redirect(settings.LOGIN_REDIRECT_URL, {}, ())
	else:
		return redirect('/', {}, ())
