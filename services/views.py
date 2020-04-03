from django.shortcuts import render
from services.models import Myth,Coronacounter
from django.views.generic import TemplateView
# Create your views here.
def myths(request):
    myth = Myth.objects.all()
    return render(request, 'services/myths.html',{'myths':myth})



class CoronaChartView(TemplateView):
    template_name = 'services/coronachart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Coronacounter.objects.all()
        return context