from django.contrib import admin
from .models import Award, Education, Experience , Publication, Course, Curr_student, Passed_student, Project, ProjectImage, Review, Collaboration, Collaboration_acad, Position, Research, Company, Book, Service


# Register your models here.
class AwardAdmin(admin.ModelAdmin):
    list_display = ('aw_id', 'Title', 'About', 'Time', 'add_date')
    search_fields = ('Title', 'add_date')
    list_per_page = 50

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('comp_id', 'title', 'image_tag', 'add_date')
    search_fields = ('title', 'add_date')
    list_per_page = 50


class EducationAdmin(admin.ModelAdmin):
    list_display = ('ed_id', 'year', 'position', 'add_date', 'company')
    search_fields = ('company', 'position')
    list_per_page = 50


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('ex_id', 'duration', 'position', 'company', 'add_date')
    search_fields = ('company', 'position')
    list_per_page = 50


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('pub_id', 'title', 'author', 'year', 'info', 'type', 'add_date')
    search_fields = ('title', 'author')
    list_per_page = 50


class CourseAdmin(admin.ModelAdmin):
    list_display = ('c_id', 'course_name', 'times_conducted', 'company', 'clink', 'about', 'special_position', 'add_date')
    search_fields = ('course_id', 'course_name', 'company')
    list_per_page = 50


class Curr_studentAdmin(admin.ModelAdmin):
    list_display = ('cstu_id', 'name', 'contact', 'year_joining', 'about', 'ed_level', 'image_tag', 'add_date')
    search_fields = ('name', 'ed_level')
    list_per_page = 50


class Passed_studentAdmin(admin.ModelAdmin):
    list_display = ('pstu_id', 'name', 'contact', 'tenure', 'about', 'ed_level', 'add_date')
    search_fields = ('name', 'ed_level')
    list_per_page = 50


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('rev_id', 'name', 'add_date')
    search_fields = ('name', 'type')
    list_per_page = 50


class CollaborationAdmin(admin.ModelAdmin):
    list_display = ('col_id', 'name', 'add_date')
    search_fields = ('name', 'add_date')
    list_per_page = 50


class Collaboration_acadAdmin(admin.ModelAdmin):
    list_display = ('col_id', 'name', 'add_date')
    search_fields = ('name', 'add_date')
    list_per_page = 50


class PositionAdmin(admin.ModelAdmin):
    list_display = ('pos_id', 'name', 'add_date')
    search_fields = ('name', 'add_date')
    list_per_page = 50


class BookAdmin(admin.ModelAdmin):
    list_display = ('b_id', 'name', 'author', 'year', 'location', 'publisher', 'add_date')
    search_fields = ('name', 'publisher')
    list_per_page = 50


class ResearchAdmin(admin.ModelAdmin):
    list_display = ('res_id', 'name', 'type', 'add_date')
    search_fields = ('name', 'type')
    list_per_page = 50


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('b_id', 'name', 'tenure', 'add_date')
    search_fields = ('name', 'tenure')
    list_per_page = 50


class ProjectImageAdmin(admin.StackedInline):
    model = ProjectImage


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageAdmin]
    list_display = ('proj_id', 'featured', 'name', 'company', 'tenure', 'status', 'project_value', 'pi', 'copi', 'about', 'image_tag', 'type', 'add_date')
    search_fields = ('name', 'company', 'featured')
    list_per_page = 50


class ProjectImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Curr_student, Curr_studentAdmin)
admin.site.register(Passed_student, Passed_studentAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Collaboration, CollaborationAdmin)
admin.site.register(Collaboration_acad, Collaboration_acadAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Research, ResearchAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Award, AwardAdmin)
