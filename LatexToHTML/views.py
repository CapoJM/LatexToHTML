from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .models import Cambio
from .textprocessing import *

# Create your views here.
def index(request):
    try:
        latex = str(request.POST["tex-input"])
        type = str(request.POST["type"])
    except KeyError:
        latex = ""
        html = ""
        type = "no type"

    if type == "Article":
        html = processArticle(latex)
    elif type == "Comment":
        html = processComment(latex)


    context = {"latex":latex, "html":html}


    return render(request, "LatexToHTML/index.html", context)
