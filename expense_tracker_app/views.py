from django.contrib.auth import authenticate, login, logout 
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import Transactions_form
from .models import Transactions
from django.db.models import Sum
from django.shortcuts import get_object_or_404

# Create your views here.


def register(request):
    
    if request.method == 'POST':
        user_name = request.POST.get('user_name','').strip()
        password = request.POST.get('password','').strip()
        email = request.POST.get('email','').strip()
        password2 = request.POST.get('password2','').strip()
        
        if not user_name or   not email or  not password or  not password2:
             print(request.POST)
             messages.warning(request,'All fields are required!')
             return redirect('register')
       
            
        if User.objects.filter(username=user_name).exists():
           messages.error(request, 'Username already exist')
           return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'The email already exist')
            return redirect('register')
        
        if password == password2:
             User.objects.create_user(username=user_name, password=password, email=email)
             messages.success(request,'Account created successfully')
             return redirect('login_view')
        else:
             messages.error(request, "Passwords do not match")
             return redirect('register')

    return render(request,'register.html') 




def login_view(request):
    
    if request.method =='POST':
        username = request.POST.get('username')
        usrepassword = request.POST.get('usre_password')
            
        if not username or not usrepassword:
            messages.warning(request, 'All fields are required!')
            return redirect('login_view')
            
        user = authenticate(request, username = username, password = usrepassword)
        
        if user :
            login(request, user)
            messages.success(request,'Login successfull')
            return redirect('dashboard')
        else:
            messages.error(request,'invalid username or password')
            
            return redirect('login_view')
    
    
    return render(request,'login.html')


def user_logout(request):
    logout(request)
    return redirect('login_view')

@login_required(login_url='login_view')
def dashboard(request):
    
    transactions = Transactions.objects.filter(user = request.user)
    total_income = transactions.filter(type='Income').aggregate(Sum('amount'))['amount__sum'] or 0
    tottal_expense = transactions.filter(type='Expense').aggregate(Sum('amount'))['amount__sum'] or 0
    total_balance = total_income - tottal_expense
    
    recent_transaction = transactions.order_by('-date')[:3]
    context = {
        'income':total_income,
        'expense':tottal_expense,
        'balance':total_balance,
        'recent_transaction':recent_transaction,
    }
    return render(request,'dashboard.html',context)


@login_required
def add_transaction(request):

    if request.method == 'POST':
        form = Transactions_form(request.POST)

        if form.is_valid():
            transaction = form.save(commit=False)
            print(request.user)
            transaction.user = request.user
            transaction.save()
            messages.success(request,'Transaction added successfully')
            return redirect('add_transaction')
          

    else:
        form = Transactions_form()   

    return render(request, 'add_transaction.html', {'form': form})
@login_required
def transaction_list(request):
    transactions = Transactions.objects.filter(user =request.user)
    return render(request,'transaction_list.html',{'data':transactions})


@login_required
def dlt_data(request):
    pk = request.GET.get('pk')
    
    dlt = get_object_or_404(Transactions, id=pk)
    dlt.delete()
    messages.success(request,' Row deleted successfully')
    return redirect('transaction_list')
    