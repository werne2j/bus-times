# Create your views here.
from django.shortcuts import render_to_response as render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime

from busing.models import Stop

def index(request):
	context = {}
	stopNum = []
	shuttle_bus = []
	location = []
	time1 = []
	time2 = []
	kind = []
	requestType = []
	coord_x = []
	coord_y = []

	stop_data = Stop.objects.all().order_by('location')

	for stop in stop_data:
		stopNum.append(stop.id)
		shuttle_bus.append(stop.shuttle)
		location.append(stop.location)
		time1.append(stop.time_1)
		time2.append(stop.time_2)
		kind.append(stop.kind_of_stop)
		requestType.append(stop.type_of_request)
		coord_x.append(stop.coord_x)
		coord_y.append(stop.coord_y)

	context['data'] = zip(stopNum, shuttle_bus, location, time1, time2, kind, requestType, coord_x, coord_y)
	context['loop_time'] = [i + 1 for i in range(6,12)]
 	context['loop_time2'] = [i + 1 for i in range(0,6)]
	


	return render('busing/index.html', context, context_instance=RequestContext(request))




