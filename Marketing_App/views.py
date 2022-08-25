import json
import time

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

from .models import *
from django.conf import settings
from datetime import date
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def logins(request):
    return render(request, 'login.html')

def logoutUser(request):
    if request.method == "GET" and (request.headers.get('x-requested-with') == 'XMLHttpRequest'):
        logout(request)
    return HttpResponse("Logout")

def page(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is None:
            return render(request, 'login.html')
        if user.is_super and user.is_active == True:
            login(request, user)
            return redirect('dashboard')
        if user.is_admin and user.is_active == True:
            login(request, user)
            return redirect('admin_dashboard')
        if user.is_client and user.is_active == True:
            login(request, user)
            return redirect('client_dashboard')
    return render(request, 'login.html')

def invoice(request):
    datas = product.objects.all()
    all_data_client = []
    for x in datas:
        all_data_client.append(x)
    return render(request, 'invoice.html', {'message': all_data_client})

def admin_register(request):
    if request.method == "GET" and (request.headers.get('x-requested-with') == 'XMLHttpRequest'):
        username = request.GET['username']
        email = request.GET['email']
        password = request.GET['password']
        mobile = request.GET['mobile']
        country = request.GET['country']
        state = request.GET['state']
        address = request.GET['address']
        print("Start")
        is_active = True
        is_admin = True
        user = NewUser(user_name=username, email=email, mobile=mobile, password=password,country=country, state=state, Address=address, is_admin=is_admin, is_active=is_active)
        user.set_password(password)
        # user.save()
        print("END")
        return HttpResponse(username)

def admin_details(request):
    data = NewUser.objects.all().order_by('-created_at')
    all_data_admin = []
    for x in data:
        if (x.is_admin == True):
            all_data_admin.append(x)
    return render(request, 'admin.html', {'message': all_data_admin})

def adminview(request, id):
    data = NewUser.objects.all()
    datas = Invoice.objects.all()
    all_data_admin = []
    all_data_invoice = []
    for x in data:
        if (x.id==id and x.is_admin == True):
            all_data_admin.append(x)
            for y in datas:
                if (x.user_name==y.customer):
                    all_data_invoice.append(y)
    return render(request, 'adminview.html', {'message': all_data_admin, 'messages': all_data_invoice})

def productlist(request):
    data = product.objects.all().order_by('-id')
    all_data_client = []
    for x in data:
        all_data_client.append(x)
    return render(request, 'productlist.html', {'message': all_data_client})

def add_product(request, id):
    print("HIIII")
    print(id)
    if request.method == "POST":
        name = request.POST['name']
        quantity = request.POST['quantity']
        price = request.POST['price']
        duration = request.POST['duration']
        description = request.POST['description']
        # product(name=name, quantity=quantity, price=price, duration=duration, description=description, user_id=id).save()
        time.sleep(2)
    return redirect('productlist')

def payment_details(request):
    data = Invoice.objects.all().order_by('-id')
    all_data_product = []
    for x in data:
        all_data_product.append(x)
    return render(request, 'payment_details.html',{'message': all_data_product})

def templates(request):
    data = fileuploads.objects.all()
    all_data_temp = []
    for x in data:
        all_data_temp.append(x)
    if request.method == "POST":
        templates = request.POST['name']
        file = request.FILES["file"]
        document = fileuploads.objects.create(file=file, templates=templates)
        document.save()
    return render(request, 'template.html', {'message': all_data_temp})

def settingss(request, id):
    data = invoice_settings.objects.all()
    all_data_setting = []
    for x in data:
        if x.user_id == id:
            all_data_setting.append(x)
    if request.method == "POST":
        username = request.POST['username']
        # password = request.POST['password']
        name = request.POST['companyname']
        email = request.POST['email']
        contactnumber = request.POST['contactnumber']
        gstin = request.POST['gstin']
        panno = request.POST['panno']
        website = request.POST['website']
        currency = request.POST['currency']
        # companylogo = request.FILES['companylogo']
        address = request.POST['address']
        bankname = request.POST['bankname']
        branchname = request.POST['branchname']
        accountname = request.POST['accountname']
        accounttype = request.POST['accounttype']
        bankaccountno = request.POST['bankaccountno']
        ifscno = request.POST['ifscno']
        heading = request.POST['heading']
        client = request.POST['client']
        price = request.POST['price']
        SubTotal = request.POST['subtotal']
        totalamount = request.POST['totalamount']
        thankyoumessage = request.POST['thankyoumessage']
        footernotes = request.POST['footernotes']
        print(footernotes)
        # stamp = request.FILES['stamp']
        termsandconditions = request.POST['termsandconditions']
        termsandconditionsdetails = request.POST['termsandconditionsdetails']
        # invoice_settings(CompanyName=name, email=email, ContactNumber=contactnumber,
        #                GSTIN=gstin, PanNo=panno, Website=website, Currency=currency,
        #                CompanyLogo=companylogo, Address=address, BankName=bankname, BranchName=branchname,
        #                AccountName=accountname, AccountType=accounttype,
        #                BankAccountNo=bankaccountno, IFSCNo=ifscno, Heading=heading
        #                ,Client=client, Price=price, SubTotal=SubTotal, TotalAmount=totalamount,
        #                ThankyouMassage=thankyoumessage, FooterNotes=footernotes, UploadYourCompanyStamp=stamp,
        #                TermsandConditions=termsandconditions, TermsandConditionsDetails=termsandconditionsdetails, user_id=id)#.save()
    return render(request, 'setting.html', {'message': all_data_setting})

def update_product(request):
    if request.method == "POST":
        idname = request.POST['idname']
        userid = request.POST['userid']
        name = request.POST['name']
        quantity = request.POST['quantity']
        price = request.POST['price']
        duration = request.POST['duration']
        description = request.POST['description']
        product.objects.filter(id=idname).update(name=name, quantity=quantity,price=price, duration=duration, description=description)
        time.sleep(2)
    return redirect('productlist')


def product_delete(request):
    if request.method == "GET" and (request.headers.get('x-requested-with') == 'XMLHttpRequest'):
        value = request.GET['value']
        # print(type(value))
        # product.objects.filter(id=int(value)).delete()
        return redirect('productlist')

def product_validity(request):
    if request.method == "GET" and (request.headers.get('x-requested-with') == 'XMLHttpRequest'):
        startdate = request.GET['startdate']
        duration = request.GET['duration']
        date = datetime.datetime.strptime(startdate, '%d-%m-%Y').strftime('%m/%d/%y')
        current_date_temp = datetime.datetime.strptime(date, "%m/%d/%y")
        again_date = current_date_temp + datetime.timedelta(days=int(duration))
        newdate = again_date.date()
        dates = datetime.datetime.strptime(str(newdate), '%Y-%m-%d').strftime('%d-%m-%y')
        return HttpResponse(dates)

def update_admin(request):
    if request.method == "POST":
        idname = request.POST['idname']
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        country = request.POST['country']
        state = request.POST['state']
        address = request.POST['address']
        status = request.POST['status']
        if status == "":
            print("HIIII")
            NewUser.objects.filter(id=idname).update(is_active=True)
            NewUser.objects.filter(id=idname).update(user_name=name, email=email, mobile=mobile, country=country,
                                                          state=state, Address=address, is_active=True)
        else:
            print("Hello")
            NewUser.objects.filter(id=idname).update(is_active=False)
            NewUser.objects.filter(id=idname).update(user_name=name, email=email,mobile=mobile, country=country,
                                                          state=state, Address=address,is_active=False)
        time.sleep(2)
    return redirect('admin_details')


def view_template(request, id):
    data = fileuploads.objects.all()
    for x in data:
        if x.id == id:
            tem = str(x.file)
            return render(request, "media/"+tem)

def temp_delete(request):
    if request.method == "GET" and (request.headers.get('x-requested-with') == 'XMLHttpRequest'):
        value = request.GET['value']
        print(value)
        print(type(value))
        # fileuploads.objects.filter(id=int(value)).delete()
        return redirect('templates')

def admin_buy_product(request):
    if request.method == "GET" and (request.headers.get('x-requested-with') == 'XMLHttpRequest'):
        username = request.GET['username']
        proname = request.GET['proname']
        proprice = request.GET['proprice']
        prodays = request.GET['prodays']
        proactive = request.GET['proactive']
        expiry_date = request.GET['expiry_date']
        payment = request.GET['payment']
        userid = request.GET['userid']
        data = product.objects.all()
        for x in data:
            if x.name == proname:
                quantity = x.quantity
                # Invoice(customer=username, productName=proname, price=proprice, duration=prodays,
                #         active_date=proactive, expiry_date=expiry_date, payment=payment,quantity=quantity,due_quantity=quantity, user_id=userid).save()
        return HttpResponse(username)


def invoice_letter(request, id):
    today = date.today()
    Date = today.strftime("%m/%d/%y")
    data = invoice_settings.objects.all()
    datas = Invoice.objects.all()
    all_data_setting = []
    all_data_invoice = []
    for x in data:
        all_data_setting.append(x)
    for x in datas:
        if x.id == id:
            all_data_invoice.append(x)
    return render(request, 'invoice_letter.html', {'message': all_data_setting, 'messages':all_data_invoice, 'Date': Date})

def dashboard(request):
    data = NewUser.objects.all()
    count = 0
    for x in data:
        if x.is_admin == True:
            count +=1
    return render(request, 'dashboard.html', {'message': count})

def clients(request):
    data = NewUser.objects.all().order_by('-created_at')
    all_data_user = []
    for x in data:
        all_data_user.append(x)
    return render(request, 'clients.html', {'message': all_data_user})

# Admin Part Views
def admin_dashboard(request):
    data = NewUser.objects.all()
    datas = customers.objects.all()
    all_data_user = []
    all_data_customer = []
    for x in data:
        if x.is_client == True :
            all_data_user.append(x)
    for y in datas:
        all_data_customer.append(y)
    return render(request, 'admin_dashboard.html', {'messages': all_data_user, 'message': all_data_customer})

def admin_invoice(request):
    datas = product.objects.all()
    all_data_product = []
    for x in datas:
        all_data_product.append(x)
    return render(request, 'admin_invoice.html', {'message': all_data_product})

def client_register(request):
    if request.method == "GET" and (request.headers.get('x-requested-with') == 'XMLHttpRequest'):
        username = request.GET['username']
        email = request.GET['email']
        password = request.GET['password']
        mobile = request.GET['mobile']
        country = request.GET['country']
        state = request.GET['state']
        address = request.GET['address']
        userid = request.GET['userid']
        print("Start")
        is_active = True
        is_client = True
        user = NewUser(user_name=username, email=email, mobile=mobile, password=password, country=country, state=state,
                       Address=address, is_client=is_client, is_active=is_active, admin_id=userid)
        user.set_password(password)
        user.save()
        print("END")
        return HttpResponse(username)


def admin_client(request):
    data = NewUser.objects.all().order_by('-id')
    all_data_client = []
    for x in data:
        all_data_client.append(x)
    return render(request, 'admin_client.html', {'message': all_data_client})

def admin_clientview(request, id):
    data = NewUser.objects.all()
    datas = Invoice.objects.all()
    all_data_admin = []
    all_data_invoice = []
    for x in data:
        if (x.id == id and x.is_client == True):
            all_data_admin.append(x)
            for y in datas:
                if (x.user_name == y.customer):
                    all_data_invoice.append(y)
    return render(request, 'admin_clientview.html', {'message': all_data_admin, 'messages': all_data_invoice})

def update_client(request):
    if request.method == "POST":
        idname = request.POST['idname']
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        country = request.POST['country']
        state = request.POST['state']
        address = request.POST['address']
        status = request.POST['status']
        if status == "":
            print("HIIII")
            NewUser.objects.filter(id=idname).update(is_active=True)
            NewUser.objects.filter(id=idname).update(user_name=name, email=email, mobile=mobile, country=country,
                                                     state=state, Address=address, is_active=True)
        else:
            print("Hello")
            NewUser.objects.filter(id=idname).update(is_active=False)
            NewUser.objects.filter(id=idname).update(user_name=name, email=email, mobile=mobile, country=country,
                                                     state=state, Address=address, is_active=False)
        time.sleep(2)
    return redirect('admin_client')

def admin_productlist(request):
    data = Invoice.objects.all().order_by('-id')
    datas = product.objects.all().order_by('-id')
    all_data_invoice = []
    all_data_product = []
    for x in data:
        all_data_invoice.append(x)
    for y in datas:
        all_data_product.append(y)
    return render(request, 'admin_productlist.html', {'message': all_data_invoice, 'messages': all_data_product})

def admin_product(request, id):
    if request.method == "POST":
        name = request.POST['name']
        quantity = request.POST['quantity']
        price = request.POST['price']
        duration = request.POST['duration']
        description = request.POST['description']
        product(name=name, quantity=quantity, price=price, duration=duration, description=description,
                user_id=id).save()
        time.sleep(2)
    return redirect('admin_productlist')

def admin_update_product(request):
    if request.method == "POST":
        name = request.POST['name']
        quantity = request.POST['quantity']
        price = request.POST['price']
        duration = request.POST['duration']
        description = request.POST['description']
        product.objects.filter(name=name).update(name=name, quantity=quantity,price=price, duration=duration, description=description)
        time.sleep(2)
    return redirect('admin_productlist')

def admin_product_delete(request):
    if request.method == "GET" and (request.headers.get('x-requested-with') == 'XMLHttpRequest'):
        value = request.GET['value']
        print(value)
        # product.objects.filter(id=int(value)).delete()
    return redirect('admin_productlist')

def admin_payment_details(request):
    data = Invoice.objects.all().order_by('-id')
    all_data_product = []
    for x in data:
        all_data_product.append(x)
    return render(request, 'admin_payment_details.html', {'message': all_data_product})

def client_buy_product(request):
    user = NewUser.objects.all()
    data = product.objects.all()
    datas = Invoice.objects.all()
    if request.method == "GET" and (request.headers.get('x-requested-with') == 'XMLHttpRequest'):
        username = request.GET['username']
        proname = request.GET['proname']
        proprice = request.GET['proprice']
        prodays = request.GET['prodays']
        proactive = request.GET['proactive']
        expiry_date = request.GET['expiry_date']
        payment = request.GET['payment']
        userid = request.GET['userid']
        for x in data:
            if x.name == proname:
                quantity = x.quantity
                Invoice(customer=username, productName=proname, price=proprice, duration=prodays,
                        active_date=proactive, expiry_date=expiry_date, payment=payment,quantity=quantity,due_quantity=quantity, user_id=userid).save()
        for x in user:
            if x.id == id:
                name = x.user_name
                for y in datas:
                    if y.customer == name:
                        u = y.due_quantity
                        print(u)
                        for z in data:
                            if z.name == proname:
                                quantity = z.quantity
                                qty = u-quantity
                                Invoice.objects.filter(customer=name).update(due_quantity=qty)
        return HttpResponse(username)

def admin_customerlist(request):
    return render(request, 'admin_customerlist.html')


def admin_template(request):
    data = fileuploads.objects.all()
    all_data_file = []
    for x in data:
        all_data_file.append(x)
    return render(request, 'admin_template.html', {'message': all_data_file})


def admin_setting(request):
    return render(request, 'admin_setting.html')

# Client Part Views
def client_dashboard(request):
    data = customers.objects.all().count()
    datas = group.objects.all().count()
    Datas = fileuploads.objects.all().count()
    print(data)
    return render(request, 'client_dashboard.html', {'data': data, 'datas': datas, 'Datas': Datas})

def client_productlist(request):
    data = Invoice.objects.all()
    all_data_invoice = []
    for x in data:
        all_data_invoice.append(x)
    return render(request, 'client_productlist.html', {'message': all_data_invoice})

def customerlist(request):
    datas = customers.objects.all().order_by('-id')
    all_data_email = []
    for y in datas:
        all_data_email.append(y)

    data = group.objects.all()
    all_data_group = []
    for x in data:
        all_data_group.append(x)
    return render(request, 'customerlist.html', {'message': all_data_group, 'messages': all_data_email})

def client_managegroup(request):
    data = group.objects.all()
    all_data_group = []
    for x in data:
        all_data_group.append(x)
    return render(request, 'client_managegroup.html', {'message': all_data_group})

def contact(request, id):
    print(id)
    if request.method == "POST":
        name = request.POST['name']
        group(name=name, cid=id).save()
    return redirect('client_managegroup')

def client_group_delete(request):
    if request.method == "GET" and (request.headers.get('x-requested-with') == 'XMLHttpRequest'):
        value = request.GET['value']
        print(value)
        group.objects.filter(id=int(value)).delete()
    return redirect('client_managegroup')

def client_template(request):
    data = fileuploads.objects.all().order_by('-id')
    all_data_file = []
    for x in data:
        all_data_file.append(x)

    data = template.objects.all()
    all_data_temp = []
    for x in data:
        all_data_temp.append(x)

    data = group.objects.all()
    all_data_group = []
    for x in data:
        all_data_group.append(x)

    return render(request, 'client_template.html', {'message': all_data_file, 'messages': all_data_temp, 'groups': all_data_group})


def client_template_details(request, cid):
    if request.method == "POST":
        fileid = request.POST['fileid']
        logo = request.FILES["logo"]
        companyurl = request.POST['companyurl']
        wtext = request.POST['wtext']
        title = request.POST['title']
        bname = request.POST['bname']
        buttonurl = request.POST['buttonurl']
        description = request.POST['description']
        copyright = request.POST['copyright']
        template.objects.create(logo=logo, logolink=companyurl, welcomeText=wtext, title=title, buttonname=bname,
                                buttonlink=buttonurl, description=description, copyright=copyright, user_id=cid, file_id=fileid).save()
        return render(request, 'client_template.html')

def send_email(request, uid):
    count = 0
    if request.method == "POST":
        ids = request.POST['fileids']
        check = request.POST.getlist('checks[]')
        subject = "HIIII"
        message = "Email"
        data = fileuploads.objects.all()
        datas = template.objects.all()
        datass = customers.objects.all()
        dues = Invoice.objects.all()
        user = NewUser.objects.all()
        for x in data:
            if x.id == int(ids):
                tem = str(x.file)
                email_from = settings.EMAIL_HOST_USER
                for a in check:
                    print(a)
                    for b in datass:
                        for c in b.checks:
                            if (c == a and b.user_id == uid):
                                print("HIII")
                                email = b.email
                                recipient_list = [email]
                                print(recipient_list)
                                for y in datas:
                                    if y.user_id == uid and y.file_id == int(ids):
                                        print("IN DATAS")
                                        logo = y.logo
                                        logolink = y.logolink
                                        welcomeText = y.welcomeText
                                        title = y.title
                                        description = y.description
                                        buttonname = y.buttonname
                                        buttonlink = y.buttonlink
                                        copyright = y.copyright
                                        html_message = render_to_string(
                                            '../templates/media/'+tem,
                                            {
                                                'logo': logo,
                                                'logolink': logolink,
                                                'welcomeText': welcomeText,
                                                'title': title,
                                                'description': description,
                                                'buttonname': buttonname,
                                                'buttonlink': buttonlink,
                                                'copyright': copyright,
                                            }
                                        )
                                        send_mail(subject, message, email_from, recipient_list, fail_silently=False, html_message=html_message)
                                        count = count + 1
                                        for x in user:
                                            if x.id == uid:
                                                name = x.user_name
                                                for y in dues:
                                                    if y.customer == name:
                                                        u = y.due_quantity
                                                        qty = u-count
                                                        Invoice.objects.filter(customer=name).update(due_quantity=qty)
                                                        print("END")
    return redirect('client_template')

def add_email(request, id):
    if request.method == "POST":
        customernames = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        state = request.POST['state']
        check = request.POST.getlist('checks[]')
        customers(name=customernames, email=email, mobile=mobile, state=state, checks=check, user_id=id).save()
        print("End")
    return redirect('customerlist')

def email_delete(request):
    if request.method == "GET" and (request.headers.get('x-requested-with') == 'XMLHttpRequest'):
        value = request.GET['value']
        print(value)
        # customers.objects.filter(id=int(value)).delete()
    return redirect('customerlist')


def update_client_template_details(request):
    if request.method == "GET" and (request.headers.get('x-requested-with') == 'XMLHttpRequest'):
        companyurl = request.GET['companyurl']
        wtext = request.GET['wtext']
        title = request.GET['title']
        bname = request.GET['bname']
        buttonurl = request.GET['buttonurl']
        description = request.GET['description']
        copyright = request.GET['copyright']
        fileid = request.GET['fileid']
        template.objects.filter(file_id=fileid).update(logolink=companyurl, welcomeText=wtext, title=title,  buttonname=bname, buttonlink=buttonurl, description=description, copyright=copyright)
    return HttpResponse("HIII")


# from Crypto.Cipher import AES
def passcode(request):
    data = NewUser.objects.all().order_by('-created_at')
    all_data_user = []
    for x in data:
        if x.is_staff == True:
            enc = x.password
            print(type(enc))
            # decoded_text = cipher_suite.decrypt(enc)
            # print(decoded_text)
    return render(request, 'login.html')