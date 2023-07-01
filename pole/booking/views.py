from django.shortcuts import render, redirect
from .models import Field, Region, Booking
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
import datetime


# Create your views here.


def is_valid_queryparam(param):
    return param != '' and param is not None

def FieldFilterView(request):
    if request.user.is_authenticated and request.user.groups.filter(name='Owners'):
        return redirect('field_bookings')
    else:
        fields = Field.objects.all()
        regions = Region.objects.all()
        bookings = Booking.objects.all()
        title_contains_query = request.GET.get('title_contains')
        price_min = request.GET.get('price_min')
        price_max = request.GET.get('price_max')
        region = request.GET.get('region')

        if is_valid_queryparam(title_contains_query):
            fields = fields.filter(title__icontains=title_contains_query)

        if is_valid_queryparam(price_min):
            fields = fields.filter(price__gte=price_min)
        if is_valid_queryparam(price_max):
            fields = fields.filter(price__lt=price_max)

        if is_valid_queryparam(region) and region != 'Choose... ':
            fields = fields.filter(region__slug=region)

        context = {
            'fields': fields,
            'regions': regions,
            'bookings': bookings,
        }

        return render(request, 'booking/filter.html', context)
#

#
def FieldDetailView(request, slug):
    if request.user.is_authenticated and request.user.groups.filter(name='Owners'):
        return redirect('field_bookings')
    else:
        field = get_object_or_404(Field, slug=slug)
        bookings_all = Booking.objects.all()
        fields = Field.objects.all()
        bookings = bookings_all.filter(field__title=field.title)

        context = {
            'field': field,
            'bookings': bookings,
            'fields': fields,
        }
        return render(request, 'booking/field_detail.html', context)

def save_booking(request, field_id):
    field = Field.objects.get(pk=field_id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = request.POST
            date = data.get('date')
            date_day = date[0:2]
            date_month = date[3:5]
            date_year = date[6:10]
            date = f'{date_year}-{date_month}-{date_day}'
            time = data.get('time')
            time = time.replace(' ', '')[:-3]
            print(5555555555555, f'<{date}>', f'<{time}>', time.isdigit())

            if (date != '--' and time != '') or (time != ''):
                if time.isdigit():
                    bookings = Booking.objects.filter(user=request.user, field=field, date=date)
                    if len(bookings) < 5:
                        booking = Booking(user=request.user, field=field, date=date, time=time)
                        booking.save()
                        messages.info(request, 'Вы успешно забронировали поле!', extra_tags='success')
                    else:
                        messages.info(request, 'Нельзя бронировать больше 5 часов в день', extra_tags='error')
                else:
                    messages.info(request, 'Что бы забронировать, введите правильную дату и время', extra_tags='error')
            else:
                messages.info(request, 'Что бы забронировать, введите правильную дату и время', extra_tags='error')
    else:
        messages.info(request, 'Что бы забронировать, войдите в аккаунт', extra_tags='error')
    return redirect('field_detail', field.slug)


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})


def myBookings(request):
    if request.user.is_authenticated and request.user.groups.filter(name='Owners'):
        return redirect('field_bookings')
    else:
        if request.user.is_authenticated:
            if request.method == 'POST':
                booking_id = request.POST.get('booking-id')
                booking = Booking.objects.filter(id=booking_id).first()
                booking.delete()
                messages.success(request, 'Бронь успешон удалена!')
            bookings = Booking.objects.filter(user=request.user).order_by('-date', '-time')
            datetime_now = datetime.datetime.now()

            context = {
                'bookings': bookings,
                'datetime': datetime_now,
            }
            return render(request, 'booking/my_bookings.html', context)
        else:
            return render(request, 'booking/my_bookings.html')


def fieldBookings(request):
    if not request.user.is_authenticated or (request.user.is_authenticated and not request.user.groups.filter(name='Owners')):
        return redirect('field_filter')
    else:
        if request.method == 'POST':
            booking_id = request.POST.get('booking-id')
            booking = Booking.objects.filter(id=booking_id).first()
            booking.delete()
            messages.success(request, 'Бронь успешон удалена!')
        bookings = Booking.objects.filter(field__owner=request.user).order_by('-date', '-time')
        datetime_now = datetime.datetime.now()

        context = {
            'bookings': bookings,
            'datetime': datetime_now,
        }
        return render(request, 'booking/field_bookings.html', context)