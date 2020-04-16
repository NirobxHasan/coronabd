from django.shortcuts import render
from services.models import Myth,Coronacounter,Area
from django.views.generic import TemplateView
# Create your views here.
def myths(request):
    myth = Myth.objects.all()
    return render(request, 'services/myths.html',{'myths':myth})


def confirmedArea(request):
    areas = Area.objects.all()
    return render(request, 'services/confirmedlist.html',{'areas':areas})


class CoronaChartView(TemplateView):
    template_name = 'services/coronachart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Coronacounter.objects.all()
        return context




