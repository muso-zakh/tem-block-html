from django.shortcuts import render

def home(request):
    return render(
        request=request,
        template_name='Home.html'
    )

def history(request):
    return render(
        request=request,
        template_name='History.html',
    ) 

def frem(request):
    return render(
        request=request,
        template_name='Frameworks.html',
    )

def libraries(request):
    return render(
        request=request,
        template_name='Libraries.html'
    )

def Documentation(request):
    return render(
        request=request,
        template_name='Documentation.html'
    )