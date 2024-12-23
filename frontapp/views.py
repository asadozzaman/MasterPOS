from django.shortcuts import render

# Create your views here.
def frontui(request):
    data = {
        # 'lab': lab,
        # 'tests': reportTestinglist_c,
        }

    return render(request,  'front/index.html', data)

