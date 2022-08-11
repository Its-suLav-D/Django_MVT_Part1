from django.shortcuts import render

# Create your views here.
def index(request): 

    template = "<html>" \
            "This is your first view" \
                "</html>"
    return HttpResponse(content=template)