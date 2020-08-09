from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """ Zadacha otpravki email-uvedomleniy pri uspeshnom oformlenii zakaza."""
    order = Order.objects.get(id=order_id)

    subject = 'Order nr. {}'.format(order_id)
    message = 'Gadyrly {},\n\nSizin satyn almak uchin eden onumleriniz bellige alyndy .' \
              '\nSizin zakazynyzyn belligi {}.'.format(order.first_name, order.id)
    mail_sent = send_mail(subject,
                          message,
                          'arslan092486@gmail.com',
                          [order.email])