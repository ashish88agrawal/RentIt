from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from django.template.context import RequestContext
from RentItApp.models import ProductCategory
from RentItApp.models import ProductRegistration


def home(request):
	pro_last3_entry = ProductRegistration.objects.all().order_by('-product_id')[:3]
	for p in pro_last3_entry:
		print p.product_name
		pass
	# print pro_last3_entry.product_name[0]
	return render_to_response('Landing/home.html', {'list1': pro_last3_entry}, context_instance=RequestContext(request))


def view_products(request):
	products = ProductRegistration.objects.all()

	for p in products:
		print p.product_name
		pass
	for p in products:
		categories = ProductCategory.objects.get(pc_id=p.pc_id)
		p.pc_id = categories.pc_name
		pass
		print categories.pc_name

	return render(request, 'Landing/product_list.html', {'product_details': products})


def products_detail(request):
	return render(request, 'Landing/product_list.html', {'product_details': products})