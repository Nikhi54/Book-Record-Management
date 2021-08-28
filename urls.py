from django.conf.urls import url
from BRMapp import views

urlpatterns = [

url('view_books',views.viewBooks),
url('edit_book',views.editBook),
url('delete_Book',views.deleteBook),
url('search_book',views.searchBook),
url('new_book',views.newBook),
url(r'^add',views.add),
url('search',views.search),
url('edit',views.edit),
url('login',views.userLogin),
url('logout',views.userLogout),

]
