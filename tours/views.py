from django.http import HttpResponse

def index(request):
    return HttpResponse("🌎 EastUSA Tours 首頁，建置中！")
