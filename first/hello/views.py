from django.shortcuts import render
from django.http import HttpResponse
import models
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('homepage.html')

def classification(request):
    s=models.Steps()
    #text=s.classification("i like abhay film i like aamir khan ghajini movie chennai express movie is good")
    text=s.classification(request.GET.get('q',''))
    print text
    response=HttpResponse(text)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"

    return response
    #return text


    #return  HttpResponse(text)
def sentiment(request):
    s=models.Steps()
    text=s.sentiment(request.GET.get('q',''))
    response=HttpResponse(text)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"

    return response
def er(request):
    s=models.Steps()
    text=s.er(request.GET.get('q',''))
    response=HttpResponse(text)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"

    return response
