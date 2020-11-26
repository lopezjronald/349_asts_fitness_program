from django.db import models
from django.urls import reverse


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(active_status='active')


class Airman(models.Model):
    ACTIVE_CHOICE = (
        ('active', 'active'),
        ('inactive', 'inactive'),
    )

    RANK_CHOICE = (
        ('AB', 'AB'),
        ('Amn', 'Amn'),
        ('A1C', 'A1C'),
        ('SrA', 'SrA'),
        ('SSgt', 'SSgt'),
        ('TSgt', 'TSgt'),
        ('MSgt', 'MSgt'),
        ('SMSgt', 'SMSgt'),
        ('CMSgt', 'CMSgt'),
        ('2nd Lt', '2nd Lt'),
        ('1st Lt', '1st Lt'),
        ('Capt', 'Capt'),
        ('Maj', 'Maj'),
        ('Lt Col', 'Lt Col'),
        ('Col', 'Col'),
        ('Brig Gen', 'Brig Gen'),
        ('Maj Gen', 'Maj Gen'),
        ('Lt Gen', 'Lt Gen'),
        ('Gen', 'General'),
    )
    FITNESS_CHOICE = (
        ('Excellent', 'EXCELLENT'),
        ('Satisfactory', 'SATISFACTORY'),
        ('Pass', 'PASS'),
        ('Unsatisfactory', 'UNSATISFACTORY'),
        ('Fail', 'FAIL'),
        ('Exemption', 'EXEMPTION'),
    )
    airman_id = models.AutoField(primary_key=True, serialize=True)
    fitness_level = models.CharField(max_length=50,
                                     choices=FITNESS_CHOICE,
                                     default='satisfactory')
    rank = models.CharField(max_length=10,
                            choices=RANK_CHOICE,
                            default='AB')
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=5)
    last_name = models.CharField(max_length=50)
    ssn = models.IntegerField()
    airman_slug = models.SlugField(max_length=50,
                                   unique_for_date='test_date')
    test_date = models.DateField()
    ptl = models.BooleanField(default=False)
    ufpm = models.BooleanField(default=False)
    active_status = models.CharField(max_length=10,
                                     choices=ACTIVE_CHOICE,
                                     default='active')

    class Meta:
        ordering = ('last_name',)

    def __str__(self):
        return f"{self.rank} {self.first_name} {self.middle_initial} {self.last_name}"

    objects = models.Manager()
    active = ActiveManager()

    def get_absolute_url(self):
        return reverse('unit:airman_detail',
                       args=[self.test_date.year,
                             self.test_date.month,
                             self.test_date.day,
                             self.airman_slug])


class Failure(models.Model):
    failure_id = models.AutoField(primary_key=True, serialize=True)
    airman_id = models.ForeignKey(
        Airman,
        on_delete=models.CASCADE, )
    failure_date = models.DateField()
    be_well_completion_date = models.DateField()

    class Meta:
        ordering = ('-failure_date',)

    def __str__(self):
        return f"{self.airman_id}"


class Physical_Training_Leader(models.Model):
    ptl_id = models.AutoField(primary_key=True, serialize=True)
    airman_id = models.ForeignKey(
        Airman,
        on_delete=models.CASCADE, )
    ptl_certification_date = models.DateField()
    ptl_expiration_date = models.DateField()
    cpr_expiration_date = models.DateField()

    class Meta:
        ordering = ('ptl_expiration_date',)

    def __str__(self):
        return f"{self.airman_id}"


class Unit_Fitness_Program_Manager(models.Model):
    ufpm_id = models.AutoField(primary_key=True, serialize=True)
    airman_id = models.ForeignKey(
        Airman,
        on_delete=models.CASCADE, )
    ptl_id = models.ForeignKey(
        Physical_Training_Leader,
        on_delete=models.CASCADE, )
    ufpm_certification_date = models.DateField()
    ufpm_expiration_date = models.DateField()

    class Meta:
        ordering = ('ufpm_expiration_date',)

    def __str__(self):
        return f"{self.airman_id}"


class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True, serialize=True)
    airman_id = models.ForeignKey(
        Airman,
        on_delete=models.CASCADE, )
    profile_start_date = models.DateField()
    profile_expiration_date = models.DateField()
    profile_details = models.TextField()

    class Meta:
        ordering = ('profile_expiration_date',)

    def __str__(self):
        return f"{self.airman_id}"
