from typing import Any

from django.template import loader

from web.blocks.template_exist import is_template_exists

from .tempate_context_processor.template_context_processor_interface import (
    TemplateContextProcessorInterface,
)
from .template_loader_interface import TemplateLoaderInterface


class TemplateLoader(TemplateLoaderInterface):
    def __init__(self, context_processor: TemplateContextProcessorInterface):
        self.context_processor = context_processor

    @staticmethod
    def load_template(app_name: str, template_name: str, request=None, context: dict[Any, Any] = None):
        if is_template_exists(f"{app_name}/{template_name}.html"):
            return loader.render_to_string(f"{app_name}/{template_name}.html", context, request, None)
        return None

    def load_change_user_form(self, request):
        context = self.context_processor.get_change_user_form_context(request)

        return self.load_template(app_name="common", template_name="change-user-form", request=request, context=context)

    def load_change_site_form(self, request):
        context = self.context_processor.get_change_site_form_context(request)

        return self.load_template(app_name="account", template_name="forms/site-form", request=request, context=context)

    def load_change_socials_form(self, request):
        context = self.context_processor.get_change_socials_form_context(request)

        return self.load_template(
            app_name="account", template_name="forms/socials-form", request=request, context=context
        )

    def load_referral_popup(self, request):
        context = self.context_processor.get_referral_popup_context(request)

        return self.load_template(
            app_name="account", template_name="popups/referral-popup", request=request, context=context
        )

    def load_choice_product_form(self, request):
        context = self.context_processor.get_choice_product_form(request)

        return self.load_template(
            app_name="account", template_name="forms/choice-product-form", request=request, context=context
        )

    def load_create_user_product_form(self, request):
        context = self.context_processor.get_create_user_product_form(request)

        return self.load_template(
            app_name="account",
            template_name="forms/update-or-create-user-product-form",
            request=request,
            context=context,
        )

    def load_product_description_popup(self, request):
        context = self.context_processor.get_product_description_popup(request)

        return self.load_template(
            app_name="account", template_name="popups/popup-description", request=request, context=context
        )

    def load_delete_product_popup(self, request):
        context = self.context_processor.get_delete_product_popup(request)

        return self.load_template(
            app_name="account", template_name="popups/delete-popup", request=request, context=context
        )

    def load_document_popup(self, request):
        context = self.context_processor.get_document_popup(request)

        return self.load_template(
            app_name="materials", template_name="document-popup", request=request, context=context
        )

    def load_create_idea_form(self, request):
        context = self.context_processor.get_create_idea_form(request)

        return self.load_template(
            app_name="account", template_name="forms/create-idea-form", request=request, context=context
        )


def get_template_loader(context_processor: TemplateContextProcessorInterface) -> TemplateLoaderInterface:
    return TemplateLoader(context_processor)
