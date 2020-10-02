from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect

#Creating what the user wants to see
class HomeView(TemplateView):
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            name = request.POST['name']
            number = request.POST['number']
            subject = request.POST['subject']
            message = request.POST['message']
            sender = request.POST['email']
            recipients = ['kiran.gangadhar.01@gmail.com', 'pcdoctor5955@gmail.com']
            message = 'Name    ---> ' + name + '\n' + 'Number ---> ' + number + '\n\n' + message
            subject = name + ' : ' + subject

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/')  # Redirect after POST
        return render(request, '/')

