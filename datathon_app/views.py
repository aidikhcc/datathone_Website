from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Participant, Sponsor
from .forms import RegistrationForm

class HomeView(TemplateView):
    template_name = 'datathon_app/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sponsors'] = Sponsor.objects.filter(is_active=True)[:6]  # Show top 6 sponsors
        return context

class AboutView(TemplateView):
    template_name = 'datathon_app/about.html'

class RegistrationView(CreateView):
    template_name = 'datathon_app/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('registration_success')
    
    def form_valid(self, form):
        # Calculate fee before saving
        participant = form.save(commit=False)
        fee = participant.calculate_fee()
        
        # Save the participant
        participant.save()
        
        # Store fee in session for success page
        self.request.session['registration_fee'] = fee
        
        messages.success(
            self.request,
            'Registration successful! Please complete your payment of ${:.2f}'.format(fee)
        )
        return super().form_valid(form)

class RegistrationSuccessView(TemplateView):
    template_name = 'datathon_app/registration_success.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fee'] = self.request.session.get('registration_fee', 0)
        # Add bank details (these should be moved to settings in production)
        context['bank_details'] = {
            'bank_name': 'Your Bank Name',
            'account_holder': 'KHCC Foundation',
            'account_number': 'XXXX-XXXX-XXXX-XXXX',
            'swift_code': 'XXXXXXXX',
        }
        return context

class SocialActivitiesView(TemplateView):
    template_name = 'datathon_app/social_activities.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activities'] = [
            {
                'name': 'Wadi Rum + Petra Trip',
                'date': 'April 15-16, 2025',
                'description': 'Experience the magic of Wadi Rum desert and the ancient city of Petra.',
                'image': 'images/wadi-rum.jpg',
            },
            {
                'name': 'Falafel Abujbarah Dinner',
                'date': 'April 12, 2025 - 7:00 PM',
                'description': 'Enjoy traditional Jordanian cuisine at the famous Falafel Abujbarah.',
                'image': 'images/falafel.jpg',
            },
            {
                'name': 'Kickboxing Session',
                'date': 'April 12, 2025 (Day 2)',
                'description': 'Energize yourself with a fun kickboxing session at KHCC.',
                'image': 'images/kickboxing.jpg',
            },
        ]
        return context

class FAQView(TemplateView):
    template_name = 'datathon_app/faq.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['faqs'] = [
            {
                'question': 'What is the registration fee?',
                'answer': 'The Datathon fee is $100, Workshop fee is $50, or both for $150. Jordanian participants receive a 50% discount.'
            },
            {
                'question': 'How do I join the Wadi Rum + Petra trip?',
                'answer': 'You can select this option during registration. Details about additional costs will be sent after registration.'
            },
            {
                'question': 'Is the kickboxing session mandatory?',
                'answer': 'No, it\'s an optional activity to help participants stay energized during the event.'
            },
            {
                'question': 'What should I bring to the event?',
                'answer': 'Bring your laptop, charger, and comfortable clothing. For the kickboxing session, bring appropriate workout attire.'
            },
            {
                'question': 'How do I access the MIMIC database?',
                'answer': 'Access details will be provided after registration is confirmed and necessary agreements are signed.'
            },
        ]
        return context

class SponsorsView(ListView):
    template_name = 'datathon_app/sponsors.html'
    model = Sponsor
    context_object_name = 'sponsors'
    
    def get_queryset(self):
        return Sponsor.objects.filter(is_active=True).order_by('tier', 'name')

class ContactView(TemplateView):
    template_name = 'datathon_app/contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_info'] = {
            'email': 'info@khccdatathon.jo',
            'phone': '+962 XXXX XXXX',
            'address': 'King Hussein Cancer Center, Amman, Jordan',
        }
        return context
