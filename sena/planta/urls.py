from django.urls import path

from . import views

app_name = "planta"
urlpatterns = [
    path('', views.index, name="index" ),
    path('saludo/', views.saludar, name="saludo" ),
    path('comprar/', views.comprar, name="comprar" ),
    path('saludo-especial/<str:dato>', views.saludoEspecial, name="especial"),
    path('sum/<int:num1>/<int:num2>', views.sumarDosNum, name="sum"),
    
    path('login-formulario/', views.loginFormulario, name="loginf"),
    path('login/', views.login, name="login"),
    
    path('calc-formulario/', views.calcFormulario, name="calcf"),
    path('calc/', views.calc, name="calc"),
]