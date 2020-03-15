from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.models import  Group
from django.views.generic import (CreateView,  TemplateView,
                                  UpdateView)


# Create your views here.
def index(request):
    context = {'title': "QRCode | Home"}
    return render(request, 'qrcode/index.html', context)

class EmployessCreate(CreateView):
    form_class = EmployeesForm
    template_name = 'employee/add_employee.html'

    def form_invalid(self, form):
        context = {
            'form': form,
            }
        return render(self.request, self.template_name, context)

    def form_valid(self, form):
        if self.request.POST.get('employeedetail') == 'Save':
            userobj = form.save(commit=False)
            userobj.set_password(form.cleaned_data['mobile'])
            userobj.save()
            my_group = Group.objects.filter(name='Employee').first()
            if my_group:
                my_group.user_set.add(userobj)
            else:
                Group.objects.get_or_create(name='Employee')
                my_group = Group.objects.filter(name='Employee').first()
                my_group.user_set.add(userobj)
            emp_id = userobj.pk
            # return redirect('/employee-details/'+emp_id)
        context = {
            'form': self.form_class,
        }
        return render(self.request, self.template_name, context)

