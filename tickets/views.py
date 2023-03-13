from django.shortcuts import render, redirect
from .models import Ticket


def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'ticket_list.html', {'tickets': tickets})


def create_ticket(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        ticket = Ticket(title=title, description=description)
        ticket.save()
        return redirect('ticket_list')
    return render(request, 'create_ticket.html')


def close_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.is_closed = True
    ticket.save()
    return redirect('ticket_list')
