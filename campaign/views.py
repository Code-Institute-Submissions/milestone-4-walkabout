from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from .forms import EditCampaignForm
from .models import Campaign


# Create your views here.
def all_campaigns(request):
    """
    Get all the campaigns from the database, ordered by active date
    """
    campaigns = Campaign.objects.all().order_by('id')
    return render(request, 'campaigns.html', {'campaigns': campaigns})


def create_or_edit_campaign(request, pk=None):
    """
    A view to create or edit a campaign depending on whether its
    primary key is null or not.
    """
    campaign = get_object_or_404(Campaign, pk=pk) if pk else None
    if request.method == 'POST':
        form = EditCampaignForm(request.POST, instance=campaign)
        if form.is_valid():
            form.save()
            return redirect(all_campaigns)
    else:
        form = EditCampaignForm(instance=campaign)

    # If data found then invoke page to edit campaign, otherwise invoke page to add campaign.
    operation_type = 'edit' if campaign else 'add'

    return render(request, operation_type + '_campaign.html', {'form': form})


class CampaignDelete(DeleteView):
    """
    Delete the campaign and return to Campaigns page after delete confirmation.
    """
    model = Campaign
    template_name = 'campaign_confirm_delete.html'
    success_url = reverse_lazy('all_campaigns')
