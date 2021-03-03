from django.contrib import admin
from .models import Student, Teacher


class StudentTeacherInline(admin.TabularInline):
    model = Student.teachers.through


class StudentAdmin(admin.ModelAdmin):
    inlines = (StudentTeacherInline,)


class TeacherAdmin(admin.ModelAdmin):
    inlines = (StudentTeacherInline,)


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
