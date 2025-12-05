from django.contrib import admin
from .models import Category, University, Program, UserProfile, SavedUniversity


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


class ProgramInline(admin.TabularInline):
    model = Program
    extra = 1


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "uni_type", "tuition_min", "tuition_max", "has_grants", "rating")
    list_filter = ("city", "uni_type", "has_grants", "language_kz", "language_ru", "language_en")
    search_fields = ("name", "short_name")
    inlines = [ProgramInline]


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "full_name", "planned_year", "my_gpa", "my_ielts", "my_ent")


@admin.register(SavedUniversity)
class SavedUniversityAdmin(admin.ModelAdmin):
    list_display = ("user", "university", "in_calculator", "created_at")
    list_filter = ("in_calculator",)