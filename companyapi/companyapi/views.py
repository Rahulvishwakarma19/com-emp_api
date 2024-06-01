from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("Home page requested..")
    #return HttpResponse("This is home page..")
    friends=[
        'ankit',
        'ravi',
        'uttam'

    ]
    return JsonResponse(friends,safe=False)