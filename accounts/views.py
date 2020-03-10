from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import PaymentSessionRequiredMixin


# @login_required
def home(request):

    request.session['test'] = '1234'
    request.session['payment_id'] = 348329482
    request.session.set_test_cookie()
    if request.method == "POST":

        # session = Session.objects.get(pk='2qbixpobhkcdt7s7ewb6x646b4v9vp72')
        # print(session.session_key)
        # print(session.session_data)
        # print(session.expire_date)
        # print(session.get_decoded())

        test = request.session['test']
        print(test)

        # if request.session.test_cookie_worked():
        #     request.session.delete_test_cookie()
        #     return HttpResponse("You're logged in")
        # else:
        #     return HttpResponse("Your browser does not support cookies")
    return render(request, "home.html")


def session_requiring_view(request, payment_id):
    if int(payment_id) == 348329482:  # the users payment id - linked with some foreignkey
        return HttpResponse("Your payment id is here")
    return HttpResponse("Your payment id is not here")

    # if request.session.get('payment_id', None) is not None:
    #     return HttpResponse("Your payment id is here")
    # return HttpResponse("Your payment id is not here")


class LoginRequiredHomeView(PaymentSessionRequiredMixin, generic.TemplateView):
    template_name = 'home.html'
