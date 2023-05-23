from django.shortcuts import render
import pywhatkit
import time
import datetime
import keyboard



# Create your views here.
def index(request):
    return render(request, 'index.html')
msgs = [];
def sent(request):
    msg = request.POST['msg']
    # now = datetime.datetime.now()
    # pywhatkit.sendwhatmsg("+91 8707256458", msg, now.hour, now.minute +1)
    # pywhatkit.sendwhatmsg("+91 7217582719", msg, now.hour, now.minute +2)
    pywhatkit.sendwhatmsg_instantly("+91 8707256458", msg, 10, tab_close=True)
    # pywhatkit.sendwhatmsg_instantly("+91 8707256458", msg, tab_close=True)


    
    # keyboard.pzress_and_release('ctrl+w')
    msgs.append(msg)
    dict = {'msgs':msgs}
    return render(request, 'index.html', {'msgs':msgs})