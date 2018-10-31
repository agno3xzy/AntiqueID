from django.shortcuts import render

def index(request):
	return render(request, 'personal/home.html')

def home(request):
	return render(request, 'personal/bootstrap_cover.html')

def contact(request):
	return render(request, 'personal/basic.html', {
		'content':['人俑','马俑','骆驼',]
	})