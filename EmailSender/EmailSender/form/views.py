from django.shortcuts import render
from django.forms import modelform_factory, ModelForm, Textarea
from .models import Email
import smtplib
# Create your views here.

EmailForm = modelform_factory(Email, exclude=[])


class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = '__all__'
        widgets = {
            'recipient': Textarea(attrs={'cols': 80, 'rows': 1}),
            'subject': Textarea(attrs={'cols': 80, 'rows': 1}),
            'text': Textarea(attrs={'cols': 80, 'rows': 20}),
        }


def send_email(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            username = ""  # Enter Your Username
            password = ""  # Enter Your Password
            message = "Subject: "
            message += form.cleaned_data.get('subject')
            message += '\n'
            message += '\n'
            message += form.cleaned_data.get('text')
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=username, password=password)
            connection.sendmail(from_addr=username, to_addrs=form.cleaned_data.get('recipient'), msg=message)
            connection.close()

            form = EmailForm()
            return render(request, 'send.html', {"form": form})
    else:
        form = EmailForm()
    return render(request, 'send.html', {"form": form})
