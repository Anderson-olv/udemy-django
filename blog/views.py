from django.http import HttpResponse

def blog(request):
    print('teste_blog')
    return HttpResponse('home do app')