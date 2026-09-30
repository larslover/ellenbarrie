from django.contrib import admin

from .models import (
    HeroSection,
    HistoryEntry,
    FarmingHero,
    FarmingUpdate,
    Child,
    School,
    HomeUpdate,
)


# ============================================================
# HERO SECTION
# ============================================================

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'is_active',
    )

    list_filter = (
        'is_active',
    )


# ============================================================
# HISTORY
# ============================================================

@admin.register(HistoryEntry)
class HistoryEntryAdmin(admin.ModelAdmin):

    list_display = (
        'year',
        'title',
        'order',
    )

    ordering = (
        'order',
        'year',
    )


# ============================================================
# FARMING HERO
# ============================================================

@admin.register(FarmingHero)
class FarmingHeroAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'is_active',
    )

    list_filter = (
        'is_active',
    )


# ============================================================
# FARMING UPDATES
# ============================================================

@admin.register(FarmingUpdate)
class FarmingUpdateAdmin(admin.ModelAdmin):

    list_display = (
        'date',
        'title',
        'order',
        'is_active',
    )

    list_filter = (
        'is_active',
    )

    ordering = (
        '-date',
        'order',
    )

# ============================================================
# CHILDREN
# ============================================================

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'age',
        'order',
        'is_active',
    )

    list_filter = (
        'is_active',
    )

    ordering = (
        'order',
        'name',
    )
# ============================================================
# GREEN VALLEY ENGLISH SCHOOL
# ============================================================

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "introduction",
        "address",
    )

# ============================================================
# HOME UPDATES
# ============================================================

@admin.register(HomeUpdate)
class HomeUpdateAdmin(admin.ModelAdmin):

    list_display = (
        "date",
        "category",
        "title",
        "is_active",
        "order",
    )

    list_filter = (
        "category",
        "is_active",
        "date",
    )

    search_fields = (
        "title",
        "content",
    )

    ordering = (
        "-date",
        "order",
    )