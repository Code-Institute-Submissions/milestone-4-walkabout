from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from .forms import EditRoundForm, EditStreetForm, EditAddressForm
from .models import Round, Street, Address


# Create your views here.
def all_rounds(request):
    """
    Get all the delivery rounds from the database, ordered by name.
    """
    rounds = Round.objects.all().order_by('name')
    return render(request, 'rounds.html', {'rounds': rounds})


def create_or_edit_round(request, pk=None):
    """
    A view to create or edit a round depending on whether its
    primary key is null or not.
    """
    round = get_object_or_404(Round, pk=pk) if pk else None
    if request.method == 'POST':
        form = EditRoundForm(request.POST, instance=round)
        if form.is_valid():
            form.save()
            return redirect(all_rounds)
    else:
        form = EditRoundForm(instance=round)

    if round is None:
        # If no data found then invoke page to add round.
        operation_type = 'add'
    else:
        # Otherwise invoke page to edit round.
        operation_type = 'edit'

    return render(request, operation_type + '_round.html', {'form': form})


class RoundDelete(DeleteView):
    """
    Delete the round and return to Rounds page after delete confirmation.
    """
    model = Round
    template_name = 'round_confirm_delete.html'
    success_url = reverse_lazy('all_rounds')


def all_streets(request):
    """
    Get all the streets from the database, ordered by name.
    """
    streets = Street.objects.all().order_by('name')

    return render(request, 'streets.html', {'streets': streets})


def create_or_edit_street(request, pk=None):
    """
    A view to create or edit a street depending on whether its
    primary key is null or not.
    """
    street = get_object_or_404(Street, pk=pk) if pk else None
    if request.method == 'POST':
        form = EditStreetForm(request.POST, instance=street)
        if form.is_valid():
            form.save()
            return redirect(all_streets)
    else:
        form = EditStreetForm(instance=street)

    if street is None:
        # If no data found then invoke page to add street.
        operation_type = 'add'
    else:
        # Otherwise invoke page to edit street.
        operation_type = 'edit'

    return render(request, operation_type + '_street.html', {'form': form})


class StreetDelete(DeleteView):
    """
    Delete the street and return to Streets page after delete confirmation.
    """
    model = Street
    template_name = 'street_confirm_delete.html'
    success_url = reverse_lazy('all_streets')


def attached_streets(request, pk):
    """
    Show the streets linked to this particular round, ordered by street name.
    """
    round = Round.objects.all().filter(id=pk)
    streets = Street.objects.select_related('round').filter(round=pk).order_by('name')

    return render(request, 'attached_streets.html', {'round': round, 'streets': streets})


def create_addresses(request, pk):
    """
    Create the addresses for this street, deleting any old ones first.
    """
    # Delete any addresses already existing for this street.
    addresses_exist = Address.objects.select_related('name').filter(name=pk).order_by('door_number')
    if addresses_exist:
        addresses_exist.delete()

    # Create a record for each new address and save to the database.
    street = Street.objects.get(id=pk)
    comments = ""
    door_end = street.door_number_end + 1
    for door_number in range(1, door_end):
        address = Address(door_number=door_number, name=street, comments=comments)
        address.save()

    # Select the addresses just saved to display in template.
    addresses = Address.objects.select_related('name').filter(name=pk).order_by('door_number')
    return render(request, 'addresses.html', {'street': street, 'addresses': addresses})


def view_addresses(request, pk):
    """"
    View the addresses for this street.
    """
    street = Street.objects.get(id=pk)
    addresses = Address.objects.select_related('name').filter(name=pk).order_by('door_number')
    return render(request, 'addresses.html', {'street': street, 'addresses': addresses})


def edit_address(request, pk, pk2):
    """
    Edit the comments field only for this addresses.
    """
    street = get_object_or_404(Street, pk=pk)
    address = get_object_or_404(Address, pk=pk2)
    if request.method == 'POST':
        form = EditAddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect(view_addresses, pk)
    else:
        form = EditAddressForm(instance=address)

    return render(request, 'edit_address.html', {'street': street, 'address': address, 'form': form})