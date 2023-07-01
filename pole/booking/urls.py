from django.urls import path
from . import views

urlpatterns = [
    path('', views.FieldFilterView, name='field_filter'),
    path('home', views.FieldFilterView, name='field_filter'),
    path('field/<slug:slug>/', views.FieldDetailView, name='field_detail'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('save_booking/<int:field_id>/', views.save_booking, name='save_booking'),
    path('my-bookings', views.myBookings, name='my_bookings'),
    path('field-bookings', views.fieldBookings, name='field_bookings'),
]