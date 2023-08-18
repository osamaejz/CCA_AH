from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Student,Employee,Results, DigitSpanTestResult, VisualArrayTestResult
# Register your models here.

class ResultsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("result_id", "assessment_duration", "date_created")

class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("student_id", "name", "roll_no", "batch", "semester", "department", "year_of_birth", "email", "date_created","result_id")

class EmployeeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("employee_id", "name", "organization", "qualification", "designation", "year_of_birth", "email", "date_created","result_id")

class DigitSpanTestResultAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("result_id","rt","recall","stimuli","accuracy","trial_type","trial_index","time_elapsed","internal_node_id")

class VisualArrayTestResultAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("result_id","rt", "trial_type", "trial_index",	"time_elapsed",	"set_size",	"locations", "colours",	"correct", "key_press", "target_different")

admin.site.register(Results, ResultsAdmin)
admin.site.register(DigitSpanTestResult, DigitSpanTestResultAdmin)
admin.site.register(VisualArrayTestResult, VisualArrayTestResultAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Employee, EmployeeAdmin)