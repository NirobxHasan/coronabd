from django.shortcuts import render
from services.models import Myth,Coronacounter,Area
from django.views.generic import TemplateView
# Create your views here.
def myths(request):
    myth = Myth.objects.all()
    return render(request, 'services/myths.html',{'myths':myth})

def CoronaChartView(request):
    qs = Coronacounter.objects.all()
    areas = Area.objects.all()
    Dhaka_total = 0
    Chattogram_total = 0
    Rangpur_total = 0
    Mymensingh_total = 0
    Sylhet_total = 0
    Khulna_total = 0
    Barishal_total = 0
    Rajshahi_total = 0
    Dhakacity_total = 0
    total = 0
    Unidentified_total = 0
    for i in areas:
        if i.division.division == "Dhaka Division" and i.district == 'Dhaka':
            Dhakacity_total = Dhakacity_total + i.confirmed_cases
        if i.division.division == "Dhaka Division":
            Dhaka_total = Dhaka_total + i.confirmed_cases
        if i.division.division == "Chattogram Division":
            Chattogram_total = Chattogram_total + i.confirmed_cases    
        if i.division.division == "Rangpur Division":
           Rangpur_total = Rangpur_total + i.confirmed_cases
        if i.division.division == "Mymensingh Division":
            Mymensingh_total =  Mymensingh_total + i.confirmed_cases
        if i.division.division == "Sylhet Division":
            Sylhet_total = Sylhet_total + i.confirmed_cases      
        if i.division.division == "Khulna Division":
            Khulna_total = Khulna_total + i.confirmed_cases    
        if i.division.division == "Barishal Division":
            Barishal_total = Barishal_total + i.confirmed_cases
        if i.division.division == "Rajshahi Division":
            Rajshahi_total = Rajshahi_total + i.confirmed_cases
        if i.division.division == "Undefined":
            Unidentified_total =Unidentified_total + i.confirmed_cases        

        total = total + i.confirmed_cases 
            
    context={
        'qs':qs,
        'areas':areas,
        'Dhaka_total':Dhaka_total,
        'Chattogram_total':Chattogram_total,
        'Rangpur_total':Rangpur_total,
        'Mymensingh_total':Mymensingh_total,
        'Sylhet_total':Sylhet_total,
        'Khulna_total':Khulna_total,
        'Barishal_total':Barishal_total,
        'Rajshahi_total':Rajshahi_total,
        'Dhakacity_total':Dhakacity_total,
        'total':total,
        'Unidentified_total':Unidentified_total,
        'confirmed_growthrate':((qs[len(qs)-1].total_confirmed-qs[len(qs)-2].total_confirmed)/qs[len(qs)-2].total_confirmed)*100,
        'death_growthrate':((qs[len(qs)-1].total_death-qs[len(qs)-2].total_death)/qs[len(qs)-2].total_death)*100,
        'recovered_growthrate':((qs[len(qs)-1].total_recovered-qs[len(qs)-2].total_recovered)/qs[len(qs)-2].total_recovered)*100,
        'tested_growthrate':((qs[len(qs)-1].total_tested-qs[len(qs)-2].total_tested)/qs[len(qs)-2].total_tested)*100,
    }        
    return render(request,'services/coronachart.html',context)

def confirmedArea(request):
    areas = Area.objects.all()
    Dhaka_total = 0
    Chattogram_total = 0
    Rangpur_total = 0
    Mymensingh_total = 0
    Sylhet_total = 0
    Khulna_total = 0
    Barishal_total = 0
    Rajshahi_total = 0
    Dhakacity_total = 0
    total = 0
    Unidentified_total = 0
    for i in areas:
        if i.division.division == "Dhaka Division" and i.district == 'Dhaka':
            Dhakacity_total = Dhakacity_total + i.confirmed_cases
        if i.division.division == "Dhaka Division":
            Dhaka_total = Dhaka_total + i.confirmed_cases
        if i.division.division == "Chattogram Division":
            Chattogram_total = Chattogram_total + i.confirmed_cases    
        if i.division.division == "Rangpur Division":
           Rangpur_total = Rangpur_total + i.confirmed_cases
        if i.division.division == "Mymensingh Division":
            Mymensingh_total =  Mymensingh_total + i.confirmed_cases
        if i.division.division == "Sylhet Division":
            Sylhet_total = Sylhet_total + i.confirmed_cases      
        if i.division.division == "Khulna Division":
            Khulna_total = Khulna_total + i.confirmed_cases    
        if i.division.division == "Barishal Division":
            Barishal_total = Barishal_total + i.confirmed_cases
        if i.division.division == "Rajshahi Division":
            Rajshahi_total = Rajshahi_total + i.confirmed_cases
        if i.division.division == "Undefined":
            Unidentified_total =Unidentified_total + i.confirmed_cases        

        total = total + i.confirmed_cases 
            


    context={
        'areas':areas,
        'Dhaka_total':Dhaka_total,
        'Chattogram_total':Chattogram_total,
        'Rangpur_total':Rangpur_total,
        'Mymensingh_total':Mymensingh_total,
        'Sylhet_total':Sylhet_total,
        'Khulna_total':Khulna_total,
        'Barishal_total':Barishal_total,
        'Rajshahi_total':Rajshahi_total,
        'Dhakacity_total':Dhakacity_total,
        'total':total,
        'Unidentified_total':Unidentified_total,
        
    }        
    return render(request, 'services/confirmedlist.html',context)



