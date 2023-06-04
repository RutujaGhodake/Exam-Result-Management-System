from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import stdata,hscdata,degreedata,degree2data,degree3data,btechdata,btech2data,btech3data,btech4data
import faker
fake = faker.Faker()

@login_required(login_url='Login')
def mainpage(request):
    return render(request,'mainpage.html')

@login_required(login_url='Login')
def ssc(request):
    if request.method == 'POST':
        d=request.POST.get('htno')
        return redirect('result',d)
    else:
        return render(request, 'ssc.html')

@login_required(login_url='Login')
def result(request,d):
    u = stdata.objects.filter(htno=d).exists()
    if u == True:
        data = stdata.objects.get(htno=d)
        m=(data.marathi+ data.hindi+data.english+data.math+data.science+data.ssci)
        per=(m//6)
        if data.marathi >= 35 and data.hindi >= 35 and data.english >= 35 and data.math >= 35 and data.science >= 35 and data.ssci >= 35:
            if m>=210 and m<308:
                context = {'data': data, 're': 'Pass', 'g':'D','m':m,'per':per}
                return render(request, 'result.html',context)
            if m>=308 and m<406:
                context = {'data': data, 're': 'Pass', 'g':'C','m':m,'per':per}
                return render(request, 'result.html',context)
            if m>=406 and m<504:
                context = {'data': data, 're': 'Pass', 'g':'B','m':m, 'per':per}
                return render(request, 'result.html',context)
            if m>=504 and m<600:
                context = {'data': data, 're': 'Pass', 'g': 'A', 'm': m, 'per': per}
                return render(request, 'result.html', context)
        else:
            context = {'data': data, 're': 'Fail', 'g':'E','m':m, 'per':per}
            return render(request, 'result.html',context)
    else:
        messages.info(request, 'Invalid Hall Ticket No', extra_tags="1")
    return redirect('ssc')


@login_required(login_url='Login')
def hsc(request):
    if request.method == 'POST':
        d=request.POST.get('htno')
        return redirect('hscresult',d)
    else:
        return render(request, 'hsc.html')

@login_required(login_url='Login')
def hscresult(request,d):
    u = hscdata.objects.filter(htno=d).exists()
    if u == True:
        data = hscdata.objects.get(htno=d)
        m=(data.english+data.marathi+ data.math+ data.physics+ data.chemistry+ data.biology)
        per=(m//6)
        if data.marathi >= 35 and data.math >= 35 and data.english >= 35 and data.physics >= 35 and data.chemistry >= 35 and data.biology >= 35:
            if m >= 210 and m < 308:
                context = {'data': data, 're': 'Pass', 'g': 'D', 'm': m, 'per': per}
                return render(request, 'hscresult.html', context)
            if m >= 308 and m < 406:
                context = {'data': data, 're': 'Pass', 'g': 'C', 'm': m, 'per': per}
                return render(request, 'hscresult.html', context)
            if m >= 406 and m < 504:
                context = {'data': data, 're': 'Pass', 'g': 'B', 'm': m, 'per': per}
                return render(request, 'hscresult.html', context)
            if m >= 504 and m < 600:
                context = {'data': data, 're': 'Pass', 'g': 'A', 'm': m, 'per': per}
                return render(request, 'hscresult.html', context)
        else:
            context = {'data': data, 're': 'Fail', 'g': 'E', 'm': m, 'per': per}
            return render(request, 'hscresult.html', context)
    else:
        messages.info(request, 'Invalid Hall Ticket No', extra_tags="2")
        return redirect('hsc')

@login_required(login_url='Login')
def degree(request):
    if request.method == 'POST':
        d=request.POST.get('htno')
        return redirect('degreeresult',d)
    else:
        return render(request, 'degree.html')

@login_required(login_url='Login')
def degreeresult(request,d):
    u = degreedata.objects.filter(htno=d).exists()
    if u == True:
        data = degreedata.objects.get(htno=d)
        m=(data.bcomm+ data.pm+ data.c+ data.dbms+ data.stat)
        per=(m//5)
        if data.bcomm >= 35 and data.pm >= 35 and data.c >= 35 and data.dbms >= 35 and data.stat >= 35:
            if m>=175 and m<256:
                context = {'data': data, 're': 'Pass', 'g':'D','m':m,'per':per}
                return render(request, 'degreeresult.html',context)
            if m>=256 and m<337:
                context = {'data': data, 're': 'Pass', 'g':'C','m':m,'per':per}
                return render(request, 'degreeresult.html',context)
            if m>=337 and m<418:
                context = {'data': data, 're': 'Pass', 'g':'B','m':m, 'per':per}
                return render(request, 'degreeresult.html',context)
            if m>=418 and m<500:
                context = {'data': data, 're': 'Pass', 'g':'A','m':m, 'per':per}
                return render(request, 'degreeresult.html',context)
        else:
            context = {'data': data, 're': 'Fail', 'g':'E','m':m, 'per':per}
            return render(request, 'degreeresult.html',context)
    else:
        messages.info(request, 'Invalid Hall Ticket No', extra_tags="3")
        return redirect('degree')

@login_required(login_url='Login')
def degree2(request):
    if request.method == 'POST':
        d=request.POST.get('htno')
        return redirect('degree2result',d)
    else:
        return render(request, '2degree.html')

@login_required(login_url='Login')
def degree2result(request,d):
    u = degree2data.objects.filter(htno=d).exists()
    if u == True:
        data = degree2data.objects.get(htno=d)
        m=(data.dm+ data.ds+ data.se+ data.php+ data.bd)
        per=(m//5)
        if data.dm >= 35 and data.ds >= 35 and data.se >= 35 and data.php >= 35 and data.bd >= 35:
            if m >= 175 and m < 256:
                context = {'data': data, 're': 'Pass', 'g': 'D', 'm': m, 'per': per}
                return render(request, 'degree2result.html', context)
            if m >= 256 and m < 337:
                context = {'data': data, 're': 'Pass', 'g': 'C', 'm': m, 'per': per}
                return render(request, 'degree2result.html', context)
            if m >= 337 and m < 418:
                context = {'data': data, 're': 'Pass', 'g': 'B', 'm': m, 'per': per}
                return render(request, 'degree2result.html', context)
            if m >= 418 and m < 500:
                context = {'data': data, 're': 'Pass', 'g': 'A', 'm': m, 'per': per}
                return render(request, 'degree2result.html', context)
        else:
            context = {'data': data, 're': 'Fail', 'g': 'E', 'm': m, 'per': per}
            return render(request, 'degree2result.html', context)
    else:
        messages.info(request, 'Invalid Hall Ticket No', extra_tags="4")
        return redirect('2degree')

@login_required(login_url='Login')
def degree3(request):
    if request.method == 'POST':
        d=request.POST.get('htno')
        return redirect('degree3result',d)
    else:
        return render(request, '3degree.html')

@login_required(login_url='Login')
def degree3result(request,d):
    u = degree3data.objects.filter(htno=d).exists()
    if u == True:
        data = degree3data.objects.get(htno=d)
        m=(data.st+ data.rit+ data.java+ data.android+ data.project)
        per=(m//5)
        if data.st >= 35 and data.rit >= 35 and data.java >= 35 and data.android >= 35 and data.project >= 35:
            if m >= 175 and m < 256:
                context = {'data': data, 're': 'Pass', 'g': 'D', 'm': m, 'per': per}
                return render(request, 'degree3result.html', context)
            if m >= 256 and m < 337:
                context = {'data': data, 're': 'Pass', 'g': 'C', 'm': m, 'per': per}
                return render(request, 'degree3result.html', context)
            if m >= 337 and m < 418:
                context = {'data': data, 're': 'Pass', 'g': 'B', 'm': m, 'per': per}
                return render(request, 'degree3result.html', context)
            if m >= 418 and m < 500:
                context = {'data': data, 're': 'Pass', 'g': 'A', 'm': m, 'per': per}
                return render(request, 'degree3result.html', context)
        else:
            context = {'data': data, 're': 'Fail', 'g': 'E', 'm': m, 'per': per}
            return render(request, 'degree3result.html', context)
    else:
        messages.info(request, 'Invalid Hall Ticket No', extra_tags="5")
        return redirect('3degree')

@login_required(login_url='Login')
def btech(request):
    if request.method == 'POST':
        d=request.POST.get('htno')
        return redirect('btechresult',d)
    else:
        return render(request, 'btech.html')

@login_required(login_url='Login')
def btechresult(request,d):
    u = btechdata.objects.filter(htno=d).exists()
    if u == True:
        data = btechdata.objects.get(htno=d)
        m=(data.eng+ data.ap+ data.math+ data.cit+ data.sdc+ data.cds)
        per=(m//6)
        if data.eng >= 35 and data.ap >= 35 and data.math >= 35 and data.cit >= 35 and data.sdc >= 35 and data.cds >= 35:
            if m >= 210 and m < 308:
                context = {'data': data, 're': 'Pass', 'g': 'D', 'm': m, 'per': per}
                return render(request, 'btechresult.html', context)
            if m >= 308 and m < 406:
                context = {'data': data, 're': 'Pass', 'g': 'C', 'm': m, 'per': per}
                return render(request, 'btechresult.html', context)
            if m >= 406 and m < 504:
                context = {'data': data, 're': 'Pass', 'g': 'B', 'm': m, 'per': per}
                return render(request, 'btechresult.html', context)
            if m >= 504 and m < 600:
                context = {'data': data, 're': 'Pass', 'g': 'A', 'm': m, 'per': per}
                return render(request, 'btechresult.html', context)
        else:
            context = {'data': data, 're': 'Fail', 'g': 'E', 'm': m, 'per': per}
            return render(request, 'btechresult.html', context)
    else:
        messages.info(request, 'Invalid Hall Ticket No', extra_tags="6")
        return redirect('btech')

@login_required(login_url='Login')
def btech2(request):
    if request.method == 'POST':
        d = request.POST.get('htno')
        return redirect('btech2result', d)
    else:
        return render(request, 'btech2.html')

@login_required(login_url='Login')
def btech2result(request, d):
    u = btech2data.objects.filter(htno=d).exists()
    if u == True:
        data = btech2data.objects.get(htno=d)
        m = (data.co + data.itm + data.et + data.dc + data.ps + data.opr)
        per = (m // 6)
        if data.co >= 35 and data.itm >= 35 and data.et >= 35 and data.dc >= 35 and data.ps >= 35 and data.opr >= 35:
            if m >= 210 and m < 308:
                context = {'data': data, 're': 'Pass', 'g': 'D', 'm': m, 'per': per}
                return render(request, 'btech2result.html', context)
            if m >= 308 and m < 406:
                context = {'data': data, 're': 'Pass', 'g': 'C', 'm': m, 'per': per}
                return render(request, 'btech2result.html', context)
            if m >= 406 and m < 504:
                context = {'data': data, 're': 'Pass', 'g': 'B', 'm': m, 'per': per}
                return render(request, 'btech2result.html', context)
            if m >= 504 and m < 600:
                context = {'data': data, 're': 'Pass', 'g': 'A', 'm': m, 'per': per}
                return render(request, 'btech2result.html', context)
        else:
            context = {'data': data, 're': 'Fail', 'g': 'E', 'm': m, 'per': per}
            return render(request, 'btech2result.html', context)
    else:
        messages.info(request, 'Invalid Hall Ticket No', extra_tags="7")
        return redirect('btech2')

@login_required(login_url='Login')
def btech3(request):
    if request.method == 'POST':
        d = request.POST.get('htno')
        return redirect('btech3result', d)
    else:
        return render(request, 'btech3.html')

@login_required(login_url='Login')
def btech3result(request, d):
    u = btech3data.objects.filter(htno=d).exists()
    if u == True:
        data = btech3data.objects.get(htno=d)
        m = (data.ca + data.ai + data.nf + data.wn + data.dsa + data.ipl)
        per = (m // 6)
        if data.ca >= 35 and data.ai >= 35 and data.nf >= 35 and data.wn >= 35 and data.dsa >= 35 and data.ipl >= 35:
            if m >= 210 and m < 308:
                context = {'data': data, 're': 'Pass', 'g': 'D', 'm': m, 'per': per}
                return render(request, 'btech3result.html', context)
            if m >= 308 and m < 406:
                context = {'data': data, 're': 'Pass', 'g': 'C', 'm': m, 'per': per}
                return render(request, 'btech3result.html', context)
            if m >= 406 and m < 504:
                context = {'data': data, 're': 'Pass', 'g': 'B', 'm': m, 'per': per}
                return render(request, 'btech3result.html', context)
            if m >= 504 and m < 600:
                context = {'data': data, 're': 'Pass', 'g': 'A', 'm': m, 'per': per}
                return render(request, 'btech3result.html', context)
        else:
            context = {'data': data, 're': 'Fail', 'g': 'E', 'm': m, 'per': per}
            return render(request, 'btech3result.html', context)
    else:
        messages.info(request, 'Invalid Hall Ticket No', extra_tags="8")
        return redirect('btech3')

@login_required(login_url='Login')
def btech4(request):
    if request.method == 'POST':
        d = request.POST.get('htno')
        return redirect('btech4result', d)
    else:
        return render(request, 'btech4.html')

@login_required(login_url='Login')
def btech4result(request, d):
    u = btech4data.objects.filter(htno=d).exists()
    if u == True:
        data = btech4data.objects.get(htno=d)
        m = (data.se + data.sm + data.java + data.mc + data.ds + data.pr)
        per = (m // 6)
        if data.se >= 35 and data.sm >= 35 and data.java >= 35 and data.mc >= 35 and data.ds >= 35 and data.pr >= 35:
            if m >= 210 and m < 308:
                context = {'data': data, 're': 'Pass', 'g': 'D', 'm': m, 'per': per}
                return render(request, 'btech4result.html', context)
            if m >= 308 and m < 406:
                context = {'data': data, 're': 'Pass', 'g': 'C', 'm': m, 'per': per}
                return render(request, 'btech4result.html', context)
            if m >= 406 and m < 504:
                context = {'data': data, 're': 'Pass', 'g': 'B', 'm': m, 'per': per}
                return render(request, 'btech4result.html', context)
            if m >= 504 and m < 600:
                context = {'data': data, 're': 'Pass', 'g': 'A', 'm': m, 'per': per}
                return render(request, 'btech4result.html', context)
        else:
            context = {'data': data, 're': 'Fail', 'g': 'E', 'm': m, 'per': per}
            return render(request, 'btech4result.html', context)
    else:
        messages.info(request, 'Invalid Hall Ticket No', extra_tags="9")
        return redirect('btech4')

@login_required(login_url='Login')
def generatedata(request):
    for i in range(20):
        stdata(
            fname=fake.first_name(),
            lname=fake.last_name(),
            htno=fake.random_element(elements=range(10001, 20000)),
            marathi=fake.random_element(elements=range(36, 100)),
            hindi=fake.random_element(elements=range(36, 100)),
            english=fake.random_element(elements=range(36, 100)),
            math=fake.random_element(elements=range(1, 100)),
            science=fake.random_element(elements=range(36, 100)),
            ssci=fake.random_element(elements=range(36, 100))
        ).save()
    return render(request,'ssc.html')

@login_required(login_url='Login')
def generatehsc(request):
    for i in range(20):
        hscdata(
            fname=fake.first_name(),
            lname=fake.last_name(),
            htno=fake.random_element(elements=range(20001, 30000)),
            english=fake.random_element(elements=range(36, 100)),
            marathi=fake.random_element(elements=range(36, 100)),
            math=fake.random_element(elements=range(1, 100)),
            physics=fake.random_element(elements=range(36, 100)),
            chemistry=fake.random_element(elements=range(36, 100)),
            biology=fake.random_element(elements=range(36, 100))
        ).save()
    return render(request,'hsc.html')

@login_required(login_url='Login')
def generatedegree(request):
    for i in range(20):
        degreedata(
            fname=fake.first_name(),
            lname=fake.last_name(),
            htno=fake.random_element(elements=range(30001, 40000)),
            bcomm=fake.random_element(elements=range(36, 100)),
            pm=fake.random_element(elements=range(36, 100)),
            c=fake.random_element(elements=range(1, 100)),
            dbms=fake.random_element(elements=range(36, 100)),
            stat=fake.random_element(elements=range(36, 100)),
        ).save()
    return render(request,'degree.html')

@login_required(login_url='Login')
def generatedegree2(request):
    for i in range(20):
        degree2data(
            fname=fake.first_name(),
            lname=fake.last_name(),
            htno=fake.random_element(elements=range(40001, 50000)),
            dm=fake.random_element(elements=range(36, 100)),
            ds=fake.random_element(elements=range(1, 100)),
            se=fake.random_element(elements=range(36, 100)),
            php=fake.random_element(elements=range(36, 100)),
            bd=fake.random_element(elements=range(36, 100)),
        ).save()
    return render(request,'degree.html')

@login_required(login_url='Login')
def generatedegree3(request):
    for i in range(20):
        degree3data(
            fname=fake.first_name(),
            lname=fake.last_name(),
            htno=fake.random_element(elements=range(50001, 60000)),
            st=fake.random_element(elements=range(36, 100)),
            rit=fake.random_element(elements=range(36, 100)),
            java=fake.random_element(elements=range(1, 100)),
            android=fake.random_element(elements=range(36, 100)),
            project=fake.random_element(elements=range(36, 100)),
        ).save()
    return render(request,'degree.html')

@login_required(login_url='Login')
def generatebtech(request):
    for i in range(20):
        btechdata(
            fname=fake.first_name(),
            lname=fake.last_name(),
            htno=fake.random_element(elements=range(60001, 70000)),
            eng=fake.random_element(elements=range(36, 100)),
            ap=fake.random_element(elements=range(36, 100)),
            math=fake.random_element(elements=range(36, 100)),
            cit=fake.random_element(elements=range(36, 100)),
            sdc=fake.random_element(elements=range(1, 100)),
            cds=fake.random_element(elements=range(36, 100))
        ).save()
    return render(request,'btech.html')

@login_required(login_url='Login')
def generatebtech2(request):
    for i in range(20):
        btech2data(
            fname=fake.first_name(),
            lname=fake.last_name(),
            htno=fake.random_element(elements=range(70001, 80000)),
            co=fake.random_element(elements=range(36, 100)),
            itm=fake.random_element(elements=range(36, 100)),
            et=fake.random_element(elements=range(36, 100)),
            dc=fake.random_element(elements=range(36, 100)),
            ps=fake.random_element(elements=range(1, 100)),
            opr=fake.random_element(elements=range(36, 100))
        ).save()
    return render(request,'btech2.html')

@login_required(login_url='Login')
def generatebtech3(request):
    for i in range(20):
        btech3data(
            fname=fake.first_name(),
            lname=fake.last_name(),
            htno=fake.random_element(elements=range(80001, 90000)),
            ca=fake.random_element(elements=range(36, 100)),
            ai=fake.random_element(elements=range(36, 100)),
            nf=fake.random_element(elements=range(36, 100)),
            wn=fake.random_element(elements=range(36, 100)),
            dsa=fake.random_element(elements=range(1, 100)),
            ipl=fake.random_element(elements=range(36, 100))
        ).save()
    return render(request,'btech3.html')

@login_required(login_url='Login')
def generatebtech4(request):
    for i in range(20):
        btech4data(
            fname=fake.first_name(),
            lname=fake.last_name(),
            htno=fake.random_element(elements=range(90001, 100000)),
            se=fake.random_element(elements=range(36, 100)),
            sm=fake.random_element(elements=range(36, 100)),
            java=fake.random_element(elements=range(36, 100)),
            mc=fake.random_element(elements=range(36, 100)),
            ds=fake.random_element(elements=range(1, 100)),
            pr=fake.random_element(elements=range(36, 100))
        ).save()
    return render(request,'btech4.html')


def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 == pass2:
            try:
                user = User.objects.get(username=uname)
                messages.info(request, 'Username already exists',extra_tags="sign3")
            except User.DoesNotExist:
                if ('@' or '!' or '#' or '$' or '%' or '^' or '&' or '*') not in pass1:
                    messages.info(request,'Password must contain atleast 1 special character',extra_tags="sign4")
                else:
                    myuser = User.objects.create_user(uname, email, pass1)
                    myuser.save()
                    messages.success(request, 'Account is created successfully', extra_tags="sign1")
                    return redirect('Login')
        else:
            messages.info(request, 'Your password and confirm password are not same!!',extra_tags="sign2")
    return render(request, 'signup.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
                login(request, user)
                return redirect('mainpage')
        else:
            messages.info(request,'Username or password is not correct',extra_tags="log")
    return render(request, 'login.html')

def Logout(request):
    logout(request)
    return redirect('Login')

