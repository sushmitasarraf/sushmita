from django.contrib import admin

from home.models import Book,Author,Genre,Library


# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ('id','name')
    # note : RelatedOnlyFieldListFilter=> applicable when some fields are related to other tables
    list_filter = ('name','purchase_date',('book_author',admin.RelatedOnlyFieldListFilter))

    # list_filter = ('name','purchase_date','author')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass    

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    search_fields = ('name','book_no')
    fields = [('name','book_no'),('issue_date','return_date')]

    list_filter = ('name','issue_date')   