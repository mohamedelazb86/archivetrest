from django.shortcuts import render,redirect
from contractor.models import Contractor
from settings.models import Sector
from django.contrib import messages

def contractor(request):
    contractor=Contractor.objects.all()
    sector=Sector.objects.all()
    context={
        'contractor':contractor,
        'sector':sector
    }
    return render(request,'contractor/contractor.html',context)

def add_contractor(request):
    if request.method=='POST':
        code=request.POST['code']
        
        name=request.POST['name']
        sector=request.POST['sector']
        project=request.POST['project']
        notes=request.POST['notes']

        Contractor.objects.create(
            code=code,
            
            name=name,
            sector_id=sector,
            project=project,
            notes=notes
        )
        messages.success(request,'تم إضافة  مقاول بنحاج')
        return redirect('/contractor/')
