from importlib.resources import contents
from turtle import title
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Medicine
# Create your views here.

# def index(request):
#     a='master'

#     return render(request,'myapp22/index.html') 



# def homepage(request):
#     home = Blogpage(title = "Is Cardio good for health")
#     home.content = "Cardio exercise can benefit brain and joint health. One study reported that physical activity may reduce dementia risk, no matter what age you are. Other benefits include: Increases blood flow and decreases chances of stroke."
    
#     home.save()
#     # return HttpResponse ('<h1>This is a String</h1>',)
#     return render(request,'myapp22/blog.html') 


# def homepage(request):
#     home= Blogpage
#     home.title="just for testing"
#     context = {
#          'home':home,
#     }

   
#     return render(request,'myapp22\blog.html',context)

#$$ space for homepage $$#

def medicine(request):
    med = Medicine(price = 72)
    med.title = "Dolo 500"
    med.content = "Paracetamol tab 500 iu"
    med.description = "a paracetamol product from company named dolo,and it cures fever and related illness"
    print(med.title)
    med.save()
    context = {
          'med':med
    }

    return render(request,'appui/base.html',context)



def medicine_details(request,id):
    med=Medicine.objects.get(id=id)


    context= {
        'med':med,
    }
     
    return render(request,'appui/med_inventory.html',context)




def add_medicine(request):
    if request.method =='POST':
       title = request.POST.get('title')
       price = request.POST.get('price')
       content = request.POST.get('content')
       description = request.POST.get('description')
       image = request.FILES['upload']
       
       med=Medicine(title=title,price=price,description=description,image=image,content=content)
        
       med.save()
       
       
       return redirect('/appui/homepage') 
    return render(request,'appui/add_medicine.html')



def update_medicine(request,id):
   medicine = Medicine.objects.get(id=id)
   
   if request.method =='POST':
       medicine.title = request.POST.get('title')
       medicine.price = request.POST.get('price')
       medicine.content = request.POST.get('content')
       medicine.description = request.POST.get('discription')
       try:
           medicine.image = request.FILES['upload']
       except:
            pass
      
       medicine.save()
       
       return redirect("/myapp22/medicine")

   context = {
    'medicine':medicine
    }
       
   return render(request,'myapp/update_medicine.html',context)



def delete_medicine(request, id):

    medicine = Medicine.objects.get(id=id)
    

    context = {
        'medicine':medicine
       }
 
    if request.method =="POST":
        #delete object
        medicine.delete()
        #after deleting redirect to
        #home page
        return redirect("/myapp22/medicine")

    return render(request,'myapp/delete_medicine.html',context)
