from django.contrib import admin

from .models import (
    HeroSection,
    HistoryEntry,
    FarmingHero,
    FarmingUpdate,
    Child,
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