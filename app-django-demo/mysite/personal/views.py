from django.shortcuts import render

def home(request):
	is_login = request.session.get('is_login', None)
	return render(request, 'personal/bootstrap_cover.html',locals())
