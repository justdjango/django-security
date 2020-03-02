
# from django.contrib.auth.middleware import AuthenticationMiddleware
# from django.utils.deprecation import MiddlewareMixin < 1.10


class PaymentSessionMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_request(self, request):
        return None

    def process_view(self, request, view_func, view_args, view_kwargs):
        # if request.user.feedback_required:
        #     return redirect("feedback")
        return None
