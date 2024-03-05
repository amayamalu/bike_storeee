import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from bike_store_app.models import *


def view_index(request):
    return render(request,"index.html")

def admin_index(request):
    return render(request,"admin/admin_index.html")

def shop_index(request):
    return render(request,"shop/shop_index.html")

def admin_home(request):
    return render(request,"admin/admin_home.html")

def loginform(request):
    return render(request,"login.html")

def loginform_post(request):
    uname=request.POST['textfield']
    pswd=request.POST['textfield2']
    data=login.objects.filter(username=uname,password=pswd)
    if data.exists():
        data=data[0]
        request.session['log'] = "lo"
        request.session['lid']=data.id
        if data.usertype=="admin":
            return redirect('/admin_index')
        elif data.usertype=="shop":
            return redirect('/shop_index')

        else:
            return HttpResponse("<script>alert('invalid');window.location='/#login'</script>")
    else:
        return HttpResponse("<script>alert('not found');window.location='/#login'</script>")


def view_shops(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=shop.objects.filter(LOGIN__usertype="pending")
    return render(request,"admin/shop_verify.html",{"data":res})

def approve_shop(request,id):
    login.objects.filter(id=id).update(usertype="shop")
    return HttpResponse("<script>alert('approved');window.location='/view_shops#aa'</script>")

def reject_shop(request,id):
    login.objects.filter(id=id).update(usertype="rejected")
    return HttpResponse("<script>alert('rejected');window.location='/view_shops#aa'</script>")

def add_service(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    return render(request,"admin/service_add.html")

def add_service_post(request):
    servicee=request.POST['textfield']
    i=service.objects.filter(service_name=servicee)
    if i.exists():
        return HttpResponse("<script>alert('Alredy in service');window.location='/add_service#aa'</script>")
    else:
        obj = service()
        obj.service_name = servicee
        obj.save()
        return HttpResponse("<script>alert('added');window.location='/admin_index'</script>")


def view_service(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=service.objects.all()
    return render(request,"admin/Vview_service.html",{"data":res})


def delete_service(request,id):
    service.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/admin_index'</script>")

def view_users(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=user.objects.all()
    return render(request,"admin/view_users.html",{"data":res})

def view_complaints(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=complaints.objects.all()
    return render(request,"admin/view_complaints.html",{"data":res})

def reply(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    id=id
    return render(request,"admin/send_reply.html",{"id":id})

def reply_post(request,id):
    replyy=request.POST['textfield']
    d=datetime.datetime.now().strftime("%Y-%m-%d")
    complaints.objects.filter(id=id).update(reply=replyy,reply_date=d)
    return HttpResponse("<script>alert('replied');window.location='/view_complaints#aa'</script>")

def view_rating(request):
        res=rating.objects.all()
        ar_rt = []

        for im in res:
            fs = "/static/star/full.jpg"
            hs = "/static/star/half.jpg"
            es = "/static/star/empty.jpg"
            ar = []
            a = float(im.rating)
            if a >= 0.0 and a < 0.4:
                print("eeeee")
                ar = [es, es, es, es, es]

            elif a >= 0.4 and a < 0.8:
                print("heeee")
                ar = [hs, es, es, es, es]

            elif a >= 0.8 and a < 1.4:
                print("feeee")
                ar = [fs, es, es, es, es]

            elif a >= 1.4 and a < 1.8:
                print("fheee")
                ar = [fs, hs, es, es, es]

            elif a >= 1.8 and a < 2.4:
                print("ffeee")
                ar = [fs, fs, es, es, es]

            elif a >= 2.4 and a < 2.8:
                print("ffhee")
                ar = [fs, fs, hs, es, es]

            elif a >= 2.8 and a < 3.4:
                print("fffee")
                ar = [fs, fs, fs, es, es]

            elif a >= 3.4 and a < 3.8:
                print("fffhe")
                ar = [fs, fs, fs, hs, es]

            elif a >= 3.8 and a < 4.4:
                print("ffffe")
                ar = [fs, fs, fs, fs, es]

            elif a >= 4.4 and a < 4.8:
                print("ffffh")
                ar = [fs, fs, fs, fs, hs]

            elif a >= 4.8 and a <= 5.0:
                print("fffff")
                ar = [fs, fs, fs, fs, fs]
            ar_rt.append({
                'r':im,
                'ar':ar
            })
            print(ar_rt)
        return render(request,"admin/view_rating.html",{"data":ar_rt})

def add_parts(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    return render(request,"admin/add_parts_category.html")

def add_parts_post(request):
    categoryy=request.POST['textfield']
    i=parts_category.objects.filter(category=categoryy)
    if i.exists():
        return HttpResponse("<script>alert('alredy in category');window.location='/add_parts#aa'</script>")
    else:
        obj = parts_category()
        obj.category = categoryy
        obj.save()
        return HttpResponse("<script>alert('added');window.location='/view_parts_cat#aa'</script>")


def view_parts_cat(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=parts_category.objects.all()
    return render(request,"admin/view_category.html",{"data":res})



def delete_parts_category(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    parts_category.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/view_parts_cat#aa'</script>")

def change_password(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    return render(request,"admin/change_password.html")

def change_password_post(request):
    current=request.POST['textfield']
    new=request.POST['textfield2']
    confirm=request.POST['textfield3']

    p=login.objects.filter(id=request.session['lid'])
    if p[0].password==current:
        if new==confirm:
            login.objects.filter(id=p[0].id).update(password=confirm)
            return HttpResponse("<script>alert('Changed');window.location='/#login'</script>")
        else:
            return HttpResponse("<script>alert('Mismatch');window.location='/change_password#aa'</script>")
    else:
        return HttpResponse("<script>alert('Not found');window.location='/change_password#aa'</script>")


#############################SHOP############################################################

def shop_home(request):
    return render(request,"shop/shop_home.html")

def register_shop(request):
    return render(request,"shop/shop_register.html")

def register_shop_post(request):
    name=request.POST['textfield']
    email=request.POST['textfield2']
    phone=request.POST['textfield3']
    post=request.POST['textfield4']
    pin=request.POST['textfield5']
    place=request.POST['textfield6']
    password=request.POST['textfield7']
    i=shop.objects.filter(name=name,email=email)
    if i.exists():
        return HttpResponse("<script>alert('already registered');window.location='/#login'</script>")

    else:
        obj = login()
        obj.username = email
        obj.password = password
        obj.usertype = "pending"
        obj.save()

        obj1 = shop()
        obj1.name = name
        obj1.email = email
        obj1.phone = phone
        obj1.post = post
        obj1.pin = pin
        obj1.place = place
        obj1.LOGIN = obj
        obj1.save()
        return HttpResponse("<script>alert('Registered');window.location='/#login'</script>")


def view_profile(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=shop.objects.get(LOGIN=request.session['lid'])
    return render(request,"shop/view_profile.html",{"data":res})

def add_bike(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    return render(request,"shop/bike_add.html")

def add_bike_post(request):
    name=request.POST['textfield']
    price=request.POST['textfield2']
    model=request.POST['textfield3']
    image=request.FILES['fileField']
    d=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    fs=FileSystemStorage()
    fs.save(r"C:\Users\amaya\PycharmProjects\bike_store\bike_store_app\static\imagess\\"+d+'.jpg',image)
    path="/static/imagess/"+d+'.jpg'
    i=bike.objects.filter(name=name,model=model)
    if i.exists():
        return HttpResponse("<script>alert('already in bike');window.location='/add_bike#ss'</script>")
    else:
        obj = bike()
        obj.name = name
        obj.price = price
        obj.image = path
        obj.model = model
        obj.SHOP = shop.objects.get(LOGIN=request.session['lid'])
        obj.save()
        return HttpResponse("<script>alert('added');window.location='/view_bike#ss'</script>")


def view_bike(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=bike.objects.filter(SHOP__LOGIN=request.session['lid'])
    return render(request,"shop/view_bike.html",{"data":res})

def update_bike(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=bike.objects.get(id=id)
    return render(request,"shop/update_bike.html",{"data":res})

def update_bike_post(request,id):
    try:
        name = request.POST['textfield']
        price = request.POST['textfield2']
        model = request.POST['textfield3']
        image = request.FILES['fileField']
        d = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        fs = FileSystemStorage()
        fs.save(r"C:\Users\amaya\PycharmProjects\bike_store\bike_store_app\static\imagess\\" + d + '.jpg', image)
        path = "/static/imagess/" + d + '.jpg'

        bike.objects.filter(id=id).update(name=name,price=price,model=model,image=path)
        return HttpResponse("<script>alert('updated');window.location='/view_bike#ss'</script>")
    except Exception as e:
        name = request.POST['textfield']
        price = request.POST['textfield2']
        model = request.POST['textfield3']
        bike.objects.filter(id=id).update(name=name,price=price,model=model)
        return HttpResponse("<script>alert('updated');window.location='/view_bike#ss'</script>")


def delete_bike(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    bike.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/view_bike#ss'</script>")


def view_parts_category(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=parts_category.objects.all()
    return render(request,"shop/view_parts_category.html",{"data":res})

def add_partss(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=parts_category.objects.all()
    return render(request,"shop/parts_add.html",{"data":res})

def add_partss_post(request):
    name=request.POST['textfield']
    price=request.POST['textfield2']
    company=request.POST['textfield3']
    category=request.POST['select']
    sid=shop.objects.get(LOGIN=request.session['lid'])
    i=parts.objects.filter(name=name)
    if i.exists():
        return HttpResponse("<script>alert('already in partss');window.location='/add_partss#ss'</script>")
    else:
        obj = parts()
        obj.name = name
        obj.price = price
        obj.manufacture_company = company
        obj.PARTS_CATEGORY_id = category
        obj.SHOP = sid
        obj.save()
        return HttpResponse("<script>alert('added');window.location='/view_parts#ss'</script>")


def view_parts(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=parts.objects.filter(SHOP__LOGIN=request.session['lid'])
    return render(request,"shop/view_parts.html",{"data":res})

def update_parts(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=parts.objects.get(id=id)
    qry=parts_category.objects.all()  #categories in PARTS_CATEGORY
    return render(request,"shop/update_parts.html",{"data":res,"data1":qry})

def update_parts_post(request,id):
    name = request.POST['textfield']
    price = request.POST['textfield2']
    company = request.POST['textfield3']
    category = request.POST['select']
    parts.objects.filter(id=id).update(name=name,price=price,manufacture_company=company,PARTS_CATEGORY=category)
    return HttpResponse("<script>alert('updated');window.location='/view_parts#ss'</script>")



def delete_parts(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    parts.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/view_parts#ss'</script>")


def view_bike_request(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=bike_request.objects.filter(status="pending")
    return render(request,"shop/view_request_bike.html",{"data":res})

def approve_bike_request(request,id):
    bike_request.objects.filter(id=id).update(status="approved")
    return HttpResponse("<script>alert('approved');window.location='/view_bike_request#ss'</script>")

def reject_bike_request(request,id):
    bike_request.objects.filter(id=id).update(status="rejected")
    return HttpResponse("<script>alert('rejected');window.location='/view_bike_request#ss'</script>")


def view_services(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=service.objects.all()
    return render(request,"shop/view_services.html",{"data":res})

def add_own_Service(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    id=id
    return render(request,"shop/amount.html",{'id':id})

def add_own_Service_post(request,sid):
    amount=request.POST['textfield']
    shid=shop.objects.get(LOGIN=request.session['lid'])
    i=ownservice.objects.filter(SERVICE_id=sid,SHOP=shid)
    if i.exists():
        return HttpResponse("<script>alert('Already Added');window.location='/view_services#ss'</script>")
    else:
        obj = ownservice()
        obj.amount = amount
        obj.SERVICE_id = sid
        obj.SHOP = shid
        obj.save()

        return HttpResponse("<script>alert('added');window.location='/view_services#ss'</script>")

def view_service_request(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=service_request.objects.filter(status="pending")
    return render(request,"shop/view_service_request.html",{'data':res})

def approve_service_request(request,id):
    service_request.objects.filter(id=id).update(status="approved")
    return HttpResponse("<script>alert('approved');window.location='/view_service_request#ss'</script>")

def reject_service_request(request,id):
    service_request.objects.filter(id=id).update(status="rejected")
    return HttpResponse("<script>alert('rejected');window.location='/view_service_request#ss'</script>")


def view_part_request(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=order.objects.filter(SHOP__LOGIN=request.session['lid'])
    return render(request,"shop/view_parts_request.html",{"data":res})

def view_part_items(request,id):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=order_sub.objects.filter(ORDER_id=id)
    return render(request,"shop/view_parts_item.html",{"data":res})

def view_payment_shop(request):
    if request.session['log'] != 'lo':
        return HttpResponse("<script>alert('logout succesfully');window.locatin='/loginform'</script>")
    res=order.objects.filter(SHOP__LOGIN=request.session['lid'])
    return render(request,"shop/view_paymnet.html",{"data":res})

def logout(request):
    request.session['log']=""
    request.session.clear()
    return HttpResponse("<script>alert('logout succesfully');window.location='/'</script>")


##################################################################################################################

def login_user(request):
    uname=request.POST['uname']
    pswd=request.POST['password']
    data=login.objects.filter(username=uname,password=pswd,usertype="user")
    if data.exists():
        return JsonResponse({"status":"ok","id":data[0].id})
    else:
        return JsonResponse({"status":"no"})



def register_user(request):
    name=request.POST['name']
    email=request.POST['email']
    phone=request.POST['phone']
    post=request.POST['post']
    pin=request.POST['pin']
    place=request.POST['place']
    password=request.POST['password']

    obj=login()
    obj.username=email
    obj.password=password
    obj.usertype="user"
    obj.save()

    obj1=user()
    obj1.name=name
    obj1.email=email
    obj1.phone=phone
    obj1.post=post
    obj1.pin=pin
    obj1.place=place
    obj1.LOGIN=obj
    obj1.save()

    return JsonResponse({"status":"ok"})

def view_profile_user(request):
    lid=request.POST['lid']
    res=user.objects.get(LOGIN=lid)
    return JsonResponse({"status":"ok","id":res.id,"name":res.name,"email":res.email,"phone":res.phone,"place":res.place,"post":res.post,"pin":res.pin})


def view_servicess(request):
    res=ownservice.objects.all()
    data=[]
    for i in res:
        data.append(
            {
                "id":i.id,
                "SERVICE":i.SERVICE.service_name,
                "amount":i.amount,
                "SHOP":i.SHOP.name,
            }
        )

    return JsonResponse({"status":"ok","data":data})




def send_request_service(request):
    sid=request.POST['sid']
    lid=request.POST['lid']
    uid=user.objects.get(LOGIN_id=lid)
    i=service_request.objects.filter(USER=uid,OWNSERVICE_id=sid)
    if i.exists():
        return JsonResponse({"status": "no"})
    else:
        obj = service_request()
        obj.USER = uid
        obj.OWNSERVICE_id = sid
        obj.date = datetime.datetime.now().strftime("%Y/%m/%d")
        obj.status = "pending"
        obj.save()
        return JsonResponse({"status": "ok"})



def view_bikes(request):
    res=bike.objects.all()
    data=[]
    for i in res:
        data.append(
            {
                "id":i.id,
                "name":i.name,
                "price":i.price,
                "image":i.image,
                "model":i.model,
                "SHOP":i.SHOP.name,
            }
        )
    return JsonResponse({"status":"ok","data":data})

def send_bike_request(request):
    bid = request.POST['bid']
    lid = request.POST['lid']
    uid = user.objects.get(LOGIN_id=lid)
    i=bike_request.objects.filter(USER=uid,BIKE_id=bid)
    if i.exists():
        return JsonResponse({"status": "no"})
    else:
        obj = bike_request()
        obj.BIKE_id = bid
        obj.USER = uid
        obj.status = "pending"
        obj.date = datetime.datetime.now().strftime("%Y/%m/%d")
        obj.save()
        return JsonResponse({"status": "ok"})


def view_partss(request):
    res=parts.objects.all()
    data=[]
    for i in res:
        data.append(
            {
                "id":i.id,
                "name":i.name,
                "price":i.price,
                "manufacture_company":i.manufacture_company,
                "PARTS_CATEGORY":i.PARTS_CATEGORY.category,
                "SHOP":i.SHOP.name,
            }
        )
    return JsonResponse({"status":"ok","data":data})

def add_to_cart_parts(request):
    q=request.POST['quantity']
    pid=request.POST['pid']
    lid=request.POST['lid']
    uid=user.objects.get(LOGIN_id=lid)
    d=cart.objects.filter(USER=uid,PARTS_id=pid)
    if d.exists():
        quan=d[0].quantity
        q1=int(quan)+int(q)
        cart.objects.filter(id=d[0].id).update(quantity=q1)
    else:
        obj = cart()
        obj.USER = uid
        obj.PARTS_id = pid
        obj.quantity = q
        obj.save()

    return JsonResponse({"status":"ok"})


def view_cart(request):
    lid=request.POST['lid']
    res=cart.objects.filter(USER=user.objects.get(LOGIN_id=lid))
    data=[]
    total=0
    for i in res:
        data.append(
            {
                "id":i.id,
                "parts_name":i.PARTS.name,
                "parts_price":i.PARTS.price,
                "quantity":i.quantity,
                "shop": i.PARTS.SHOP.name,
                "shop_id": i.PARTS.SHOP.id,
                "total":int(i.quantity)*int(i.PARTS.price)
            }
        )
        total = total + int(i.quantity) * int(i.PARTS.price)
    return JsonResponse({"status":"ok","data":data,"total":total})

def offline_payment(request):
    lid = request.POST['lid']
    amount=request.POST['amount']
    res = cart.objects.filter(USER=user.objects.get(LOGIN=lid))
    for i in res:
        cartobj = order.objects.filter(USER=user.objects.get(LOGIN=lid),SHOP=i.PARTS.SHOP,status='pending')
        if cartobj.exists():

            obj1=order_sub()
            obj1.quantity=i.quantity
            obj1.ORDER_id = cartobj[0].id
            obj1.PARTS_id = i.PARTS_id
            obj1.save()
        else:
            obj = order()
            obj.status = 'pending'
            obj.price = amount
            obj.payment_status = "offline"
            obj.payment_date = datetime.datetime.now().strftime("%Y/%m/%d")
            obj.USER = user.objects.get(LOGIN_id=lid)
            obj.SHOP = res[0].PARTS.SHOP
            obj.save()

            obj1 = order_sub()
            obj1.quantity = i.quantity
            obj1.ORDER_id = obj.id
            obj1.PARTS_id = i.PARTS_id
            obj1.save()
    res.delete()
    return JsonResponse({"status":"ok"})

def online_payment(request):
    lid = request.POST['lid']
    amount = request.POST['amount']
    res = cart.objects.filter(USER=user.objects.get(LOGIN=lid))

    for i in res:
        cartobj = order.objects.filter(USER=user.objects.get(LOGIN=lid), SHOP=i.PARTS.SHOP, status='pending')
        if cartobj.exists():

            obj1 = order_sub()
            obj1.quantity = i.quantity
            obj1.ORDER_id = cartobj[0].id
            obj1.PARTS_id = i.PARTS_id
            obj1.save()
        else:
            obj = order()
            obj.status = 'pending'
            obj.price = amount
            obj.payment_status = "online"
            obj.payment_date = datetime.datetime.now().strftime("%Y/%m/%d")
            obj.USER = user.objects.get(LOGIN_id=lid)
            obj.SHOP = res[0].PARTS.SHOP
            obj.save()

            obj1 = order_sub()
            obj1.quantity = i.quantity
            obj1.ORDER_id = obj.id
            obj1.PARTS_id = i.PARTS_id
            obj1.save()
    res.delete()
    return JsonResponse({"status":"ok"})



def view_previous_order(request):
    lid=request.POST['lid']
    uid=user.objects.get(LOGIN_id=lid)
    d=datetime.datetime.now().strftime("%Y/%m/%d")
    prev=order_sub.objects.filter(ORDER__USER_id=uid,ORDER__payment_date__lt=d)
    data=[]
    for i in prev:
        data.append(
            {
                "id":i.id,
                "payment_date": i.ORDER.payment_date,
                "parts_name": i.PARTS.name,
                "quantity":i.quantity,
                "status":i.ORDER.status,
                "payment_status":i.ORDER.payment_status,
            }
        )
    return JsonResponse({"status":"ok","data":data})


def send_review(request):
    lid=request.POST['lid']
    d=datetime.datetime.now().strftime("%Y/%m/%d")
    rat=request.POST['rating']
    uid=user.objects.get(LOGIN=lid)
    i=rating.objects.filter(USER=uid,rating=rat)
    if i.exists():
        return JsonResponse({"status": "ok"})
    else:
        obj = rating()
        obj.date = d
        obj.rating = rat
        obj.USER = uid
        obj.save()
        return JsonResponse({"status": "ok"})


def send_complaint(request):
    lid = request.POST['lid']
    d = datetime.datetime.now().strftime("%Y/%m/%d")
    com = request.POST['complaint']
    uid = user.objects.get(LOGIN_id=lid)
    i=complaints.objects.filter(USER=uid,complaint=com)
    if i.exists():
        return JsonResponse({"status": "no"})
    else:
        obj = complaints()
        obj.date = d
        obj.complaint = com
        obj.reply = "pending"
        obj.USER = uid
        obj.save()
        return JsonResponse({"status": "ok"})


def view_reply(request):
    lid=request.POST['lid']
    uid = user.objects.get(LOGIN_id=lid)
    res=complaints.objects.filter(USER=uid)
    data=[]
    for i in res:
        data.append(
            {
                "id":i.id,
                "date":i.date,
                "complaint":i.complaint,
                "reply":i.reply,
                "reply_date":i.reply_date,
            }
        )
    return JsonResponse({"status":"ok","data":data})