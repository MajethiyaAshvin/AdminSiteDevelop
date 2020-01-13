
from django.contrib import admin
from app.models import User, Book, Author, Student
class UsersAdmin(admin.ModelAdmin):
    list_display= ('firstname', 'midlename', 'lastname', 'mobile','password')
    list_filter = ('lastname', 'firstname')
    list_editable = ['lastname','midlename']
    ordering = ['lastname']
    search_fields = ('firstname','mobile')
    date_hierarchy = 'date_a'
class AutherAdmin(admin.ModelAdmin):
    list_display= ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    list_filter = ('first_name', 'last_name')
class BookAdmin(admin.ModelAdmin):
    list_display = ('Auther','subject')
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('last_name','first_name')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = (
        ('a','b'),
        ('c','d'),
        ('date_a'),
        ('date_b'),
        'field_name'
    )
# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#    fieldsets = (
#        (None,{
#            'fields':(
#                ('a','b'),
#                ('c','d')
#
#            )
#        }),
#        ('Dates',{
#            'class':('callapse',),
#            'fields':('date_a','date_b')
#
#        })
#    )

admin.site.register(User,UsersAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Author,AutherAdmin)


