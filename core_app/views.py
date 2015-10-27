from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
from core_app.models import Item
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.

@login_required
def home(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item, created = Item.objects.get_or_create(item_id=item_id,user=request.user)
        item.count += 1
        item.save()
    token, created = Token.objects.get_or_create(user=request.user)
    return render(request, 'index.html', {'token': token})

@login_required

def analytics(request):
    return JsonResponse(list(Item.objects.filter(user=request.user).values('item_id','count')),safe=False)