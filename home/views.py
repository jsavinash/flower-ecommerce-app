from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'firstname': 'Avinash',
        'lastname': 'Nishad'
    }
    return render(request, 'home/index.html', context)
