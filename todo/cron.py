from django.utils import timezone
from django.core.mail import send_mail
from .models import Todo

def reminder_task():
    now = timezone.now()
    due_todos = Todo.objects.filter(to_be_done_before__lte=now, completed=False)

    for todo in due_todos:
        user_email = todo.user.email  # suppose que le champ user est relié
        if user_email:
            send_mail(
                subject="Reminder: Task Deadline Approaching",
                message=f"Don't forget to complete: {todo.title}",
                from_email="noreply@dobloom.com",
                recipient_list=[user_email]
            )
