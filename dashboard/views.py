from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from campaign.models import Campaign
from round.models import Street


# Create your views here.
def dashboard(request):
    """
    A view that displays the dashboard page. The dashboard shows the campaign tasks
    assigned to each Agent.
    """
    # Select all active campaigns with attached rounds
    campaigns = Campaign.objects.all().filter(inactive_date__isnull=True).order_by('id')
    streets = Street.objects.all().order_by('round', 'name')

    return render(request, "dashboard.html",  {'campaigns': campaigns, 'streets': streets})


def assign_user_to_campaign(request, pk):
    """
    A view that assigns a user to a campaign.
    """
    campaign = Campaign.objects.get(pk=pk)
    campaign.assigned_users.add(request.user)

    messages.add_message(request, messages.INFO, 'User ' + str(request.user) +
                         ' added to Campaign: ' + str(campaign))

    return redirect(reverse('dashboard'))


def start_tasks(request, pk):
    """
    A view that gets the campaign and round data to physically start the campaign.
    Called from the Dashboard page.
    """
    campaign = Campaign.objects.get(pk=pk)
    return render(request, "start_tasks.html", {'campaign': campaign})
