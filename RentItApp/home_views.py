from django.shortcuts import render_to_response
from django.template import RequestContext

from RentItApp.models import ProductRegistration


def home(request):
	pro_last3_entry = ProductRegistration.objects.all().order_by('-product_id')[:3]
	for p in pro_last3_entry:
		print p.product_name
		pass
	# print pro_last3_entry.product_name[0]
	return render_to_response('Landing/home.html', {'list1': pro_last3_entry}, context_instance=RequestContext (request))
