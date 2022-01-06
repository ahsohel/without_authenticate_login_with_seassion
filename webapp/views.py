from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from . models import info
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def info_login(request):
    if request.method == 'POST':
        form_login_email = request.POST.get('login_email')
        form_login_password = request.POST.get('login_password')

        r = info.objects.filter(e=form_login_email)


        if r:
            rr = info.objects.get(e=form_login_email)
            password_of_database = rr.p
            if password_of_database == form_login_password:

                request.session['session_email']=form_login_email
                request.session['session_password']=form_login_password

                print("setion is ")
                print(request.session.get('session_email'))



                s_e =request.session.get('session_email')
                s_p = request.session.get('session_password')


                return render(request, 'd.html', {'s_e':s_e, 's_p':s_p})
        else:
            messages.error(request, 'your password is wrong')
            return render(request, 'index.html')

    return render(request, 'index.html')


def go_t(request):
    i = request.session.get('session_email')
    if i:
        return render(request, 't.html')

    return render(request, 'index.html')


def clear_seassion(request):
    request.session.clear()
    return render(request, 'index.html')



def go_last(request):
    itt = request.session.get('session_email')
    if itt:
        return render(request, 'last.html')

    return render(request, 'index.html')

def update_session(request):
    ittt = request.session.get('session_email')
    ittt = info.objects.get(e = ittt)
    print("ittt.p")
    print(ittt.p)
    ittt.e ="sohel "
    ittt.p="sohel"
    ittt.save()
    print("ittt.p 222222222222")
    print(ittt.p)
    r_e = request.session['session_email'] = ittt.e
    r_p = request.session['session_password'] = ittt.p

    return render(request, 'sow_session.html', {'r_e':r_e, 'r_p':r_p})
