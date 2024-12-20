import os

from django import forms
from django.conf import settings
from django.contrib import admin
from django.utils.html import mark_safe
from dotenv import load_dotenv

from application.services.site_service import get_domain_service
from domain.user.sites.site_service import SiteServiceInterface
from infrastructure.persistence.models.user.idea import Idea, IdeaScreen
from infrastructure.persistence.models.user.product import UserProduct
from infrastructure.persistence.models.user.roles import Roles, SuperUserRole
from infrastructure.persistence.models.user.site import Site
from infrastructure.persistence.models.user.user import User
from infrastructure.persistence.repositories.user_repository import get_user_repository
from web.admin.admin import redirect_to_change_page_tag
from web.common.admin import BaseInline


class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "phone", "email", "register_on", "email_is_confirmed"]
    exclude = ["password", "staff", "is_superuser"]

    def register_on(self, obj, domain_service: SiteServiceInterface = get_domain_service()):
        return domain_service.get_register_on_site(obj)

    register_on.short_description = "зарегистрирован на"
    register_on.allow_tags = True


class UserRoleInlineForm(forms.ModelForm):
    email = forms.CharField(label="Почта", required=False)

    class Meta:
        model = SuperUserRole
        fields = ["email"]

    repository = get_user_repository()

    def clean(self):
        cleaned_data = self.cleaned_data
        if "email" not in cleaned_data:
            cleaned_data["email"] = cleaned_data["id"].user.email

        return cleaned_data


class SuperUserRoleInline(BaseInline):
    model = SuperUserRole
    form = UserRoleInlineForm

    fields = ["user", "email", "phone"]
    readonly_fields = fields

    def email(self, user_role):
        return user_role.user.email

    def phone(self, user_role):
        return user_role.user.phone

    def has_add_permission(self, request, *args, **kwargs):
        return False

    def has_delete_permission(self, request, *args, **kwargs):
        return True


class AddSuperUserRoleInline(BaseInline):
    model = SuperUserRole
    form = UserRoleInlineForm

    def has_change_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return False


class RolesAdmin(admin.ModelAdmin):
    inlines = [SuperUserRoleInline, AddSuperUserRoleInline]

    repository = get_user_repository()

    def save_related(self, request, form, formsets, change):
        try:
            # Ваша кастомная логика сохранения
            for formset in formsets:
                for obj_ind, obj in enumerate(formset.save(commit=False)):
                    email = formset.cleaned_data[0].get("email")
                    user = self.repository.get_user_by_email(email)

                    if user:
                        obj.user = user
                        obj.save()
                    else:
                        obj.delete()
        except Exception as e:
            print(e)

        super().save_related(request, form, formsets, change)


class IdeaScreenInline(BaseInline):
    model = IdeaScreen

    def image_tag(self, screen):
        return mark_safe(
            '<a href="#" class="open-image-popup" data-image="%s"><img src="%s" width="100" /></a>'
            % (screen.screen.url, screen.screen.url)
        )

    image_tag.allow_tags = True
    image_tag.short_description = "Скрин"

    fields = ["image_tag"]
    readonly_fields = fields


load_dotenv()


class IdeaAdmin(admin.ModelAdmin):
    model = Idea
    list_display = ["status_img", "created_at_tag", "title_tag", "user", "status", "finishe_date_tag", "rating"]

    admin_site_url = os.getenv("ADMIN_URL")

    def title_tag(self, idea):
        return redirect_to_change_page_tag(idea, idea.title)

    def finishe_date_tag(self, idea):
        if idea.finishe_date:
            return idea.finishe_date.strftime("%d.%m.%Y")

        return "---"

    def created_at_tag(self, idea):
        return idea.created_at.strftime("%d.%m.%Y")

    def status_img(self, idea):
        if idea.category == "errors":
            src = f"{settings.STATIC_URL}account/images/bugs/icobug_error.png"
        elif idea.category == "correction":
            src = f"{settings.STATIC_URL}account/images/bugs/icobug_fix.png"
        elif idea.category == "modernization":
            src = f"{settings.STATIC_URL}account/images/bugs/icobug_addon.png"
        elif idea.category == "new_feature":
            src = f"{settings.STATIC_URL}account/images/bugs/icobug_idea.png"

        return mark_safe(f'<img width="15" src="{src}" />')

    title_tag.short_description = "Тема"
    status_img.short_description = ""
    created_at_tag.short_description = "Дата"
    finishe_date_tag.short_description = "Срок"

    readonly_fields = ["title", "description", "rating"]

    change_form_template = "common/screen_inline.html"

    def rating(self, idea):
        return idea.likes.count()

    rating.short_description = "Рейтинг"

    inlines = [IdeaScreenInline]

    def get_fieldsets(self, request, obj):
        fieldsets = (
            (
                None,
                {
                    "fields": (
                        "user",
                        "title",
                        "category",
                        "rating",
                        "status",
                        "finishe_date",
                        "description",
                        "admin_answer",
                    ),
                },
            ),
        )
        return fieldsets


class SiteAdmin(admin.ModelAdmin):
    exclude = ["online_from"]


admin.site.register(User, UserAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(UserProduct)
admin.site.register(Idea, IdeaAdmin)
admin.site.register(Roles, RolesAdmin)
