from django.shortcuts import render,HttpResponse
def index(request):
    # 
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def service(request):
     return render(request, 'services.html')
def demo(request):
    return render(request, 'demo.html')
def base(request):
    return render(request, 'base.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message, File





from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message, File

@login_required
def send_message(request):
    if request.method == 'POST':
        receiver = request.POST.get('receiver')
        content = request.POST.get('content')
        message = Message.objects.create(sender=request.user, receiver=User.objects.get(username=receiver), content=content)
        message.save()
        return redirect('inbox')
    return render(request, 'send_message.html')

@login_required
def inbox(request):
    received_messages = Message.objects.filter(receiver=request.user, is_deleted_by_receiver=False)
    return render(request, 'inbox.html', {'received_messages': received_messages})

@login_required
def delete_message(request, message_id):
    message = Message.objects.get(id=message_id)
    if message.sender == request.user:
        message.is_deleted_by_sender = True
    elif message.receiver == request.user:
        message.is_deleted_by_receiver = True
    message.save()
    return redirect('inbox')

@login_required
def send_file(request):
    if request.method == 'POST':
        receiver = request.POST.get('receiver')
        file = request.FILES['file']
        file_obj = File.objects.create(sender=request.user, receiver=User.objects.get(username=receiver), file=file)
        file_obj.save()
        return redirect('inbox')
    return render(request, 'send_file.html')

@login_required
def files_received(request):
    received_files = File.objects.filter(receiver=request.user)
    return render(request, 'files_received.html', {'received_files': received_files})
