from django.shortcuts import render
from RentItApp.models import ProductRegistration
from RentItApp.models import ProductCategory


def show_details(request):
	print "In ProductEdit"
	product_id_current = request.POST.get("product_id_current")
	print product_id_current
	pr = ProductRegistration.objects.filter(product_id=product_id_current)
	for p in pr:
		proc_name = ProductCategory.objects.get(pc_id=p.pc_id)
		p.pc_id = proc_name.pc_name
		pass
	# Below code is to get the profile details of the user
	# sUserDetails = UserRegistration.objects.get(uid=uid)
	# sUsersEmail = User.objects.get(uid=uid)
	# Below code is to get the Product details of the user]
	for sProduct in pr:
		procid = sProduct.product_id
		pcategory_id = sProduct.pc_id
		# pCategory__name=ProductCategory.objects.get(pc_id=pCategory_id)
		# pImage = ProductImage.objects.get(product_id=procId).docfile
		pImage = ""
		print "######################"
		print pcategory_id
		print "######################"
		pass
	# print sUserDetails.uname
	# print "CategoryName"+pcategory_id
	return render(request, 'seller/page_ecom_dashboard.html', {'pr_details': pr, 'pr_category': pcategory_id})
