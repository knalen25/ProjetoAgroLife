from django.contrib import admin
from django.urls import path
from boi import views
from account import views as v2

urlpatterns = [
    
    path('', views.home, name='base'),
    path('admin/', admin.site.urls),
    path('login/', v2.login_view, name='login'),
    path('logout/', v2.logout_view, name='logout'),
    
    # Urls de criacao
    path('criarcurral/', views.CurralCreateView.as_view(), name='criarcurral'),
    path('criarboi/', views.BoiCreateView.as_view(), name='criarboi'),
    path('criarlote/', views.LoteCreateView.as_view(), name='criarlote'),
    path('criarmedicamento/', views.MedicamentoCreateView.as_view(), name='criarmedicamento'),
    
    # urls de listagem
    path('listacurral/', views.lista_curral_view, name='listacurral'),
    path('listaboi/', views.lista_boi_view, name='listaboi'),
    path('listamedicamento/', views.lista_medicamento_view, name='listamedicamento'),
    path('listalote/', views.lista_lote_view, name='listalote'),
    
    # Urls de detalhes do objeto
    path('curral/<int:pk>/', views.CurralDetailView.as_view(), name='detalhecurral'),
    path('boi/<int:pk>/', views.BoiDetailView.as_view(), name='detalheboi'),
    path('lote/<int:pk>/', views.LoteDetailView.as_view(), name='detalhelote'),
    path('medicamento/<int:pk>/', views.MedicamentoDetailView.as_view(), name='detalhemedicamento'),
    
    # Urls de update
    path('curral/<int:pk>/update/', views.CurralUpdateView.as_view(), name='atualizacurral'),
    path('boi/<int:pk>/update/', views.BoiUpdateView.as_view(), name='atualizaboi'),
    path('lote/<int:pk>/update/', views.LoteUpdateView.as_view(), name='atualizalote'),
    path('medicamento/<int:pk>/update/', views.MedicamentoUpdateView.as_view(), name='atualizamedicamento'),
    
    # Urls de delete
    path('curral/<int:pk>/delete/', views.CurralDeleteView.as_view(), name='deletacurral'),
    path('boi/<int:pk>/delete/', views.BoiDeleteView.as_view(), name='deletaboi'),
    path('lote/<int:pk>/delete/', views.LoteDeleteView.as_view(), name='deletalote'),
    path('medicamento/<int:pk>/delete/', views.MedicamentoDeleteView.as_view(), name='deletamedicamento'),
    
    ]