from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mail.forms import NewsletterForm, MessageForm, ClientForm, NewsletterModeratorForm
from mail.models import Newsletter, Message, Client, Attempt
from mail.services import get_three_articles, get_blog_posts


def home(request):
    context = {'count_newsletters': Newsletter.objects.all().count(),
               'active_count_newsletters': Newsletter.objects.filter(is_active=True).count(),
               'count_clients': Client.objects.all().count(), 'blogs': get_three_articles()}

    return render(request, 'home.html', context=context)


class NewsletterListView(LoginRequiredMixin, ListView, UserPassesTestMixin):
    model = Newsletter
    template_name = 'newsletter_list.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.has_perm('mail.can_view_newsletter'):
            newsletters = Newsletter.objects.all()
        else:
            newsletters = Newsletter.objects.filter(owner=user)
        blog_posts = get_blog_posts()
        return newsletters | blog_posts
        # return list(newsletters) + blog_posts

    def test_func(self):
        user = self.request.user
        # Проверка на суперпользователя
        if user.is_superuser:
            return True
        # Проверка на модератора с правами
        if user.has_perm('mail.can_view_newsletter'):
            return True
        return False


    # def test_func(self):
    #     return self.request.user.has_perm('mail.can_view_newsletter')


class NewsletterDetailView(LoginRequiredMixin, DetailView):
    model = Newsletter


class NewsletterCreateView(LoginRequiredMixin, CreateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('mail:newsletter_list')

    def form_valid(self, form):
        newsletter = form.save()
        user = self.request.user
        newsletter.owner = user
        newsletter.save()

        return super().form_valid(form)


class NewsletterUpdateView(LoginRequiredMixin, UpdateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('mail:newsletter_list')

    # def get_form_class(self):
    #     user = self.request.user
    #     if user == self.object.owner:
    #         return NewsletterForm
    #     if user.has_perm('mail.can_block_newsletter') and user.perm('mail.can_view_newsletter'):
    #         return NewsletterModeratorForm
    #     raise PermissionDenied


class NewsletterDeleteView(LoginRequiredMixin, DeleteView):
    model = Newsletter
    success_url = reverse_lazy('mail:newsletter_list')


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mail:newsletter_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MessageListView(LoginRequiredMixin, ListView):
    model = Message

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Message.objects.all()
        else:
            return Message.objects.filter(owner=user)


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mail:message_list')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mail:message_list')


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Client.objects.all()
        else:
            return Client.objects.filter(owner=user)


class ClientCreateView(CreateView, LoginRequiredMixin):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail:client_list')

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()

        return super().form_valid(form)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail:client_list')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mail:client_list')


class AttemptListView(ListView):
    model = Attempt
    template_name = 'mail/attempt_list.html'
    context_object_name = 'attempts'
