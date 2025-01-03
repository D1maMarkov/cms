from django.forms import Form
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from application.email_services.work_email_service.email_service_interface import (
    WorkEmailServiceInterface,
)
from infrastructure.email_services.work_email_service.email_service import (
    get_work_email_service,
)
from infrastructure.requests.request_interface import RequestInterface
from infrastructure.security import get_link_encryptor
from web.common.forms import FeedbackForm


class RedirectToLink(View):
    link_encryptor = get_link_encryptor()

    def get(self, request: HttpRequest) -> HttpResponse:
        tracker = self.request.GET.get("product")
        if tracker:
            link = self.link_encryptor.decrypt(tracker)
            if link:
                return HttpResponseRedirect(link)

        return HttpResponse(status=400)


@method_decorator(csrf_exempt, name="dispatch")
class FormView(View):
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(request, form, *args, **kwargs)

        return JsonResponse({"errors": form.errors}, status=400)

    def get_form(self) -> Form:
        return self.form_class(self.request.POST, self.request.FILES)

    def add_form_error(self, form: Form, exception):
        """Функция для добавления ошибки в форму на основании исключения."""
        error_field = self.error_mapping.get(type(exception))
        if error_field:
            form.add_error(error_field, str(exception))


class SendFeedbackView(FormView):
    email_service: WorkEmailServiceInterface = get_work_email_service()
    form_class = FeedbackForm

    def form_valid(self, request: RequestInterface, form: FeedbackForm) -> HttpResponse:
        self.email_service.send_feedback_email(
            site_name=request.site_name,
            site_domain=request.get_host(),
            username=form.cleaned_data.get("username"),
            phone=form.cleaned_data.get("phone"),
            email=form.cleaned_data.get("email"),
            message=form.cleaned_data.get("message"),
            user_id=request.user.id if request.user.is_authenticated else None,
        )

        return HttpResponse(status=200)
