from django.conf import settings
from django.contrib import admin
from django.db.models import Max
from django.utils.html import mark_safe

from infrastructure.admin.admin_settings import get_admin_settings
from infrastructure.persistence.models.site_statistics import (
    PenaltyLog,
    SessionAction,
    SessionFilters,
    SessionFiltersHeader,
    SessionModel,
    TryLoginToAdminPanel,
    TryLoginToFakeAdminPanel,
    UserAction,
    UserActivity,
    WebSearcher,
    WebSearcherAction,
)
from web.admin.admin import redirect_to_change_page_tag
from web.common.admin import BaseInline


class UserActionInline(BaseInline):
    model = UserAction
    fields = ["action"]
    readonly_fields = fields

    @admin.display(description="")
    def action(self, obj):
        return f"""{obj.time.strftime('%d.%m %H:%M:%S')}:{r"     "}{obj.adress} - {obj.text}"""

    def has_delete_permission(self, *args, **kwargs) -> bool:
        return False

    def has_add_permission(self, *args, **kwargs) -> bool:
        return False


class BaseSessionAdmin(admin.ModelAdmin):
    admin_url = get_admin_settings().admin_url

    @admin.display(description="Дата", ordering="-start_time")
    def start_time_tag(self, obj):
        return obj.start_time.strftime("%d.%m %H:%M:%S")

    @admin.display(description="Время")
    def time_tag(self, obj):
        last_action = obj.actions.first()
        if last_action:
            end_time = last_action.time
        else:
            end_time = obj.start_time

        return str(end_time - obj.start_time).split(".")[0]

    @admin.display(description="")
    def device_tag(self, obj):
        src = f"""{settings.STATIC_URL}site_statistics/images/{"icoadm_desktop.png" if not obj.device else "icoadm_smart.png"}"""

        return mark_safe(f"""<img height="15" src={src} />""")

    @admin.display(description="ip")
    def ip_tag(self, obj):
        return redirect_to_change_page_tag(obj, obj.ip)

    @admin.display(description="Последнее действие", ordering="last_action")
    def last_action_tag(self, obj):
        last_action = obj.actions.first()
        if last_action:
            return last_action.time.strftime("%d.%m %H:%M:%S")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(last_action=Max("actions__time")).order_by("-last_action")

    class Media:
        css = {"all": ("site_statistics/css/user_action_admin.css",)}


class UserActivityAdmin(BaseSessionAdmin):
    inlines = [UserActionInline]

    fields = [
        "device_tag",
        "site_tag",
        "ip_tag",
        "user_tag",
        "start_time_tag",
        "time_tag",
        "pages_count",
        "banks_count",
        "profile_actions_count",
        "last_action_tag",
        "session_tag",
    ]

    def ip_tag(self, obj):
        return redirect_to_change_page_tag(obj, obj.session.ip)

    def device_tag(self, obj):
        src = f"""{settings.STATIC_URL}site_statistics/images/{"icoadm_desktop.png" if not obj.session.device else "icoadm_smart.png"}"""

        return mark_safe(f"""<img height="15" src={src} />""")

    def site_tag(self, obj):
        return obj.session.site

    @admin.display(description="сессия")
    def session_tag(self, obj):
        if obj.session:
            return redirect_to_change_page_tag(obj.session, obj.session.ban_rate)

        return "-"

    @admin.display(description="Пользователь")
    def user_tag(self, obj):
        if not obj.user:
            return "-"

        tag = obj.user.email
        if obj.auth == "login":
            tag += f"""<img src="{settings.STATIC_URL}site_statistics/images/icoadm_login.png" height=15 style="margin-left: 10px;" />"""

        if obj.auth == "register":
            tag += f"""<img src="{settings.STATIC_URL}site_statistics/images/icoadm_signup.png" height=15 style="margin-left: 10px;" />"""

        return mark_safe(tag)

    @admin.display(description="Стр.")
    def pages_count(self, session):
        return session.actions.filter(is_page=True).count()

    readonly_fields = fields

    list_display = fields


class SessionActionInline(BaseInline):
    model = SessionAction
    fields = ["action"]
    readonly_fields = fields

    @admin.display(description="")
    def action(self, obj):
        return f"""{obj.time.strftime('%d.%m %H:%M:%S')}:{obj.adress}"""

    def has_delete_permission(self, *args, **kwargs) -> bool:
        return False

    def has_add_permission(self, *args, **kwargs) -> bool:
        return False

    raw_id_fields = ["session"]

    def get_formset(self, request, obj=None, **kwargs):
        return super().get_formset(request, obj, **kwargs)


class PenaltylogAdmin(BaseInline):
    model = PenaltyLog
    fields = ["text"]
    readonly_fields = fields


class SessionModelAdmin(BaseSessionAdmin):
    inlines = [PenaltylogAdmin, SessionActionInline]

    fields = [
        "device_tag",
        "site",
        "ip_tag",
        "start_time_tag",
        "time_tag",
        "pages_count",
        "source_count",
        "hacking",
        "headers",
        "ban_rate",
        "last_action_tag",
    ]

    @admin.display(description="Стр.")
    def pages_count(self, session):
        return session.actions.filter(is_page=True).count()

    @admin.display(description="Ресурсы")
    def source_count(self, session):
        return session.actions.filter(is_source=True).count()

    readonly_fields = fields

    list_display = [field for field in fields if field != "headers"]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("actions")

    list_prefetch_related = [
        "actions",
    ]


class SessionHeaderInline(BaseInline):
    model = SessionFiltersHeader


class SessionFiltersAdmin(admin.ModelAdmin):
    inlines = [SessionHeaderInline]

    class Media:
        css = {"all": ("site_statistics/css/session_filters.css",)}


class WebSearcherActionInline(BaseInline):
    model = WebSearcherAction


class WebSearcherAdmin(BaseSessionAdmin):
    inlines = [WebSearcherActionInline]

    fields = [
        "site",
        "ip_tag",
        "start_time_tag",
        "time_tag",
        "headers",
        "last_action_tag",
    ]

    readonly_fields = fields

    list_display = [field for field in fields if field != "headers"]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("actions")

    list_prefetch_related = [
        "actions",
    ]


admin.site.register(TryLoginToAdminPanel)
admin.site.register(TryLoginToFakeAdminPanel)
admin.site.register(UserActivity, UserActivityAdmin)
admin.site.register(SessionModel, SessionModelAdmin)
admin.site.register(WebSearcher, WebSearcherAdmin)
admin.site.register(SessionFilters, SessionFiltersAdmin)
