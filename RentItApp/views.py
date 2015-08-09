from django.shortcuts import render_to_response
from django.shortcuts import render
# from forms import SignupForm
from RentItApp.models import User
from RentItApp.models import UserRegistration
from RentItApp.models import ProductCategory
from RentItApp.models import ProductRegistration


temp = ""
uemail = ""
global_uid = 0
pr_details = []
pr = ""


def register(request):
	try:
		UMAIL = request.POST.get("register-email")
		UPASS = request.POST.get("register-password")
		UNAME = request.POST.get("register-firstname")
		UMOBILE = request.POST.get("register-mobile")
		UCITY = request.POST.get("register-city")
		if UMAIL != "" and UPASS != "":
			user = User(umail=UMAIL, upass=UPASS)
			user.save()
			e = User.objects.get(umail=UMAIL)
			user_reg = UserRegistration(uid=e.uid, uname=UNAME, umobile=UMOBILE, ucity=UCITY)
			user_reg.save()
			return render(request, 'seller/user_dashboard.html')
		pass
	except Exception, e:
		raise e


def show(request):
	login_user_email = request.POST.get("login-email")
	print("This is login user:")
	print(login_user_email)
	global pr, pr
	request.session['uemail'] = login_user_email
	login_user_pass = request.POST.get("login-password")
	list1 = []
	list2 = []
	for e in User.objects.all():
		list1.append(e.umail)
		list2.append(e.upass)
		pass

	if login_user_email in list1:
		index_email = list1.index(login_user_email)
		index_pass = list2[index_email]
		e = User.objects.get(umail=request.session['uemail'])
		uid = e.uid
		print(uid)
		request.session['global_uid'] = uid
		ee = UserRegistration.objects.get(uid=uid)
		print(ee.uname)
		uname = ee.uname

		if index_pass == login_user_pass:
			product_id_current = request.POST.get("product_id_current")
			print product_id_current
			pr = ProductRegistration.objects.filter(uid=uid)
			for p in pr:
				proc_name = ProductCategory.objects.get(pc_id=p.pc_id)
				p.pc_id = proc_name.pc_name
				pass

			for sProduct in pr:
				category_id = sProduct.pc_id
				pass
				return render_to_response(request, 'seller/user_dashboard.html', {'list1': uname, 'pr_details': pr, 'pr_category': category_id})
	else:
		return render_to_response("seller/login.html", {'list1': 'Wrong password, please enter valid Credentials.'})


def show_details(request):
	print ("Ajax working")
	if request.method == "POST" and request.is_ajax():
		name = request.POST['data']
		print name
		print "#######$$$$$$$$$$$$"
	print "In ProductEdit"
	print request.POST.get("product_id_current")
	product_id_current = request.POST.get("product_id_current")
	print product_id_current
	pr = ProductRegistration.objects.filter(product_id=product_id_current)
	for p in pr:
		proc_name = ProductCategory.objects.get(pc_id=p.pc_id)
		p.pc_id = proc_name.pc_name
		pass
	# Below code is to get the profile details of the user
	# sUserDetails = User_registration.objects.get(uid=uid)
	# sUsersEmail = User.objects.get(uid=uid)
	# Below code is to get the Product details of the user]
	# for sProduct in pr:
	# procId = sProduct.product_id
	# pCategory_id = sProduct.pc_id
	# pCategory__name=Product_category.objects.get(pc_id=pCategory_id)
	# pImage = ProductImage.objects.get(product_id=procId).docfile
	# pass
	# print sUserDetails.uname
	# print "CategoryName"+pCategory_id
	# return render(request, 'seller/user_dashboard.html')
