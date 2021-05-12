from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from contact_tienda.models import contacts

# Create your views here.
def view_contact (request) :
    # contact = contacts(name_contact='anderson',phone_contact='3154168458',email_contact ='andersonvid478@gmail.com')
    # contact.save()

    if request.method == 'POST' :
        nombreC = request.POST['nombreC']
        telefonoC = request.POST['telefonoC']
        correoC = request.POST['correoC']

        contact = contacts(name_contact=nombreC,phone_contact=telefonoC,email_contact =correoC)
        contact.save()
        return redirect('/contact/')
        
        
         
 
    
    list_contact = contacts.objects.all()

    return render(request,'index.html',{'list_contact': list_contact})


def delete_contact (request,idC) :

    contact = contacts.objects.filter(id=idC).delete()   
    return redirect('/contact/')
        

    




