from django import forms
from .models import Participant
from django.core.exceptions import ValidationError

class RegistrationForm(forms.ModelForm):
    # Additional fields for skills with checkboxes
    SKILL_CHOICES = [
        ('python', 'Python'),
        ('r', 'R'),
        ('statistics', 'Statistics'),
        ('machine_learning', 'Machine Learning'),
        ('data_visualization', 'Data Visualization'),
        ('previous_datathons', 'Previous Datathon Experience'),
    ]
    
    skill_choices = forms.MultipleChoiceField(
        choices=SKILL_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        help_text="Select all that apply"
    )
    
    # Terms and conditions
    terms_accepted = forms.BooleanField(
        required=True,
        label="I agree to the terms and conditions",
        help_text="You must accept the terms and conditions to register"
    )
    
    class Meta:
        model = Participant
        fields = [
            'full_name', 'email', 'phone', 'nationality',
            'event_choice', 'slack_username', 'discord_username',
            'linkedin', 'twitter', 'wadi_rum_trip', 'falafel_dinner',
            'kickboxing_session'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+XXX-XX-XXXXXXX'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control'}),
            'event_choice': forms.Select(attrs={'class': 'form-control'}),
            'slack_username': forms.TextInput(attrs={'class': 'form-control'}),
            'discord_username': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter': forms.TextInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'phone': 'Include country code (e.g., +962 for Jordan)',
            'nationality': 'As shown in your passport',
            'event_choice': 'Select which events you want to attend',
        }
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            # Remove any spaces or special characters except + and -
            phone = ''.join(c for c in phone if c.isdigit() or c in ['+', '-'])
            if not phone.replace('+', '').replace('-', '').isdigit():
                raise ValidationError('Phone number can only contain digits, plus sign, and hyphens.')
        return phone
    
    def clean(self):
        cleaned_data = super().clean()
        skills = cleaned_data.get('skill_choices')
        
        # Convert skill choices to comma-separated string for storage
        if skills:
            cleaned_data['skills'] = ', '.join(skills)
        
        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make some fields optional
        optional_fields = ['slack_username', 'discord_username', 'linkedin', 'twitter']
        for field in optional_fields:
            self.fields[field].required = False
        
        # Add Bootstrap classes to checkboxes
        for field in ['wadi_rum_trip', 'falafel_dinner', 'kickboxing_session']:
            self.fields[field].widget.attrs['class'] = 'form-check-input'
        
        # Add labels for social activities
        self.fields['wadi_rum_trip'].label = "Join Wadi Rum + Petra Trip (April 15-16)"
        self.fields['falafel_dinner'].label = "Join Falafel Abujbarah Dinner"
        self.fields['kickboxing_session'].label = "Join Kickboxing Session (Day 2)" 