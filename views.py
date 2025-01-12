from django.core.files.storage import FileSystemStorage
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *
from datetime import datetime
# Create your views here.
def fpage(request):
    return render(request,"loginindex.html")
def logout(request):
    return render(request,"loginindex.html")

def logincode(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    try:
        ob=login.objects.get(username=username,password=password)
        if ob is None:
            return HttpResponse('''<script>alert("invalid");window.location="/"</script>''')
        elif ob.type=='admin':

            return HttpResponse('''<script>alert("welcome to admin home");window.location="admin_home"</script>''')
        elif ob.type=='expert':
            request.session['lid']=ob.id

            return HttpResponse('''<script>alert("welcome to expert home");window.location="expert_home"</script>''')
        else:
            return HttpResponse('''<script>alert("invalid");window.location="/"</script>''')
    except:

            return HttpResponse('''<script>alert("invalid");window.location="/"</script>''')


def forgot_password(request):
    return render(request, "fp.html")

# ==================ADMIN=========================

def admin_home(request):
    return render(request, "admin/adminindex.html")



def manage_expert(request):
    obj = expert.objects.all()
    return render(request,"admin/manage expert.html",{'val':obj})


def add_expert(request):
   return render(request,"admin/expertreg index.html")

def addex(request):
    FirstName=request.POST['textfield']
    LastName = request.POST['textfield2']
    DOB = request.POST['textfield62']
    Place = request.POST['textarea']
    Post=request.POST['textarea1']
    Pincode = request.POST['textfield3']
    Phone=request.POST['textfield4']
    Email = request.POST['textfield5']
    Gender = request.POST['radiobutton']
    Username = request.POST['textfield6']
    Password = request.POST['textfield8']
    ob1=login()
    ob1.username=Username
    ob1.password=Password
    ob1.type='expert'
    ob1.save()

    ob=expert()
    ob.fname=FirstName
    ob.lname=LastName
    ob.DOB=DOB
    ob.place=Place
    ob.post=Post
    ob.pin=Pincode
    ob.phone=Phone
    ob.email=Email
    ob.gender=Gender
    ob.lid=ob1
    ob.save()
    return HttpResponse('''<script>alert("Inserted");window.location="/manage_expert"</script>''')


def delete_expert(request,id):
    ob = expert.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("deleted");window.location="/manage_expert"</script>''')

def edit_expert(request,id):
    obj=expert.objects.get(id=id)
    request.session['lid']=id
    return render(request,"admin/edit expert.html",{'data':obj})


def editex(request):
    obj=expert.objects.get(id=request.session[ 'lid'])

    FirstName = request.POST['textfield']
    LastName = request.POST['textfield2']
    DOB = request.POST['textfield62']
    Place = request.POST['textarea']
    Post = request.POST['textarea1']
    Pincode = request.POST['textfield3']
    Phone = request.POST['textfield4']
    Email = request.POST['textfield5']
    Gender = request.POST['radiobutton']


    obj.fname = FirstName
    obj.lname = LastName
    obj.DOB = DOB
    obj.place = Place
    obj.post = Post
    obj.pin = Pincode
    obj.phone = Phone
    obj.email = Email
    obj.gender = Gender
    obj.save()
    return HttpResponse('''<script>alert("edited");window.location="/manage_expert"</script>''')

def manage_complaint(request):
    obj = complaint.objects.all()
    return render(request,"admin/manage complaint.html",{"val":obj})


def send_reply(request,id):
    request.session['CID']=id
    return render(request,"admin/send reply.html")


def sendr(request):
    obj=complaint.objects.get(id=request.session['CID'])
    Reply=request.POST['textarea']
    obj.reply=Reply
    obj.save()
    return HttpResponse('''<script>alert("Replayed");window.location="/manage_complaint"</script>''')

def manage_instructions(request):
    obs=instructions.objects.all()
    return render(request,"admin/manage_instructions.html",{"val":obs})

def add_instruction(request):
    return render(request,"admin/add_instructions.html")


def addi(request):
    ins = request.POST['textfield']
    tp = request.POST['t']
    ob = instructions()
    ob.instruction = ins
    ob.topic = tp
    ob.date = datetime.now().strftime("%Y-%m-%d")
    ob.save()
    return HttpResponse('''<script>alert("Inserted");window.location="/manage_instructions"</script>''')




def delete_instruction(request,id):

    ob = instructions.objects.get(id=id)

    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location="/manage_instructions"</script>''')

def view_user(request):
    obj=user.objects.all()
    return render(request,"admin/view user.html",{"val":obj})


def block(request,id):
    obj=login.objects.get(id=id)
    obj.type='block'
    obj.save()
    return HttpResponse('''<script>alert("block");window.location="/view_user"</script>''')

def unblock(request,id):
    obj=login.objects.get(id=id)
    obj.type='user'
    obj.save()
    return HttpResponse('''<script>alert("unblock");window.location="/view_user"</script>''')


def view_feedback(request):
    obj = feedback.objects.all()
    return render(request,"admin/view feedback.html",{"val":obj})
def view_rating(request):
    obj = rating.objects.all()
    return render(request,"admin/view rating.html",{"val":obj})



# Expert


def expert_home(request):
    return render(request,"expert/expert home.html")

def manage_classvideo(request):
    ob=classvideos.objects.filter(eid__lid__id=request.session['lid'])
    return render(request,"expert/manage classvideo.html",{'val':ob})

def add_classvideo(request):
    return render(request,"expert/add classvideo.html")
def addc(request):
    Classvideo=request.FILES['file']
    d=request.POST['d']
    fs=FileSystemStorage()
    fsave=fs.save(Classvideo.name,Classvideo)
    ob = classvideos()
    ob.eid=expert.objects.get(lid__id=request.session['lid'])
    ob.date=datetime.today()
    ob.description=d
    ob.video = fsave
    ob.save()
    return HttpResponse('''<script>alert("Inserted");window.location="/manage_classvideo"</script>''')

def delete_classvideos(request,id):
    ob = classvideos.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("deleted");window.location="/manage_classvideo"</script>''')

def manage_exams(request):
    obj = exam.objects.filter(eid__lid__id=request.session['lid']).order_by('-id')
    return render(request,"expert/manage exams.html",{'val':obj})
def add_exam(request):
    return render(request,"expert/add exam.html")


def adde(request):
    Examname=request.POST['textfield']
    Details=request.POST['textfield2']
    Level=request.POST['select']
    ob=exam()
    ob.eid=expert.objects.get(lid__id=request.session['lid'])
    ob.examname=Examname
    ob.details=Details
    ob.level=Level

    ob.date = datetime.now().strftime("%Y-%m-%d")
    ob.save()
    return HttpResponse('''<script>alert("Inserted");window.location="/manage_exams"</script>''')

def delete_exam(request,id):
    ob = exam.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("deleted");window.location="/manage_exams"</script>''')

def edit_exam(request,id):
    obj = exam.objects.get(id=id)
    request.session['exid'] = id
    return render(request, "expert/edit exam.html", {'data': obj})
def editexam(request):
    obj=exam.objects.get(id=request.session[ 'exid'])

    Examname = request.POST['textfield']
    Details = request.POST['textfield2']
    Level= request.POST['select']

    obj.examname = Examname
    obj.details = Details
    obj.level=Level

    obj.save()
    return HttpResponse('''<script>alert("edited");window.location="/manage_exams"</script>''')

def questionss(request,id):
    request.session['exid'] = id
    obj = answer_details.objects.filter(Exid=id).order_by('id')
    print(obj)
    return render(request,"expert/questions.html",{"val":obj})


def Add_questions(request):
    return render(request,"expert/Add questions.html")

def addq(request):
    print(request.POST,"++++++++++++ ")

    Answer=request.POST['textarea2']
    Option1=request.POST['textarea3']
    Option2=request.POST['textarea4']
    Option3=request.POST['textarea5']
    Option4=request.POST['textarea6']

    img1=request.FILES['file']
    fn=FileSystemStorage()
    fs1=fn.save(img1.name,img1)

    Level=request.POST['select']


    ob1=answer_details()
    ob1.Exid_id=request.session['exid']
    ob1.question=fs1

    ob1.answer=Answer
    ob1.option1=Option1
    ob1.option2=Option2
    ob1.option3=Option3
    ob1.option4=Option4
    ob1.level=Level
    ob1.save()
    return HttpResponse('''<script>alert("Inserted");window.location="/manage_exams"</script>''')


def delete_questions(request,id):
    ob = answer_details.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("deleted");window.location="/manage_exams"</script>''')



def Instructions(request):
    ob = instructions.objects.all()

    return render(request,"expert/view_instructions.html",{"val":ob})




