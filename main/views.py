# from django.http import HttpResponse
# from django.shortcuts import render
# from django.template import loder

# Create your views here.

# def home(request):
    # template = loder.get_template('home.html')
    # return HttpResponse(template.render())
    # return render(request, 'main/home.html')


from django.shortcuts import render

def home(request):
    return render(request, 'home.html')



# ********************************
# initial state
# from django.shortcuts import render

# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to my home page!")