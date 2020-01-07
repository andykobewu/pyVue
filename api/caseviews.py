from django.shortcuts import render
from api.models import Case

# Create your views here.
def case_manage(request):
    usename = request.session.get('user','')
    case_list = Case.objects.all()
    return render(request,'<h1>test<h1/>', {'user':usename,'cases':case_list})


