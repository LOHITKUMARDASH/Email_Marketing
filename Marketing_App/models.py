from django.db import models
import datetime
from django.db.models import JSONField, BinaryField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

# class ConvertingDateTimeField(models.DateTimeField):
#     def get_prep_value(self, value):
#         #print(value)
#         return str(datetime.datetime.strftime(value, '%d%m%Y-%H%M%S'))

class NewUser(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=150, unique=False)
    email = models.EmailField(_('email address'), unique=True)
    mobile = models.CharField(max_length=120, blank=True)
    country = models.CharField(max_length=120, default=False, blank=True)
    state = models.CharField(max_length=120, default=False, blank=True)
    Address = models.CharField(max_length=120, default=False, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_super = models.BooleanField('Is super', default=False)
    is_admin = models.BooleanField('Is admin', default=False)
    is_client = models.BooleanField('Is client', default=False)
    is_credit = models.IntegerField('Is Credit', blank=True, default=0)
    admin_id = models.IntegerField('admin_id', blank=True, default=0)

    first_name = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = "USERS"
        verbose_name = 'User'

class product(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.IntegerField()
    duration = models.IntegerField()
    description = models.CharField(max_length=300)
    user_id = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "PRODUCT"
        verbose_name = 'product'

class invoice_settings(models.Model):
    CompanyName = models.CharField(max_length=300)
    email = models.EmailField(max_length=30)
    ContactNumber = models.IntegerField()
    GSTIN = models.CharField(max_length=300)
    PanNo = models.CharField(max_length=300)
    Website = models.CharField(max_length=300)
    Currency = models.CharField(max_length=300)
    CompanyLogo = models.FileField()
    Address = models.CharField(max_length=300)
    BankName = models.CharField(max_length=300)
    BranchName = models.CharField(max_length=300)
    AccountName = models.CharField(max_length=300)
    AccountType = models.CharField(max_length=300)
    BankAccountNo = models.CharField(max_length=300)
    IFSCNo = models.CharField(max_length=300)
    Heading = models.CharField(max_length=300)
    Client = models.CharField(max_length=300)
    Price = models.CharField(max_length=300)
    SubTotal = models.CharField(max_length=300)
    TotalAmount = models.CharField(max_length=300)
    ThankyouMassage = models.CharField(max_length=300)
    FooterNotes = models.CharField(max_length=300)
    UploadYourCompanyStamp = models.FileField()
    TermsandConditions = models.CharField(max_length=300)
    TermsandConditionsDetails = models.CharField(max_length=300)
    user_id = models.IntegerField()

    def __str__(self):
        return self.CompanyName

    class Meta:
        db_table = "SETTING"
        verbose_name = 'invoice_settings'

class fileuploads(models.Model):
    templates = models.CharField(max_length=150)
    file = models.FileField()

    def __str__(self):
        return self.templates

    class Meta:
        db_table = "TEMPLATES"
        verbose_name = 'fileuploads'

class Invoice(models.Model):
    customer = models.CharField(max_length=300)
    productName = models.CharField(max_length=300)
    price = models.IntegerField()
    quantity = models.IntegerField()
    duration = models.IntegerField()
    active_date = models.CharField(max_length=300)
    expiry_date = models.CharField(max_length=300)
    payment = models.CharField(max_length=300)
    due_quantity = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    def __str__(self):
        return self.customer

    class Meta:
        db_table = "INVOICE"
        verbose_name = 'invoice'

class group(models.Model):
    name = models.CharField(max_length=30)
    cid = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "GROUP"
        verbose_name = 'group'

class template(models.Model):
    logo = models.FileField()
    logolink = models.URLField(max_length=300)
    welcomeText = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    buttonname = models.CharField(max_length=300)
    buttonlink = models.URLField(max_length=300)
    description = models.CharField(max_length=3000)
    copyright = models.CharField(max_length=3000)
    user_id = models.IntegerField(default=0)
    file_id = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "TEMPLATE"
        verbose_name = 'template'

class customers(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.CharField(max_length=300, blank=True)
    state = models.CharField(max_length=300)
    checks = BinaryField()
    user_id = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "CUSTOMERS"
        verbose_name = 'customers'