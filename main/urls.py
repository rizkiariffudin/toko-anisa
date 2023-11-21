from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id, create_item_flutter
from main.views import register #sesuaikan dengan nama fungsi yang dibuat
from main.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from main.views import logout_user, add_amount, reduce_amount, remove_item
from main.views import edit_item, get_item_json, create_ajax


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
    path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
    path('logout/', logout_user, name='logout'),
    path('add_amount/<int:item_id>/', add_amount, name='add_amount'),
    path('reduce_amount/<int:item_id>/', reduce_amount, name='reduce_amount'),
    path('edit-item/<int:id>', edit_item, name='edit_item'),
    path('remove_item/<int:item_id>/', remove_item, name='remove_item'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-ajax/', create_ajax, name='create-ajax'),
    path('create-flutter/', create_item_flutter, name='create_item_flutter'),
]