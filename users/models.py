from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate


class DoctorsAccountManager(BaseUserManager):
    def create_user(self, email, username,  first_name, last_name, date_of_birth, gender, referral_id, license_no, university, city, country, zip_code, phone, password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have a username")
        if not first_name:
            raise ValueError("User must have a first_name")
        if not last_name:
            raise ValueError("User must have a last_name")
        if not date_of_birth:
            raise ValueError("User must have a date of birth")
        if not gender:
            raise ValueError("User must have a gender")
        if not license_no:
            raise ValueError("User must have a license_no")
        if not university:
            raise ValueError("User must have a university")
        if not city:
            raise ValueError("User must have a city")
        if not country:
            raise ValueError("User must have a country")
        if not zip_code:
            raise ValueError("User must have a zip code")
        if not phone:
            raise ValueError("User must have a phone number")
        if not referral_id:
            raise ValueError("User must have a ref id")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender,
            license_no=license_no,
            university=university,
            # father_ID=father_ID,
            # mother_ID=mother_ID,
            # spouse_ID=spouse_ID,
            # child_ID=child_ID,
            referral_id=referral_id,
            city=city,
            country=country,
            zip_code=zip_code,
            phone=phone,
        )
        user.is_admin = False
        user.is_superuser = False
        user.set_password(password)
        user.save(using=self._db)
        return user


class RegDoctor(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=20, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(verbose_name='date of birth')
    gender = models.CharField(max_length=7)
    license_no = models.CharField(max_length=30, unique=True)
    university = models.CharField(max_length=40)
    # father_ID = models.CharField(max_length=20)
    # mother_ID = models.CharField(max_length=20)
    # spouse_ID = models.CharField(max_length=20)
    # child_ID = models.CharField(max_length=20)
    referral_id = models.CharField(max_length=90)
    city = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['username', 'first_name', 'last_name',
                      'date_of_birth', 'gender', 'license_no', 'university', 'referral_id', 'city', 'country', 'zip_code', 'phone']

    objects = DoctorsAccountManager()


class PatientsAccountManager(BaseUserManager):
    def create_user(self, email, username,  first_name, last_name, date_of_birth, gender, city, country, zip_code, phone, password=None):

        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have an username")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")
        if not date_of_birth:
            raise ValueError("User must have a Date of Birth")
        if not gender:
            raise ValueError("User must have a gender")
        if not city:
            raise ValueError("User must have a city")
        if not country:
            raise ValueError("User must have a country")
        if not zip_code:
            raise ValueError("User must have a zip code")
        if not phone:
            raise ValueError("User must have a phone")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender,
            # parents_id_father=parents_id_father,
            # parents_id_mother=parents_id_mother,
            # spouse_id=spouse_id,
            # child_id=child_id,
            city=city,
            country=country,
            zip_code=zip_code,
            phone=phone,
        )
        user.is_admin = False
        user.is_superuser = False
        user.set_password(password)
        user.save(using=self._db)
        return user


class RegPatient(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=20, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(verbose_name='date_of_birth')
    gender = models.CharField(max_length=7)
    # parents_id_father = models.CharField(max_length=15)
    # parents_id_mother = models.CharField(max_length=15)
    # spouse_id = models.CharField(max_length=15)
    # child_id = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['username', 'first_name', 'last_name',
                      'Date_of_Birth', 'gender', 'city', 'country', 'zip_code', 'phone']

    objects = PatientsAccountManager()


class AdminAccountManager(BaseUserManager):
    def create_user(self, username, password=None):
        # if not email:
        #     raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have an username")

        user = self.model(
            username=username,
            # email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            # email=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class AdminUser(AbstractBaseUser):
    username = models.CharField(
        verbose_name='username', max_length=50, unique=True)
    email = models.EmailField(verbose_name="email", max_length=50)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = []

    objects = AdminAccountManager()

    def __str__(self):
        return f"{self.username}    {self.email}    {self.phone}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
