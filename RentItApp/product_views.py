from django.shortcuts import render
from django.template import RequestContext
from forms import NewProductForm
from RentItApp.models import User
from RentItApp.models import UserRegistration
from RentItApp.models import ProductRegistration
from RentItApp.models import ProductCategory
from RentItApp.models import ProductImage


def product_add(request):
	new_product_form = NewProductForm()
	user_email = request.session['uemail']
	list1 = []
	for e in User.objects.all():
		list1.append(e.umail)
		pass
		if user_email in list1:
			logged_user = User.objects.get(umail=user_email)
			uid = logged_user.uid
			ee = UserRegistration.objects.get(uid=uid)
			uname = ee.uname
			return render(request, 'seller/product_add.html', {'new_product_form': new_product_form, 'UserName': uname})
		else:
			return render(request, 'seller/product_add.html', {'new_product_form': new_product_form})


def product_data_add(request):
	register = ProductRegistration(uid=request.session['global_uid'], pc_id=request.POST.get("product_category"), product_name=request.POST.get("product_name"), available_from=request.POST.get("available_from"), available_till=request.POST.get("available_till"), product_title=request.POST.get("product_title"), product_description=request.POST.get("product_description"), rental_condition=request.POST.get("product_conditions"))
	register.save()
	user_email = request.session['uemail']
	list1 = []
	for e in User.objects.all():
		list1.append(e.umail)
		pass
		if user_email in list1:
			logged_user = User.objects.get(umail=user_email)
			uid = logged_user.uid
			ee = UserRegistration.objects.get(uid=uid)
			uname = ee.uname
			pr = ProductRegistration.objects.filter(uid=uid)
			if pr.count() != 0:
				for p in pr:
					proc_name = ProductCategory.objects.get(pc_id=p.pc_id)
					p.pc_id = proc_name.pc_name
					pass

				for sProduct in pr:
					category_id = sProduct.pc_id
					pass
					return render(request, 'seller/user_dashboard.html', {'UserName': uname, 'pr_details': pr, 'pr_category': category_id})
			else:
				return render(request, 'seller/user_dashboard.html', {'UserName': uname})
		else:
				return render(request, 'seller/user_dashboard.html')


def search_result(request):
	search_proc_name = request.POST.get("ecom-search")
	search_proc_id = ProductCategory.objects.filter(pc_name__icontains=search_proc_name)
	search_pro_list = ProductRegistration.objects.filter(pc_id=search_proc_id)
	return render('Landing/search_results.html', {'search_pro_list': search_pro_list}, context_instance=RequestContext(request))


def upload_product_image(request):
	p_id = request.POST.get("product_id_label_file")
	print request.POST.get("product_id_label_file")
	print request.FILES['file']
	docfile = ProductImage(docfile=request.FILES['file'], product_id=p_id)
	docfile.save()
	return render(request, 'seller/user_dashboard.html')
