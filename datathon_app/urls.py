from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('registration/success/', views.RegistrationSuccessView.as_view(), name='registration_success'),
    path('social-activities/', views.SocialActivitiesView.as_view(), name='social_activities'),
    path('faq/', views.FAQView.as_view(), name='faq'),
    path('sponsors/', views.SponsorsView.as_view(), name='sponsors'),
    path('contact/', views.ContactView.as_view(), name='contact'),
] 