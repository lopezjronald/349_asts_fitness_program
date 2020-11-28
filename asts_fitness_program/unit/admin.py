from django.contrib import admin
from .models import Airman, Profile, Naughty, PhysicalTrainingLeader, UnitFitnessProgramManager

admin.site.site_header = '349 ASTS FITNESS PROGRAM'
admin.site.site_title = '349 ASTS Fitness Program'
admin.site.index_title = 'UFPM KICK-ASS ADMIN TEAM'


class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1


class NaughtyInline(admin.TabularInline):
    model = Naughty
    extra = 1


class PhysicalTrainingLeaderInline(admin.TabularInline):
    model = PhysicalTrainingLeader
    extra = 1


class UnitFitnessProgramManagerInline(admin.TabularInline):
    model = UnitFitnessProgramManager
    extra = 1


# Register your models here.
# admin.site.register(Airman)
@admin.register(Airman)
class AirmanAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
        NaughtyInline,
        PhysicalTrainingLeaderInline,
        UnitFitnessProgramManagerInline,
    ]

    list_display = (
        'ssn', 'rank', 'first_name', 'middle_initial', 'last_name', 'test_date', 'fitness_level', 'active_status',)
    list_display_links = ('ssn',)
    list_editable = (
        'rank', 'first_name', 'middle_initial', 'last_name', 'test_date', 'fitness_level', 'active_status',)
    list_filter = ('first_name', 'last_name', 'test_date', 'fitness_level',)
    search_fields = ('first_name', 'last_name', 'ssn')
    prepopulated_fields = {'airman_slug': ('ssn',)}
    date_hierarchy = 'test_date'
    ordering = ('test_date', 'last_name')
    actions_on_bottom = True


# @admin.register(Physical_Training_Leader)
@admin.register(PhysicalTrainingLeader)
class PhysicalTrainingLeaderAdmin(admin.ModelAdmin):
    list_display = ('airman_id', 'ptl_certification_date', 'ptl_expiration_date', 'cpr_expiration_date')
    list_editable = ('ptl_certification_date', 'ptl_expiration_date', 'cpr_expiration_date',)
    list_filter = ('ptl_expiration_date', 'cpr_expiration_date')
    date_hierarchy = 'ptl_expiration_date'
    ordering = ('-ptl_expiration_date', '-cpr_expiration_date')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('airman_id', 'profile_start_date', 'profile_expiration_date',)
    list_editable = ('profile_start_date', 'profile_expiration_date',)
    list_filter = ('profile_expiration_date',)
    date_hierarchy = 'profile_expiration_date'
    ordering = ('-profile_expiration_date',)


@admin.register(Naughty)
class NaughtyAdmin(admin.ModelAdmin):
    list_display = ('airman_id', 'failure_date', 'be_well_completion_date', 'status_level')
    list_editable = ('failure_date', 'be_well_completion_date', 'status_level',)
    list_filter = ('failure_date',)
    search_fields = ('failure_date',)
    date_hierarchy = 'failure_date'
    ordering = ('-failure_date',)


@admin.register(UnitFitnessProgramManager)
class UnitFitnessProgramManagerAdmin(admin.ModelAdmin):
    list_display = ('airman_id', 'ptl_id', 'ufpm_certification_date', 'ufpm_expiration_date')
    list_editable = ('ptl_id', 'ufpm_certification_date', 'ufpm_expiration_date',)
    list_filter = ('ufpm_expiration_date',)
    date_hierarchy = 'ufpm_expiration_date'
    ordering = ('-ufpm_expiration_date',)
