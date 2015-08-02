from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext

from forms import NewProductForm
from RentItApp.models import Product_registration
from RentItApp.models import Product_category
from RentItApp.models import ProductImage
from forms import DocumentForm


def product_add(request):
    new_product_form = NewProductForm()
    upload_photo_form = DocumentForm()


    # register = Product_registration(uid=request.session['global_uid'])
    # register = Product_registration(uid=request.session['global_uid'],pc_id=request.POST.get("product_category"),product_name=request.POST.get("product_name"),product_title=request.POST.get("product_title"),product_description=request.POST.get("product_description"),rental_condition=request.POST.get("product_conditions"))
    # register.save()
    # product_registration_list=Product_registration.objects.get(uid=request.session['global_uid'])
    # product_id=product_registration_list.product_id
    # print product_id

    return render(request, 'seller/product_add.html', {'new_product_form': new_product_form})


def product_data_add(request):
    # register = Product_registration.objects.get(uid=request.session['global_uid'])
    # register = Product_registration(uid=request.session['global_uid'],pc_id=request.POST.get("product_category"),product_name=request.POST.get("product_name"),product_title=request.POST.get("product_title"),product_description=request.POST.get("product_description"),rental_condition=request.POST.get("product_conditions"))
    # register.save()
    print "########" + request.POST.get("product_id_label") + "#############"
    # product_registration_list=Product_registration.objects.get(product_id=request.POST.get("product_id_label"))
    register = Product_registration(uid=request.session['global_uid'], pc_id=request.POST.get("product_category"),
                                    product_name=request.POST.get("product_name"),
                                    available_from=request.POST.get("available_from"),
                                    available_till=request.POST.get("available_till"),
                                    product_title=request.POST.get("product_title"),
                                    product_description=request.POST.get("product_description"),
                                    rental_condition=request.POST.get("product_conditions"))
    register.save()
    # Product_registration.pc_id=request.POST.get("product_category")
    # Product_registration.product_name=request.POST.get("product_name")
    # Product_registration.available_from=request.POST.get("available_from")
    # Product_registration.available_till=request.POST.get("available_till")
    # Product_registration.product_title=request.POST.get("product_title")
    # Product_registration.product_description=request.POST.get("product_description")
    # Product_registration.rental_condition=request.POST.get("product_conditions")
    # print product_id
    # Product_registration.save()
    return render(request, 'seller/user_dashboard.html')


def search_result(request):
    search_proc_name = request.POST.get("ecom-search")
    search_proc_id = Product_category.objects.filter(pc_name__icontains=search_proc_name)

    search_pro_list = Product_registration.objects.filter(pc_id=search_proc_id)
    # print(spi1.product_name)
    # search_pro_list.append(spi1)
    # pass
    # for pci in search_proc_list1:
    #	search_pro_list= Product_registration.objects.filter(pc_id=)
    #	pass
    # search_pro_list= Product_registration.objects.filter(pc_id=search_proc_id)
    # for p in search_pro_list:
    #	print (p.product_name)
    #	pass
    return render_to_response('Landing/search_results.html', {'search_pro_list': search_pro_list},
                              context_instance=RequestContext(request))


def upload_product_image(request):
    p_id = request.POST.get("product_id_label_file")
    print request.POST.get("product_id_label_file")
    print request.FILES['file']
    form = DocumentForm(request.POST, request.FILES)
    docfile = ProductImage(docfile=request.FILES['file'],
                           product_id=p_id)
    docfile.save()
    form.errors
    # Redirect to the document list after POST
    #        return HttpResponseRedirect(reverse('upfile.views.list'))
    # else:
    #    form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    # documents = Document.objects.all()

    return render(request, 'seller/user_dashboard.html')
