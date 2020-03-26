from django.shortcuts import render
from services.models import Myth
# Create your views here.
def myths(request):
    myth = Myth.objects.all()
    return render(request, 'services/myths.html',{'myths':myth})
