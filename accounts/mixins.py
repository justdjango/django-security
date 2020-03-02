from django.core.exceptions import PermissionDenied


class PaymentSessionRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if 'payment_id' not in request.session:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
