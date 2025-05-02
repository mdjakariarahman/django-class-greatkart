from django.http import HttpResponse

def home(request):
    return HttpResponse("<h3> Hey, you FOOOOOOOL . You're at the home page. </h3>")