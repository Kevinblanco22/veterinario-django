from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Owner, Pet, Appointment


class IndexView(generic.ListView):
    template_name = 'clinic/index.html'
    context_object_name = 'latest_pets_list'

    def get_queryset(self):
        return Pet.objects.select_related('owner').order_by('name')[:10]


class PetDetailView(generic.DetailView):
    model = Pet
    template_name = 'clinic/detail.html'


def book_appointment(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)

    if request.method == "POST":
        date = request.POST.get('date')
        reason = request.POST.get('reason')

        if date and reason:
            Appointment.objects.create(
                pet=pet,
                date=date,
                reason=reason,
            )
            return HttpResponseRedirect(
                reverse('clinic:pet_detail', args=(pet.id,))
            )

    return render(request, 'clinic/book_appointment.html', {'pet': pet})
