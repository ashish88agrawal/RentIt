from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.core.context_processors import csrf
from django.db import models
from django import forms
from forms import NewProductForm
from RentItApp.models import User_registration
from RentItApp.models import Product_registration
from RentItApp.models import Product_category
from RentItApp.models import ProductImage
from RentItApp.models import ProductImage
from django.core import validators
from django.template import RequestContext
from django.core.urlresolvers import reverse
from forms import DocumentForm

def product_add(request):
	new_product_form = NewProductForm()
	upload_photo_form = DocumentForm()
	return render(request, 'seller/product_add.html',{'new_product_form':new_product_form})

def product_data_add(request):
		register = Product_registration(uid=request.session['global_uid'],
									pc_id=request.POST.get("product_category"),
									product_name=request.POST.get("product_name"),
									available_from=request.POST.get("available_from"),
									available_till=request.POST.get("available_till"),
									product_title=request.POST.get("product_title"),
									product_description=request.POST.get("product_description"),
									rental_condition=request.POST.get("product_conditions"))
		register.save()
		return render(request, 'seller/page_ecom_dashboard.html')

def search_result(request):
		search_proc_name = request.POST.get("ecom-search")
		search_proc_id = Product_category.objects.filter(pc_name__icontains=search_proc_name)
		search_pro_list = Product_registration.objects.filter(pc_id=search_proc_id)
		return render_to_response('ecom_search_results.html',{'search_pro_list':search_pro_list},context_instance=RequestContext(request))



def upload_product_image(request):
	p_id=request.POST.get("product_id_label_file")
	print request.POST.get("product_id_label_file")
	print request.FILES['file']
	form = DocumentForm(request.POST, request.FILES)
	docfile = ProductImage(docfile=request.FILES['file'],
							product_id=p_id)
	docfile.save()
	form.errors

	return render(request, 'page_ecom_dashboard.html')