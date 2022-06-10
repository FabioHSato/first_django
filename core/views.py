from django.shortcuts import render, HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse('Hello Word')


def soma(request, num1, num2):
    return HttpResponse('<h1>Soma dos Numeros {} + {} = {}<h1>'.format(num1, num2, num1 + num2))
