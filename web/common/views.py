from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from infrastructure.security import get_link_encryptor


class RedirectToLink(View):
    link_encryptor = get_link_encryptor()

    def get(self, request):
        tracker = self.request.GET.get("product")
        print(tracker)
        if tracker:
            link = self.link_encryptor.decrypt(tracker)
            print(link)
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

    def get_form(self):
        return self.form_class(self.request.POST, self.request.FILES)
