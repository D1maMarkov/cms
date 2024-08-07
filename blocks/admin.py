from adminsortable2.admin import SortableAdminBase, SortableStackedInline
from django.contrib import admin
from django.utils.safestring import mark_safe

from blocks.models.blocks import (
    ContentBlock,
    Cover,
    FeaturesBlock,
    Navbar,
    QuestionsBlock,
    RegisterBlock,
    SocialMediaBlock,
    StagesBlock,
)
from blocks.models.blocks_components import (
    AdditionalCatalogProductType,
    CatalogProduct,
    CatalogProductType,
    Feature,
    NavMenuItem,
    Question,
    SocialMediaButton,
    Stage,
)
from blocks.models.catalog_block import (
    AdditionalCatalogBlock,
    CatalogBlock,
    MainPageCatalogBlock,
    PromoCatalog,
)
from blocks.models.common import Block, BlockRelationship, Page, Template
from common.admin import BaseInline
from styles.admin import (
    AdditionalCatalogCustomStylesInline,
    CatalogCustomStylesInline,
    ContentCustomStylesInline,
    CoverCustomStylesInline,
    FeaturesCustomStylesInline,
    MainPageCatalogCustomStylesInline,
    NavbarCustomStylesInline,
    PromoCatalogCustomStylesInline,
    QuestionsCustomStylesInline,
    RegisterCustomStylesInline,
    SocialCustomStylesInline,
    StagesCustomStylesInline,
)
from user.admin import UserAdmin
from user.models import User


class QuestionInline(BaseInline):
    model = Question


class NavMenuItemAdmin(BaseInline):
    model = NavMenuItem


class FeatureInline(BaseInline):
    model = Feature


class SocialMediaButtonInline(BaseInline):
    model = SocialMediaButton


class StageInline(BaseInline):
    model = Stage


class PageBlockInline(SortableStackedInline, BaseInline):
    model = Block


class CatalogProductInline(SortableStackedInline, BaseInline):
    model = CatalogProduct


class MainPageCatalogProductInline(SortableStackedInline, BaseInline):
    model = CatalogProductType


class AdditionalCatalogProductInline(SortableStackedInline, BaseInline):
    model = AdditionalCatalogProductType


class TemplateAdmin(admin.ModelAdmin):
    list_display = ["name", "file"]


class BaseBlockAdmin(admin.ModelAdmin):
    change_form_template = "blocks/change_form.html"
    list_display = ["name", "template", "clone_button"]
    exclude = ["block_relation"]

    change_list_template = "blocks/change_list_page.html"

    def clone_button(self, obj):
        return mark_safe(
            f"""<button class="copy-button" onclick="cloneBlock({obj.id}, '{obj.__class__.__name__}')">Копировать</button>"""
        )

    clone_button.short_description = ""

    def delete_queryset(self, request, queryset):
        for block in queryset:
            relation_id = block.block_relation.id
            print(relation_id, "relation_id")
            BlockRelationship.objects.filter(id=relation_id).delete()
        queryset.delete()


class NavbarAdmin(BaseBlockAdmin):
    inlines = [NavMenuItemAdmin, NavbarCustomStylesInline]


class ContentAdmin(BaseBlockAdmin):
    inlines = [ContentCustomStylesInline]


class CoverAdmin(BaseBlockAdmin):
    inlines = [CoverCustomStylesInline]


class FeaturesBlockAdmin(BaseBlockAdmin):
    inlines = [FeatureInline, FeaturesCustomStylesInline]


class RegisterBlockAdmin(BaseBlockAdmin):
    inlines = [RegisterCustomStylesInline]


class SocialMediaBlockAdmin(BaseBlockAdmin):
    inlines = [SocialMediaButtonInline, SocialCustomStylesInline]


class QuestionsBlockAdmin(BaseBlockAdmin):
    inlines = [QuestionInline, QuestionsCustomStylesInline]


class StagesBlockAdmin(BaseBlockAdmin):
    inlines = [StageInline, StagesCustomStylesInline]


class CatalogAdmin(SortableAdminBase, BaseBlockAdmin):
    inlines = [CatalogProductInline, CatalogCustomStylesInline]
    exclude = BaseBlockAdmin.exclude


class MainPageCatalogBlogAdmin(SortableAdminBase, BaseBlockAdmin):
    inlines = [MainPageCatalogProductInline, MainPageCatalogCustomStylesInline]
    exclude = BaseBlockAdmin.exclude


class AdditionalCatalogBlogAdmin(SortableAdminBase, BaseBlockAdmin):
    inlines = [AdditionalCatalogProductInline, AdditionalCatalogCustomStylesInline]
    exclude = BaseBlockAdmin.exclude


class PromoCatalogAdmin(BaseBlockAdmin):
    inlines = [PromoCatalogCustomStylesInline]


class PageAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ["url", "title", "clone_button"]
    change_list_template = "blocks/change_list_page.html"

    inlines = [PageBlockInline]

    def clone_button(self, obj):
        return mark_safe(f'<button class="copy-button" onclick="clonePage({obj.id})">Копировать</button>')

    clone_button.short_description = ""


admin.site.register(User, UserAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Navbar, NavbarAdmin)
admin.site.register(Cover, CoverAdmin)
admin.site.register(RegisterBlock, RegisterBlockAdmin)
admin.site.register(PromoCatalog, PromoCatalogAdmin)
admin.site.register(MainPageCatalogBlock, MainPageCatalogBlogAdmin)
admin.site.register(AdditionalCatalogBlock, AdditionalCatalogBlogAdmin)
admin.site.register(CatalogBlock, CatalogAdmin)
admin.site.register(ContentBlock, ContentAdmin)
admin.site.register(FeaturesBlock, FeaturesBlockAdmin)
admin.site.register(StagesBlock, StagesBlockAdmin)
admin.site.register(SocialMediaBlock, SocialMediaBlockAdmin)
admin.site.register(QuestionsBlock, QuestionsBlockAdmin)
admin.site.register(Template, TemplateAdmin)
