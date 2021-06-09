from django.views.generic.base import TemplateView
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import Permission
from django.contrib.auth.mixins import LoginRequiredMixin
import stripe


stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

class OrdersView(LoginRequiredMixin, TemplateView):
    template_name = 'orders/purchase.html'
    login_url = 'account_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context


def charge(request):
    permission = Permission.objects.get(codename='special_status')

    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=3900,
            currency='usd',
            description='Purchase all books',
            source=request.POST['stripeToken']
        )

        user = request.user
        user.user_permissions.add(permission)

        return render(request, 'orders/charge.html')
