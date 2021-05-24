from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class NewUserManager(BaseUserManager):

    def create_user(self, GIN, name, email, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.GIN =GIN

        user.name = name

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_hospital(self, GIN, email, name, password):

        user = self.create_user(
            GIN,
            email,
            name,
            password=password,
        )
        user.staff = True
        user.is_hospital = True
        user.save(using=self._db)
        return user

    def create_doctor(self, email, first_name, last_name, password):

        user = self.create_user(
            email,
            first_name,
            last_name,
            password=password,
        )
        user.is_doctor = True
        user.save(using=self._db)
        return user

    def create_patient(self, email, first_name, last_name, password):

        user = self.create_user(
            email,
            first_name,
            last_name,
            password=password,
        )
        user.is_patient = True
        user.save(using=self._db)
        return user

    def create_superuser(self, GIN, name, password):

        user = self.create_user(
            GIN,
            name,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class NewUser(AbstractBaseUser):

    # GIN = models.IntegerField(unique=True)  # general id number ,unique
    GIN = models.CharField(max_length=6, null=True, blank=True, unique=True)

    email = models.EmailField(max_length=255, null=True)

    name = models.CharField(max_length=255, null=True)

    first_name = models.CharField(max_length=255, null=True)

    last_name = models.CharField(max_length=255, null=True)

    is_active = models.BooleanField(default=True, null=True)

    is_hospital = models.BooleanField(default=False, null=True)  # hospital

    is_doctor = models.BooleanField(default=False, null=True)  # doctor

    is_patient = models.BooleanField(default=False, null=True)  # patient

    staff = models.BooleanField(default=False, null=True)  # staff

    admin = models.BooleanField(default=False, null=True)  # superuser

    USERNAME_FIELD = 'GIN'
    REQUIRED_FIELDS = []

    objects = NewUserManager()

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property                   # ??
    def is_staff(self):
        return self.staff

    @property                   # ??
    def is_admin(self):
        return self.admin
