from django.shortcuts import render

# MAIN
def index(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")

# ACCOUNTS
def login_view(request):
    return render(request, "core/login.html")

def register_view(request):
    return render(request, "core/register.html")

def profile_view(request):
    return render(request, "core/profile.html")

# UNIVERSITIES
def university_list(request):
    return render(request, "core/university_list.html")

def university_detail(request, pk):
    return render(request, "core/university_detail.html")

# CALCULATOR
def calculator(request):
    return render(request, "core/calculator.html")

def calculator_result(request):
    return render(request, "core/calculator_result.html")

from django.shortcuts import render, get_object_or_404
from .models import University, Category


def home(request):
    category_slug = request.GET.get("category")
    limit = request.GET.get("limit")

    try:
        limit = int(limit) if limit is not None else 6
    except ValueError:
        limit = 6

    categories = Category.objects.all().order_by("name")

    qs = University.objects.prefetch_related("categories").order_by("-popularity_score")

    selected_category = None
    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        qs = qs.filter(categories=selected_category)

    total_count = qs.count()
    universities = qs[:limit]
    show_more = total_count > limit
    next_limit = limit + 6

    context = {
        "categories": categories,
        "selected_category": selected_category,
        "universities": universities,
        "show_more": show_more,
        "next_limit": next_limit,
        "total_count": total_count,
        "shown_count": len(universities),
    }
    return render(request, "core/index.html", context)