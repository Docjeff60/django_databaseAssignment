from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Student, CohortGroup, student_type
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.conf import settings
from django.core.paginator import Paginator

# Create your views here.



def cohort_home(request):
    students = Student.objects.all()
    cohorts = CohortGroup.objects.all()
    paginator = Paginator(students, 3) 

    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)  

    context = {
        "page_obj": page_obj,
        "cohorts": cohorts,
        "student_rank": student_type
    }

    return render(request, "newstud/index.html", context)




def about_cohort(request): 
    students = Student.objects.all()
    context = {'student': students}
    return render(request, "newstud/about.html", context)





def student_detail(request, slug):
    try:
        student = Student.objects.get(slug=slug)
    except Student.DoesNotExist:
        return redirect('404')
    
    cohort_group = student.cohort.first() # type: ignore
    if cohort_group:
        cohort_members = Student.objects.filter(cohort=cohort_group)
    else:
        cohort_members = Student.objects.none() 

    context = {
        "student": student,
        "cohort_members": cohort_members,
    }

    

    return render(request, "newstud/about.html", context)





# Creating email message

def send_message(request, id):
    if request.method == 'POST':
        recipient_name = request.POST.get('recipient_name')
        recipient_email = request.POST.get('recipient_email')
        sender_name = request.POST.get('sender_name')
        sender_email = request.POST.get('sender_email')
        sender_contact = request.POST.get('sender_contact')
        email_title = request.POST.get('email_title')
        message_body = request.POST.get('message_body')
        
        # Construct the email message
        recipient_message = f"""
        Hello {recipient_name},

        {message_body}

        Best regards,
        {sender_name}
        Contact: {sender_contact}
        Email: {sender_email}
        """

        sender_confirmation_message = f"""
        Hello {sender_name},

        Your email to {recipient_name} ({recipient_email}) has been successfully sent. Below is a copy of your message:

        {message_body}

        Thank you for using our platform!

        Regards,
        The Team
        """

        # Attempt to send the message
        try:
            # Send the email to the recipient
            send_mail(
                subject=email_title,
                message=recipient_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[recipient_email],
            )

            # Send a confirmation email to the sender
            send_mail(
                subject=f"Confirmation: {email_title}",
                message=sender_confirmation_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[sender_email],
            )

            # Log success
            print(f"Confirmation email sent to: {sender_email}")

            # Display success message
            messages.success(request, "Email sent successfully!")
        except Exception as e:
            # Display error message
            messages.error(request, f"An error occurred: {e}")
            print(f"Error sending email: {e}")

        return redirect(reverse("student_detail", args=[id]))
        

    return render(request, 'newstud/about.html')


        