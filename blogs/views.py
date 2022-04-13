from django.shortcuts import render

# Create your views here.
def index(request):
    blogs = ['Первый блог','Второй блог','Третий блог','Четвертый блог']
    context = {
        'blogs' : blogs
    }
    return render(request, 'blogs/index.html', context)

def user(request):
    # Как передавать переменные!
    user_name = 'Алексей'
    user_age = 27
    context = {
        'user_name': user_name,
        'user_age': user_age
    }
    return render(request, 'blogs/user.html', context)