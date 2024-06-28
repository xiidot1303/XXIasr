from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save
import datetime
from datetime import date  
import os

# Create your models here.
class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True, default='static/profile/user-default.jpg', upload_to='static/profile/')
    phone = models.CharField(max_length=100, null=True, blank=True)
    ADMIN_CHOICES = (
        ('user', 'Oddiy foydalanuvchi'),
        ('superuser', 'Nazoratchi'),
        ('admin', 'Admin')
    )
    status = models.CharField(choices=ADMIN_CHOICES, max_length=200)
    OFFICE_CHOICES = (
        ('1', 'XXI ASR BUXGALTERIYA'),
        ('2', 'XXI ASR KOMPYUTER XIZMATLARI'),
        ('3', 'XXI ASR BUXGALTERIYA XIZMATLARI MARKAZI'),
    )
    office = models.CharField(choices=OFFICE_CHOICES, max_length=200)
    password = models.CharField(max_length=300)

    def __str__(self):
        return self.name    


class Access(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ManyToManyField(Profile)
    name = models.CharField(max_length=255)

class File(models.Model):
    ishonchnoma = models.FileField(upload_to='static/ishonchnoma/')
    application = models.FileField(upload_to='static/application/')
    
    @property
    def filename(self):
        return os.path.basename(self.ishonchnoma.name)
    
    @property
    def filename2(self):
        return os.path.basename(self.application.name)

class Client(models.Model):
    picture = models.ImageField(null=True, blank=True, default="static/profile/user-default.jpg", upload_to="static/profile/")
    name = models.CharField(max_length=255)
    tin = models.CharField(max_length=255, null=True, blank=True)
    TYPE_CHOICES = (
        ('ytt','YaTT'),
        ('yuridik','Yuridik shaxs'),
        ('jismoniy','Jismoniy shaxs'),
        ('tanirovka','Tanirovka'),
        ('auction','Avtoraqam'),
        ('auction2','Auksion'),
        ('teacher',"O'qituvchi"),
        ('governor', 'Hokim yordamchisi'),
        ('taxi', 'Taxi litsenziya'),
        ('ishonchnoma', 'Ishonchnoma'),
        ('aviakassa', 'Aviakassa va tur'),
        ('daromad12', '12% daromad'),
        ('taxer', 'Soliqchi'),
        ('student', 'Talaba'),
        ('mahalla', 'Mahalla'),
    )
    type = models.CharField(choices=TYPE_CHOICES, max_length=255)
    SUB_CHOICES = (
        ('aylanma', 'Aylanma'),
        ('oddiy', 'Oddiy'),
        ('qatiy', 'Qat\'iy'),
        ('yollanma', "Yollanma xodim"),
    )
    sub_type = models.CharField(choices=SUB_CHOICES, max_length=255, null=True, blank=True)
    is_sub_gived = models.BooleanField(default=False)
    YURIDIK_CHOICES = (
        ('buxgalteriya', 'Buxgalteriya'),
        ('hisobotchilar', 'Hisobotchilar'),
        ('birrovchilar', 'Birrovchilar'),
    )
    MAHALLA_CHOICES = (
        ('yetakchi', 'Yoshlar yetakchisi'),
        ('oqsoqol', 'Mahalla oqsoqoli'),
        ('xotin_qizlar', 'Xotin qizlar faoli'),
        ('inson', 'Inson ijtimoiy agentligi'),
    )
    mahalla_type = models.CharField(null=True, blank=True, choices=MAHALLA_CHOICES, max_length=64)
    yuridik_type = models.CharField(choices=YURIDIK_CHOICES, max_length=255, null=True, blank=True)
    gov_login = models.CharField(max_length=255, null=True, blank=True)
    gov_password = models.CharField(max_length=255, null=True, blank=True)
    jshshir = models.CharField(max_length=255, null=True, blank=True)
    guvohnoma_file = models.FileField(null=True, blank=True, upload_to="static/guvohnoma/")
    guvohnoma_exp = models.DateField(null=True, blank=True)
    director = models.CharField(max_length=255, null=True, blank=True)
    director_tin = models.CharField(max_length=255, null=True, blank=True)
    school = models.CharField(max_length=255, null=True, blank=True)
    work_as = models.CharField(max_length=255, null=True, blank=True)
    phone1 = models.CharField(max_length=255, null=True, blank=True)
    phone2 = models.CharField(max_length=255, null=True, blank=True)
    phone3 = models.CharField(max_length=255, null=True, blank=True)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    key = models.FileField(upload_to='static/keys', null=True, blank=True)
    key_exp = models.DateField(null=True, blank=True)
    key2 = models.FileField(upload_to='static/keys', null=True, blank=True)
    key_exp2 = models.DateField(null=True, blank=True)
    passport = models.FileField(null=True, blank=True, upload_to="static/passport/")
    owner = models.CharField(max_length=255, null=True, blank=True)
    tex_number = models.CharField(max_length=255, null=True, blank=True)
    text_series = models.CharField(max_length=255, null=True, blank=True)
    given_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    ustav = models.FileField(null=True, blank=True, upload_to="static/ustav/")
    selfy = models.FileField(null=True, blank=True, upload_to="static/selfy/")
    ruxsatnoma = models.FileField(null=True, blank=True, upload_to="static/ruxsatnoma/")
    workplace = models.CharField(max_length=255, null=True, blank=True)
    texpas = models.FileField(null=True, blank=True, upload_to="static/texpas/")
    order1 = models.CharField(max_length=255, null=True, blank=True)
    order2 = models.CharField(max_length=255, null=True, blank=True)
    order3 = models.CharField(max_length=255, null=True, blank=True)
    auc_login = models.CharField(max_length=255, null=True, blank=True)
    auc_password = models.CharField(max_length=255, null=True, blank=True)
    congragulate = models.BooleanField(null=True, blank=True, default=False)
    bot_login = models.CharField(max_length=255, null=True, blank=True, unique=True)
    bot_password = models.CharField(max_length=255, null=True, blank=True)
    bot_user = models.OneToOneField('Bot_user', null=True, blank=True, on_delete=models.PROTECT)

    # car number and auction
    pledge = models.CharField(null=True, blank=True, max_length=32) # Залог
    start_price = models.CharField(null=True, blank=True, max_length=32)
    end_price = models.CharField(null=True, blank=True, max_length=32)
    up_to_price = models.CharField(null=True, blank=True, max_length=32)
    zaklat = models.CharField(null=True, blank=True, max_length=32)
    sold_price = models.CharField(null=True, blank=True, max_length=32)
    stock_market_price = models.CharField(null=True, blank=True, max_length=32)
    service_fee = models.CharField(null=True, blank=True, max_length=32)
    overall_price = models.CharField(null=True, blank=True, max_length=32)
    win_value = models.CharField(null=True, blank=True, max_length=32)
    overall_payment = models.CharField(null=True, blank=True, max_length=32)

    proxy_owner = models.CharField(max_length=255, null=True, blank=True)
    ishonchnoma = models.FileField(null=True, blank=True, upload_to="static/ishonchnoma/")
    ishonchnoma_files = models.ManyToManyField(File)

    fly_direction = models.CharField(max_length=255, null=True, blank=True)
    brom_date = models.DateField(null=True, blank=True)
    fly_date = models.DateField(null=True, blank=True)
    ticket = models.FileField(null=True, blank=True, upload_to="static/ticket/")
    ticket_price = models.CharField(max_length=255, null=True, blank=True)
    ticket_selled_price = models.CharField(max_length=255, null=True, blank=True)
    profit = models.CharField(max_length=255, null=True, blank=True)
    discount = models.CharField(max_length=255, null=True, blank=True)

    card = models.CharField(max_length=64, null=True, blank=True)
    receipt = models.FileField(null=True, blank=True, upload_to="static/receipt/")
    contract = models.FileField(null=True, blank=True, upload_to="static/contract/")
    period = models.DateField(null=True, blank=True)
    application_files = models.ManyToManyField(File, related_name='application_files')
    profession = models.CharField(null=True, blank=True, max_length=255)
    quarter = models.CharField(null=True, blank=True, max_length=255)

    last_profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.type == 'auction':
            try:
                self.overall_price = str(int(self.sold_price) + int(self.stock_market_price))
                self.overall_payment = str(int(self.overall_price) + int(self.service_fee) - int(self.pledge))
            except Exception as e:
                print(e)

        super(Client, self).save(*args, **kwargs)
        
    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        if self.jshshir:
            return self.name + ' ' + self.jshshir
        else:
            return self.name

    @property
    def is_certificate_expired(self):
        if self.guvohnoma_exp:
            dates = datetime.datetime.strptime(str(self.guvohnoma_exp), "%Y-%m-%d").date()
            today = datetime.date.today()
            subs =  dates -today
            if subs.days >=1 and subs.days <=10:
                return 'in_ten_days'
            elif subs.days >10 and subs.days <=30:
                return 'in_a_month'
            elif subs.days > 30:
                return 'active'
            else:
                return 'inactive'
        else:
            return 'not_found'
    @property
    def is_key_expired(self):
        if self.key_exp:
            dates = datetime.datetime.strptime(str(self.key_exp), "%Y-%m-%d").date()
            today = datetime.date.today()
            subs =  dates -today
            if subs.days >=1 and subs.days <=10:
                return 'in_ten_days'
            elif subs.days >10 and subs.days <=30:
                return 'in_a_month'
            elif subs.days > 30:
                return 'active'
            else:
                return 'inactive'
        else:
            return 'not_found'

    @property
    def is_key2_expired(self):
        if self.key_exp2:
            dates = datetime.datetime.strptime(str(self.key_exp2), "%Y-%m-%d").date()
            today = datetime.date.today()
            subs =  dates -today
            if subs.days >=1 and subs.days <=10:
                return 'in_ten_days'
            elif subs.days >10 and subs.days <=30:
                return 'in_a_month'
            elif subs.days > 30:
                return 'active'
            else:
                return 'inactive'
        else:
            return 'not_found'

    @property
    def is_t_expired(self):
        if self.expiry_date:
            dates = datetime.datetime.strptime(str(self.expiry_date), "%Y-%m-%d").date()
            today = datetime.date.today()
            subs =  dates -today
            if subs.days >=1 and subs.days <=10:
                return 'in_ten_days'
            elif subs.days >10 and subs.days <=30:
                return 'in_a_month'
            elif subs.days > 30:
                return 'active'
            else:
                return 'inactive'
        else:
            return 'not_found'


class Service(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Upload(models.Model):
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    reciever = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='reciever')
    STATUS_CHOICES = (
        ('0','Narxlanmagan'),
        ('5','Bajarilmagan'),
        ('10','Bajarilgan')
    )
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='0')
    payment = models.CharField(max_length=255, null=True, blank=True)
    loaded_date = models.DateTimeField(auto_now_add=True)
    period = models.DateField(null=True, blank=True)
    uploaded_file = models.FileField(upload_to='static/files', null=True, blank=True)
    answer = models.TextField(max_length=350, null=True, blank=True)
    sender = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='sender')
    office = models.CharField(max_length=10)
    comment = models.TextField(null=True, blank=True)
    archived = models.BooleanField(default=False)

    class Meta:
        ordering = ['archived', '-status', 'period']
    
    @property
    def remaining_days(self):
        today = date.today()
        return (self.period - today).days

class Task(models.Model):
    text = models.TextField(max_length=500)
    given_date = models.DateTimeField(auto_now_add=True)
    duration = models.DateField(null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255, null=True, blank=True)
    STATUS_CHOICES = (
        ('0', 'Bajarilmagan'),
        ('5', 'Jarayonda'),
        ('10', 'Tugatilgan'),
    )
    client = models.ManyToManyField(Client, null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=255, default='0')
    given_file = models.FileField(upload_to='static/files/task', null=True, blank=True)
    answer_text = models.TextField(max_length=500, null=True, blank=True)
    answer_file = models.FileField(upload_to='static/files/task', null=True, blank=True)

    OFFICE_CHOICES = (
        ('1', 'XXI ASR BUXGALTERIYA'),
        ('2', 'XXI ASR KOMPYUTER XIZMATLARI'),
        ('3', 'XXI ASR BUXGALTERIYA XIZMATLARI MARKAZI'),
    )
    office = models.CharField(choices=OFFICE_CHOICES, max_length=200)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-given_date']

    @property
    def is_past_due(self):
            return date.today() >= self.duration


class SMS(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    STATUS_CHOICES = (
        ('0', 'Raqam kiritilmagan'),
        ('5', 'Raqam xato kiritilgan'),
        ('10', 'Yuborilgan'),
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client.name


class Notes(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    period = models.DateField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    payment = models.CharField(max_length=255, null=True, blank=True)
    payed = models.CharField(max_length=255, null=True, blank=True)
    comment = models.TextField(max_length=300, null=True, blank=True)
    
    STATUS_CHOICES = (
        ('0', 'Bajarilmagan'),
        ('5', 'Jarayonda'),
        ('10', 'Tugatilgan'),
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=255, default='0')
    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-period']

class SMStext(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField(max_length=300)
    
    
class subscriptions(models.Model):
    name = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    status = models.CharField(max_length=255, null=True, blank=True)
    
class telegramPost(models.Model):
    file = models.FileField(upload_to='static/files/telegram', null=True, blank=True)
    post_type = models.CharField(max_length=255)
    client_type = models.CharField(max_length=255)
    text = models.TextField(max_length=1000, blank=True, null=True)
    
    def __str__(self):
        return self.text
    

class Bot_user(models.Model):
    user_id = models.BigIntegerField(null=True)
    name = models.CharField(null=True, blank=True, max_length=200)
    username = models.CharField(null=True, blank=True, max_length=200)
    firstname = models.CharField(null=True, blank=True, max_length=500)
    phone = models.CharField(null=True, blank=True, max_length=40)
    lang = models.CharField(null=True, blank=True, max_length=5)
    date = models.DateTimeField(db_index = True, null=True, auto_now_add=True, blank=True)
    # client informations
    login = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self) -> str:
        try:
            first = self.name or self.firstname
            second = self.phone or self.username or ''
            return first + ' ' + second
        except:
            return super().__str__()

def template_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/static/templates/user_<id>/<filename>
    return 'static/templates/user_{0}/{1}'.format(instance.user.id, filename)

class Template(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(null=True, blank=True, max_length=255)
    comment = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to=template_directory_path, null=True, blank=True)

class msg(models.Model):
    msg_id = models.BigIntegerField(null=True, blank=True)
    forward_msg_id = models.BigIntegerField(null=True, blank=True)
    user_id = models.BigIntegerField(null=True, blank=True)

class Key(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True, related_name='key_client')
    TYPE_CHOICES = (
        ('ytt','YaTT'),
        ('yuridik','Yuridik shaxs'),
        ('jismoniy','Jismoniy shaxs'),
        ('tanirovka','Tanirovka'),
        ('auction','Avtoraqam'),
        ('auction2','Auksion'),
        ('teacher',"O'qituvchi"),
        ('governor', 'Hokim yordamchisi'),
        ('taxi', 'Taxi litsenziya'),
        ('ishonchnoma', 'Ishonchnoma'),
        ('daromad12', '12% daromad'),
        ('taxer', 'Soliqchi'),
        ('student', 'Talaba'),
        ('mahalla', 'Mahalla')
    )
    type = models.CharField(choices=TYPE_CHOICES, max_length=255, blank=True, null=True)
    jshshir = models.CharField(max_length=255, null=True, blank=True)
    inn = models.CharField(max_length=255, null=True, blank=True)
    added_by = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    key = models.FileField(upload_to='static/keys', null=True, blank=True)
    key_exp = models.DateField(null=True, blank=True)

    @property
    def is_active(self):
        if self.expiry_date:
            dates = datetime.datetime.strptime(str(self.expiry_date), "%Y-%m-%d").date()
            today = datetime.date.today()
            subs =  dates -today
            if subs.days >=1 and subs.days <=10:
                return True
            elif subs.days >10 and subs.days <=30:
                return True
            elif subs.days > 30:
                return True
            else:
                return False
        else:
            return None
    
class ActionHistory(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    client_id = models.BigIntegerField(null=True, blank=True)
    action_time = models.DateTimeField(auto_now_add=True)
    model_name = models.CharField(null=True, blank=True, max_length=255)
    action_type = models.CharField(null=True, blank=True, max_length=50)
    changed_values = models.TextField(null=True, blank=True, )

class Duedate(models.Model):
    client = models.ForeignKey('base.Client', null=True, blank=True, on_delete = models.SET_NULL)
    # STATUS_CHOICES = [
    #     (0, 'inactive'),
    #     (1, 'active')
    # ]
    # status = models.IntegerField(default = 1, choices = STATUS_CHOICES)
    TYPE_CHOICES = [
        ('key', 'Kalit'),
        ('guvohnoma', 'Guvohnoma'),
        ('taxi', 'Taxi litsenziya'),
        ('ishonchnoma', 'Ishonchnoma'),
        ('tanirovka', 'Tanirovka'),
    ]
    type = models.CharField(null=True, blank=True, max_length=64, choices = TYPE_CHOICES)
    comment = models.TextField(null=True, blank=True, default = '')
    due_date = models.DateField(null=True, blank=True)
    is_called = models.BooleanField(default = False)