from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Karticka
from .forms import KartickaForm
from django.views.decorators.http import require_POST, require_http_methods

# Create your views here.

def index(request):
    karticky = Karticka.objects.all()
    context = {
            'karticky': karticky,
            'form': KartickaForm()
            }
    
    return render(request, 'index.html', context)


@require_POST
def submit_form(request):
    form = KartickaForm(request.POST)
    if form.is_valid():
        karticka = form.save(commit=False)
        karticka.save()
        
        # return paretial html
        context = {'karticka': karticka}
        return render(request, 'index.html#kartickaitem-partial', context)
       
       
@require_POST
def more_info(request, id):
    info = get_object_or_404(Karticka, id=id)
    context = {'info': info}
    return render(request, 'info.html', context)

@require_http_methods(['DELETE'])
def delete_card(request, id):
    karticka = get_object_or_404(Karticka, id=id)
    karticka.delete()
    response = HttpResponse(status=202)
    response['HX-Trigger'] = 'delete-card'
    return response
    
    