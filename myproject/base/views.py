from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

@login_required(login_url='login')
def home(request):
    flight_data=flightmodel.objects.all()
    if 'search' in  request.GET:
        q=request.GET['search']
        flight_data=flightmodel.objects.filter(Q(flight_company__icontains=q) | Q(flight_name__icontains=q))
        
    if not flight_data.exists():
        return HttpResponse("No data found")
    return render (request,'home.html',{'data':flight_data})

@login_required(login_url='login')
def booking(request):
    data=Bookingmodel.objects.all()
    return render(request,'booking.html',{"bookingdata":data})

@login_required(login_url='login')
def history(request):
    cancel_data=historymodel.objects.all()
    confirm_data=Bookingmodel.objects.all()
    return render(request,'history.html',{'hist_data':cancel_data,'confirm_data':confirm_data})

@login_required(login_url='login')
def support(request):
    return render(request,'support.html')

def about(request):
    return render(request,'about.html')

@login_required(login_url='login')
def booking_form(request,id):
    data=flightmodel.objects.get(id=id)
    if request.method=='POST':
        pname=request.POST['pname']
        pemail=request.POST['pemail']
        p_phone_no=request.POST['p_phone_no']
        p_Adhar_no=request.POST['p_Adhar_no']
        p_age=request.POST['p_age']
        p_seat_class=request.POST['p_seat_class']
        seat_num=request.POST['seat_num']
        Bookingmodel.objects.create(
        flight_company=data.flight_company,
        flight_name=data.flight_name,
        flight_number=data.flight_number,
        flight_from=data.flight_from,
        flight_to=data.flight_to,
        flight_depaturetime=data.flight_depaturetime,
        flight_date=data.flight_date,
        flight_price=data.flight_price,
        pname=pname,
        pemail=pemail,
        p_phone_no=p_phone_no,
        p_Adhar_no=p_Adhar_no,
        p_age=p_age,
        p_seat_class=p_seat_class,
        seat_num=seat_num,
    )
        return redirect('booking')
    return render(request,'book_now.html',{'data':data})

@login_required(login_url='login')
def update_booking(request,id):
    data=Bookingmodel.objects.get(id=id)
    if request.method=='POST':
        pname=request.POST['pname']
        pemail=request.POST['pemail']
        p_phone_no=request.POST['p_phone_no']
        p_Adhar_no=request.POST['p_Adhar_no']
        p_age=request.POST['p_age']
        p_seat_class=request.POST['p_seat_class']
        seat_num=request.POST['seat_num']
        data.pname=pname
        data.pemail=pemail
        data.p_phone_no=p_phone_no
        data.p_Adhar_no=p_Adhar_no
        data.p_age=p_age
        data.p_seat_class=p_seat_class
        data.seat_num=seat_num
        data.save()
        return redirect('booking')
    return render(request,'update.html',{'bookingdata':data})

@login_required(login_url='login')
def cancel_booking(request,id):
    data=Bookingmodel.objects.get(id=id)
    historymodel.objects.create(
        flight_company=data.flight_company,
        flight_name=data.flight_name,
        flight_number=data.flight_number,
        flight_from=data.flight_from,
        flight_to=data.flight_to,
        flight_depaturetime=data.flight_depaturetime,
        flight_date=data.flight_date,
        flight_price=data.flight_price,
        pname=data.pname,
        pemail=data.pemail,
        p_phone_no=data.p_phone_no,
        p_Adhar_no=data.p_Adhar_no,
        p_age=data.p_age,
        p_seat_class=data.p_seat_class,
        seat_num=data.seat_num,
    )
    data.delete()
    return redirect('history')
