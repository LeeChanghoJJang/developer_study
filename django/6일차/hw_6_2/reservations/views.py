from django.shortcuts import render,redirect
from .models import Reservation
from .forms import ReservationForm

# Create your views here.
def index(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'reservations/index.html', context)

def new(request):
    form = ReservationForm()
    context = {
        'form':form,
    }
    return render(request,'reservations/new.html',context)

def create(request):
    form =ReservationForm(request.POST)
    if request.method =='POST':
        # form의 유효성 검사 : 에러 메시지를 포함한 폼
        if form.is_valid():
            # form을 저장함 ==> return 값은 article 객체를 반환
            reservation = form.save()
            return redirect('reservations:index')
    else: # POST가 아닐 때 (GET은 중요하지 않음)
        form = ReservationForm()
    context = {
        'form':form,
    }
    return render(request,'reservations/create.html')