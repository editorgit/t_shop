from django.db import models


class Email(models.Model):
    email_id = models.BigIntegerField(primary_key=True)
    email_address = models.CharField(max_length=50)

    def __str__(self):
        return self.email_address

    class Meta:
        db_table = 'emails'


class Customer(models.Model):
    customer_id = models.BigIntegerField(primary_key=True)
    email = models.ForeignKey(Email, to_field='email_id', on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'customers'
