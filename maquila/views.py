from django.shortcuts import render

# Create your views here.
def cuts(request):
    return render(request, 'maquila/cuts.html')