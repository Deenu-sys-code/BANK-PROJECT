from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import random as rd,datetime as dt
from .models import Customer,User_Statements

# Create your views here.

def app_reg(request):

    if request.method == 'POST':
        obj = UserCreationForm(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect('app_log')
        else:
            messages.error(request,obj.errors)
            return render(request,'User_Registration.html',{'F':UserCreationForm()})
    else:
        return render(request,'User_Registration.html',{'F':UserCreationForm()})
    
def app_log(request):

    if request.method == 'POST':
        name = request.POST['My-Name']
        password = request.POST['My-Pass']
        user = authenticate(username = name ,password = password)
        if user is not None:# user = 'Appu'
            login(request,user)
            return redirect('UI')
        else:
            messages.error(request,'Invalid Credentials')
            return render(request,'User_Login.html')  
            
    else:
        return render(request,'User_Login.html')  
    

@login_required
def Customer_login(request):
    if request.method=='POST':
        ac_num=int(request.POST['Ac_num'])
        ph=int(request.POST['Ph_no'])
        obj=Customer.objects.filter(Ac_num=ac_num,Ph_number=ph)
        if obj.exists():
            request.session['ac']=ac_num
            return redirect('Bank_UI')
        else:
            messages.error(request,'Ac_num or Ph_no Invalid')
            return render(request,'Customer_login.html')
    else:
        return render(request,'Customer_login.html')

@login_required
def Customer_Creation(request):
    if request.method == 'POST':
        ac_num = int(request.POST['My-Ac'])
        nm = request.POST['My-Name']
        ph = int(request.POST['My-Ph'])
        obj = Customer(Ac_num = ac_num,Name = nm,Ph_number = ph)
        obj.save()
        return redirect('UI')
    else:
        ac_num=rd.randint(1000000000,9999999999)
        return render(request,'Customer_Creation.html',{'ac_num':ac_num})

@login_required
def Bank_UI(request):
    obj = Customer.objects.get(Ac_num = request.session['ac'])
    return render(request,'Bank_UI.html',{'cus':obj})

@login_required
def Home(request):
    obj = Customer.objects.get(Ac_num = request.session['ac'])
    return render(request,'home.html',{'cus':obj})

@login_required
def Deposit_Amount(request):
    obj = Customer.objects.get(Ac_num = request.session['ac'])
    if request.method == "POST":
        dpt_am = int(request.POST['Dpt'])
        obj.Balance = obj.Balance + dpt_am
        obj.save()
        his = User_Statements.objects.create(User=obj,
            History = f'Deposited on {dt.datetime.now().ctime()}',
            Amount = dpt_am)
        messages.success(request,'Deposited Succesfulll')
        return render(request,'Deposit.html')
    else:
        return render(request,'Deposit.html')

@login_required
def Withdrawn_amount(request):
    obj = Customer.objects.get(Ac_num=request.session['ac'])
    if request.method == "POST":
        wit_am = int(request.POST['wit'])
        obj.Balance = obj.Balance - wit_am
        obj.save()
        his = User_Statements.objects.create(User=obj,
            History = f'withdrawn on {dt.datetime.now().ctime()}',
            Amount = wit_am)
        messages.success(request,'Withdrawn Succesfulll')
        return render(request,'Withdrawn.html')
    else:
        return render(request,'Withdrawn.html')

@login_required
def Transaction_history(request):
   # select * from customer inner join user statement on acnum = ac_num where Ac_num = 78;
   obj = User_Statements.objects.filter(User__Ac_num = request.session['ac'])
   return render(request,'Transaction.html',{'get':obj})

@login_required
def Statement(request):
    obj = User_Statements.objects.filter(User__Ac_num = request.session['ac'])
    return render(request,'statement.html',{'state':obj})

@login_required
def Balance(request):
    obj = Customer.objects.get(Ac_num=request.session['ac']).Balance
    print(obj)
    return render(request,'balance.html',{'bal':obj})


@login_required
def Logout_user(request):
    logout(request)
    request.session['ac']=None
    return redirect('app_log')


