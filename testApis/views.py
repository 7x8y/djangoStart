from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("home page requested")
    list1=[
        "qq1",
        "qq2",
        "qq3"
    ]
    # return HttpResponse("home page returned")
    return JsonResponse(list1, safe=False)