from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    """
    Customizing the Django admin interface for the Student model.
    This configuration allows enhanced functionalities in the admin interface.
    """

    # Fields to display in the list view
    list_display = ('roll_no', 'name', 'age')

    # Add search functionality based on roll_no and name
    search_fields = ['roll_no', 'name']

    # Add filters for age and date_of_birth
    list_filter = ['age']

    ordering = ['name']

admin.site.register(Student, StudentAdmin)