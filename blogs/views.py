from django.shortcuts import render

# Create your views here.
def index(request):
    blogs = [{'name': 'Первый блог', 'autor': {'name': 'admin'}, 'publication_date': '16.04.2022'},
    {'name': 'Второй блог', 'autor': {'name': 'user'}, 'publication_date': '16.04.2020'},
    {'name':'Третий блог', 'autor': {'name': 'guest'}, 'publication_date': '16.04.2021'},
    {'name':'Четвертый блог', 'autor': {'name': 'master'}, 'publication_date': '16.04.2019'}]

    context = {
        'blogs' : blogs
    }
    return render(request, 'blogs/index.html', context)

def user(request):
    # Как передавать переменные!
    user_data =['Алексей, 27 лет.', 'Кыргызстан, г.Кара-Балта', 'Высшее Образование']
            
            
    context = {
            'user_data': user_data

    }
    
    return render(request, 'blogs/user.html', context)

def apple(request):
   
    
    return render(request, 'blogs/apple.html')


def production(request):

    return render(request, 'blogs/production.html')

def price(request):
    return render(request, 'blogs/price.html')