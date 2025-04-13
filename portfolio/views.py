from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ContactMessage
from .forms import ContactForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')
    else:
        form = ContactForm()
    
    return render(request, 'portfolio/index.html', {'form': form})

class MessageListView(LoginRequiredMixin, ListView):
    model = ContactMessage
    template_name = 'portfolio/messages.html'
    context_object_name = 'messages'
    ordering = ['-created_at']
    login_url = '/admin/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact Messages'
        return context
