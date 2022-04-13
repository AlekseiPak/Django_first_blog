from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'blogs/index.html')

def name(request):
	return render(request, 'blogs/name.html')