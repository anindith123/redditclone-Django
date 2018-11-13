from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup(request):
	if request.method == 'POST':
		if request.POST["password1"] == request.POST["password2"]:
			try:
				user = User.objects.get(username = request.POST['username'])
				return render(request, 'account/signup.html', {"error":"username already taken"})

			except User.DoesNotExist:
				user = User.objects.create_user(request.POST["username"], password = request.POST["password1"])
				login(request, user)
				return redirect('home')
		else:
			return render(request, 'account/signup.html', {"error":'passwords didnt match'})

	else:
		return render(request, 'account/signup.html')


def loginview(request):
	if request.method == 'POST':
		user = authenticate(username = request.POST['username'], password = request.POST['password1'])

		if user is not None:
			login(request,user)
			return redirect('home')
			if 'next' in request.POST:
				return redirect(request.POST['next'])
			return redirect('home')
		else:
			return render(request, 'account/login.html', {"error":"username and password ddidnot match"})

	else:
		return render(request, 'account/login.html')


def logoutview(request):
	if request.method == "POST":
		logout(request)
		return redirect('home')
