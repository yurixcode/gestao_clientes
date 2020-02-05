#Django
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Mixins
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

#Django Generic Views
from django.views.generic.list import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

#Models
from .models import Person
from produtos.models import Produto

#Forms
from .forms import PersonForm

# Utils
from django.utils import timezone
from django.urls import reverse_lazy


@login_required
def persons_list(request):
    persons = Person.objects.filter()
    return render(request, 'person.html', {'persons': persons})


@login_required
def persons_new(request):
    if not request.user.has_perm('clientes.add_person'):
        return HttpResponse('No autorizado')
        
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)


    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'person': person})


class PersonList(LoginRequiredMixin, ListView):
    model = Person


class PersonDetailView(LoginRequiredMixin, DetailView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
        

class PersonCreateView(CreateView):
    model = Person
    fields = '__all__'
    success_url = '/clientes/person_list/'


class PersonUpdateView(UpdateView):
    model = Person
    fields = '__all__'
    success_url = reverse_lazy('person_list_cbv')


class PersonDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('clientes.deletar_clientes',)
    raise_exception = True
    model = Person
    # success_url = reverse_lazy('person_list_cbv')
    
    def get_success_url(self):
        return reverse_lazy('person_list_cbv')


class ProductoBulk(View):
    def get(self, request):
        produtos = ['Banana', 'Maca', 'Limao', 'Pera', 'Melancia']
        lista_produtos = []

        for produto in produtos:
            p = Produto(descricao=produto, preco=10)
            lista_produtos.append(p)

        print(lista_produtos)
        Produto.objects.bulk_create(lista_produtos)

        return HttpResponse('Works!!')
