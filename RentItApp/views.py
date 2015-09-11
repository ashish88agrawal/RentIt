from django.shortcuts import render

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


def get_user_email(request):
	login_user_email = request.POST.get("login-email")
	return login_user_email


def get_user_password(request):
	login_user_pass = request.POST.get("login-password")
	return login_user_pass


def show(request):
	global pr
	user_email = get_user_email(request)
	user_password = get_user_password(request)
	request.session['uemail'] = user_email
	list1 = []
	list2 = []
	for e in User.objects.all():
		list1.append(e.umail)
		list2.append(e.upass)
		pass

	if user_email in list1:
		index_email = list1.index(user_email)
		index_pass = list2[index_email]
		e = User.objects.get(umail=request.session['uemail'])
		uid = e.uid
		request.session['global_uid'] = uid
		ee = UserRegistration.objects.get(uid=uid)
		uname = ee.uname

		if index_pass == user_password:
			pr = ProductRegistration.objects.filter(uid=uid)
			print(pr.count())
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
			return render ("seller/login.html", {'Error': 'Wrong password, please enter valid Credentials.'})
	else:
		return render("seller/login.html", {'Error': 'Wrong password, please enter valid Credentials.'})


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


def show_user_dashboard(request):
	global pr1
	user_email1 = get_user_email()
	user_password1 = get_user_password()
	request.session['uemail1'] = user_email1
	list1 = []
	list2 = []
	for e in User.objects.all():
		list1.append(e.umail)
		list2.append(e.upass)
		pass

	if user_email1 in list1:
		index_email1 = list1.index(user_email1)
		index_pass1 = list2[index_email1]
		e1 = User.objects.get(umail1=request.session['uemail1'])
		uid1 = e1.uid
		request.session['global_uid1'] = uid1
		ee1 = UserRegistration.objects.get(uid=uid1)
		uname1 = ee.uname

		if index_pass1 == user_password1:
			product_id_current1 = request.POST.get("product_id_current")
			print product_id_current1
			pr1 = ProductRegistration.objects.filter(uid=uid1)
			for p in pr1:
				proc_name1 = ProductCategory.objects.get(pc_id=p.pc_id)
				p.pc_id = proc_name1.pc_name
				pass

			for sProduct in pr1:
				category_id1 = sProduct.pc_id
				pass
				return render(request, 'seller/user_dashboard.html', {'UserName': uname1, 'pr_details': pr1, 'pr_category': category_id1})
		else:
			return render("seller/login.html", {'Error': 'Wrong password, please enter valid Credentials.'})
	else:
		return render("seller/login.html", {'Error': 'Wrong password, please enter valid Credentials.'})