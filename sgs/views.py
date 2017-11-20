from django.shortcuts import render
from django.http import Http404

from sgs.models import Shipment

def index(request):
    shipments = Shipment.objects.all()
    return render(request, 'sgs/index.html', {
        'shipments': shipments,
    })

def shipment_detail(request, id):
    try:
        shipment = Shipment.objects.get(id=id)
    except Shipment.DoesNotExist:
        raise Http404('This shipment does not exist')
    return render(request, 'sgs/shipment_detail.html', {
        'shipment':shipment,
    })
