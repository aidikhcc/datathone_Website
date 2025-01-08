from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

class Participant(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected'),
    ]
    
    EVENT_CHOICES = [
        ('datathon', 'Datathon Only'),
        ('workshop', 'Workshop Only'),
        ('both', 'Both Events'),
    ]

    # Personal Information
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    nationality = models.CharField(max_length=50)
    
    # Event Selection
    event_choice = models.CharField(max_length=10, choices=EVENT_CHOICES)
    payment_status = models.CharField(
        max_length=10,
        choices=PAYMENT_STATUS_CHOICES,
        default='pending'
    )
    
    # Skills (stored as comma-separated values)
    skills = models.TextField(
        help_text="Comma-separated list of skills (e.g., Python, R, Statistics)"
    )
    
    # Social Media (all optional)
    slack_username = models.CharField(max_length=50, blank=True)
    discord_username = models.CharField(max_length=50, blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.CharField(max_length=50, blank=True)
    
    # Social Activities
    wadi_rum_trip = models.BooleanField(default=False)
    falafel_dinner = models.BooleanField(default=False)
    kickboxing_session = models.BooleanField(default=False)
    
    # Timestamps
    registration_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def calculate_fee(self):
        """Calculate the registration fee based on nationality and event choice."""
        base_fees = {
            'datathon': 100,
            'workshop': 50,
            'both': 150,
        }
        
        base_fee = base_fees[self.event_choice]
        
        # 50% discount for Jordanians
        if self.nationality.lower() == 'jordanian':
            return base_fee * 0.5
        return base_fee
    
    def clean(self):
        """Validate the model data."""
        if not self.skills:
            raise ValidationError({'skills': 'Please specify at least one skill.'})
            
        # Ensure phone number is in a valid format
        if not self.phone.replace('+', '').replace('-', '').isdigit():
            raise ValidationError({'phone': 'Phone number can only contain digits, plus sign, and hyphens.'})
    
    def __str__(self):
        return f"{self.full_name} - {self.get_event_choice_display()}"
    
    class Meta:
        ordering = ['-registration_date']


class Sponsor(models.Model):
    TIER_CHOICES = [
        ('platinum', 'Platinum'),
        ('gold', 'Gold'),
        ('silver', 'Silver'),
        ('bronze', 'Bronze'),
    ]
    
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='sponsor_logos/')
    website = models.URLField()
    description = models.TextField()
    tier = models.CharField(max_length=10, choices=TIER_CHOICES)
    
    # Contact Information
    contact_person = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.get_tier_display()}"
    
    class Meta:
        ordering = ['tier', 'name']
