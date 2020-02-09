from django.db import models
from django.core.mail import send_mail, mail_admins
from django.template.loader import render_to_string

# Signals
from django.db.models.signals import post_save
from django.dispatch import receiver


class Documento(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)
    doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ('deletar_clientes', 'Usuario pode deletar clientes'),
        )

    # def save(self, *args, **kwargs):
    #     super(Person, self).save(*args, **kwargs)
    #     self.sendTestEmail()

    def sendTestEmail(self):
        context = {'cliente': self.first_name}
        plain_text = render_to_string('emails/new_client.txt', context)
        html_email = render_to_string('emails/new_client.html', context)

        send_mail(
            'Nuevo cliente registrado',
            plain_text,
            'yurimm4@gmail.com',
            ['iyurimm4@gmail.com'],
            html_message=html_email,
            fail_silently=False,
        )
        
        mail_admins(
            'ADMINS - Nuevo cliente registrado',
            plain_text,
            html_message=html_email,
            fail_silently=False,
        )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name.capitalize()


@receiver(post_save, sender=Person)
def post_save_send_email(sender, instance, *args, **kwargs):
    instance.sendTestEmail()