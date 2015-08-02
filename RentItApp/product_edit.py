from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.core.context_processors import csrf
from django.db import models
from django import forms
#from forms import SignupForm
from forms import NewProductForm
from RentItApp.models import User
from RentItApp.models import User_registration
from RentItApp.models import Product_registration
from RentItApp.models import Product_category
from RentItApp.models import ProductImage
from django.core import validators
from django.template import RequestContext


def show_details(request):
		print "In ProductEdit"
		product_id_current = request.POST.get("product_id_current")
		print product_id_current
		pr = Product_registration.objects.filter(product_id=product_id_current)
		for p in pr:
			proc_name = Product_category.objects.get(pc_id=p.pc_id)
			p.pc_id = proc_name.pc_name
			pass
		# Below code is to get the profile details of the user
		# sUserDetails = User_registration.objects.get(uid=uid)
		# sUsersEmail = User.objects.get(uid=uid)
		# Below code is to get the Product details of the user]
		for sProduct in pr:
			procId = sProduct.product_id
			pCategory_id = sProduct.pc_id
			# pCategory__name=Product_category.objects.get(pc_id=pCategory_id)
			# pImage = ProductImage.objects.get(product_id=procId).docfile
			pImage = ""
			print "######################"
			print pCategory_id
			print "######################"
			pass
		# print sUserDetails.uname
		# print "CategoryName"+pCategory_id
		return render(request, 'page_ecom_dashboard.html',
						  { 'pr_details': pr, 'pr_category':pCategory_id})
