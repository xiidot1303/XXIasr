import imp
from pyexpat import model
from re import L
from django import forms
from django.forms import DateInput, ModelForm, fields, widgets
from .models import Client, Notes, Profile, Service, Task, Upload, Template, Bot_user


class UploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ['service', 'client','reciever', 'period', 'uploaded_file', 'comment']
        
        class DateInput(forms.DateInput):
            input_type = 'date'
        
            
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
            'period' : DateInput(),
        }
        labels = {
            'service':'Xizmatni tanlang',
            'client':'Mijozni tanlang',
            'reciever':'Xodimni tanlang',
            'uploaded_file':'Fayl biriktirish',
            'period':'Muddat',
            'comment': 'Izoh',
        }
        
        

    def __init__(self, *args, **kvargs):
        super(UploadForm, self).__init__(*args, **kvargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['service'].widget.attrs.update({'class':'form-control js-example-basic-single'})
        self.fields['client'].widget.attrs.update({'class':'form-control js-example-basic-single'})
        self.fields['reciever'].widget.attrs.update({'class':'form-control js-example-basic-single'})
        
class ServiceCreation(ModelForm):
    class Meta:
        model = Service
        fields = ['name','price']
        labels = {
            'name':'Xizmat nomi',
            'price':'Xizmat narxi'
        }

    def __init__(self, *args, **kvargs):
            super(ServiceCreation, self).__init__(*args, **kvargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'form-control'})
        

class TaskCreation(ModelForm):
    class Meta:
        model = Task
        fields = ['text','duration', 'user', 'client','given_file']
        labels = {
            'text':'Topshiriq matni',
            'duration':'Muddati',
            'user':'Xodimlar',
            'client':'Mijozni biriktirish',
            'given_file':'Faylni biriktirish'
        }
        class DateInput(forms.DateInput):
            input_type = 'date'
        
        widgets = {
            'duration': DateInput()
        }

    def __init__(self, *args, **kvargs):
            super(TaskCreation, self).__init__(*args, **kvargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'form-control'})
            self.fields['client'].widget.attrs.update({'class':'js-example-basic-multiple w-100', 'multiple':'multiple'})


class YaTTCreation(ModelForm):
    class Meta:
        model = Client
        fields = ['picture', 'name', 'tin','sub_type', 'gov_login', 'gov_password', 'jshshir', 'guvohnoma_exp', 
            'phone1', 'phone2', 'phone3', 'address', 'key', 'key_exp', 'key2', 'key_exp2', 'guvohnoma_file', 'passport', 'selfy', 'bot_user', 'bot_login', 'bot_password']
        labels = {
            'picture':'Rasm',
            'name': 'Nom',
            'tin':'STIR',
            'gov_login' : 'id.gov login',
            'gov_password' : 'id.gov parol',
            'jshshir': 'JSHSHIR',
            'guvohnoma_exp':'Guvohnoma muddati',
            'phone1' : 'Telefon',
            'phone2' : 'Telefon 2',
            'phone3' : 'Telefon 3',
            'bot_user' : 'Telegram foydalanuvchisi',
            'address' : 'Manzil',
            'key':'Kalit e-imzo',
            'key_exp':'Kalit e-imzo muddati',            
            'key2':'Kalit 2 e-auksion',
            'key_exp2':'Kalit 2 e-auksion muddati',
            'guvohnoma_file':'Guvohnoma fayli',
            'passport':'Pasport',
            'selfy':'Selfi',
            'sub_type':'Hisobot turi',
            'bot_login': 'Login',
            'bot_password': 'Parol',
        }

        class DateInput(forms.DateInput):
            input_type = 'date'
            
        widgets = {
            'key_exp':DateInput(),
            'key_exp2':DateInput(),
            'guvohnoma_exp':DateInput()
        }

    
     

    def __init__(self, *args, **kvargs):
        super(YaTTCreation, self).__init__(*args, **kvargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'required':'required'})
        self.fields['jshshir'].widget.attrs.update({'required':'required'})
        self.fields['phone1'].widget.attrs.update({'required':'required'})
        self.fields['address'].widget.attrs.update({'required':'required'})
        self.fields['bot_user'].widget.attrs.update({'class':'form-control js-example-basic-single'})




class YuridikCreation(ModelForm):
    class Meta:
        model = Client
        
        fields = ['picture', 'name', 'yuridik_type', 'tin', 'gov_login', 'gov_password','director', 'director_tin', 'jshshir', 
            'phone1', 'phone2', 'phone3', 'key', 'key_exp', 'guvohnoma_file', 'ustav','passport', 'selfy', 
            'bot_user', 'bot_login', 'bot_password', 'key2', 'key_exp2']
        labels = {
            'picture':'Rasm',
            'name': 'Nom',
            'yuridik_type': 'Turi',
            'tin':'STIR',
            'gov_login' : 'id.gov login',
            'gov_password' : 'id.gov parol',
            'director': 'Direktor',
            'director_tin' : 'Direktor STIRi',
            'jshshir': 'JSHSHIR',
            'phone1' : 'Telefon',
            'phone2' : 'Telefon 2',
            'phone3' : 'Telefon 3',
            'bot_user' : 'Telegram foydalanuvchisi',
            'key':'Kalit',
            'key_exp':'Kalit muddati',
            'key2':'Kalit (Jismoniy)',
            'key_exp2':'Kalit muddati (Jismoniy)',
            'guvohnoma_file':'Guvohnoma fayli',
            'ustav':'Ustav',
            'passport':'Pasport',
            'selfy':'Selfi',
            'bot_login': 'Login',
            'bot_password': 'Parol',
        }
        
        class DateInput(forms.DateInput):
            input_type = 'date'
        
        widgets = {
            'key_exp':DateInput(),
            'key_exp2':DateInput(),
            # 'key_exp': forms.DateInput(attrs={'type': 'date'}, format='%d-%m-%Y')
        }
        
    

    def __init__(self, *args, **kvargs):
        super(YuridikCreation, self).__init__(*args, **kvargs)
        # self.fields['key_exp'] = forms.DateField(input_formats=['%d/%m/%y'], widget=forms.DateInput(attrs={'type': "date"}))
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'required':'required'})
        self.fields['jshshir'].widget.attrs.update({'required':'required'})
        self.fields['tin'].widget.attrs.update({'required':'required'})
        self.fields['director'].widget.attrs.update({'required':'required'})
        self.fields['phone1'].widget.attrs.update({'required':'required'})
        self.fields['phone2'].widget.attrs.update({'required':'required'})
        self.fields['bot_user'].widget.attrs.update({'class':'form-control js-example-basic-single'})
        


class JismoniyCreation(ModelForm):
    class Meta:
        model = Client
        fields = ['picture', 'name', 'tin', 'gov_login', 'gov_password', 'jshshir', 'phone1', 'phone2', 
            'phone3', 'key', 'key_exp', 'key2', 'key_exp2', 'passport', 'selfy', 'bot_login', 'bot_password', 'bot_user']
        labels = {
            'picture':'Rasm',
            'name': 'Nom',
            'tin':'STIR',
            'gov_login' : 'id.gov login',
            'gov_password' : 'id.gov parol',
            'jshshir': 'JSHSHIR',
            'phone1' : 'Telefon',
            'phone2' : 'Telefon 2',
            'phone3' : 'Telefon 3',
            'bot_user' : 'Telegram foydalanuvchisi',
            'key': 'Kalit e-imzo',
            'key_exp':'Kalit e-imzo muddati',            
            'key2': 'Kalit 2 e-auksion',
            'key_exp2':'Kalit 2 e-auksion muddati',
            'passport':'Pasport',
            'selfy':'Selfi',
            'bot_login': 'Login',
            'bot_password': 'Parol',
        }
        
        class DateInput(forms.DateInput):
            input_type = 'date'
            
        widgets = {
            'key_exp':DateInput(),
            'key_exp2':DateInput(),
        }

    def __init__(self, *args, **kvargs):
        super(JismoniyCreation, self).__init__(*args, **kvargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'required':'required'})
        self.fields['jshshir'].widget.attrs.update({'required':'required'})
        self.fields['phone1'].widget.attrs.update({'required':'required'})
        self.fields['bot_user'].widget.attrs.update({'class':'form-control js-example-basic-single'})


class TaxiCreation(ModelForm):
    class Meta:
        model = Client
        fields = ['picture', 'name', 'owner', 'tex_number', 'text_series', 'ruxsatnoma', 'given_date', 'expiry_date', 
            'tin', 'gov_login', 'gov_password', 'jshshir', 'phone1', 'phone2', 
            'phone3', 'key', 'key_exp', 'passport', 'selfy', 'bot_login', 'bot_password', 'bot_user']
        labels = {
            'picture':'Rasm',
            'name': 'Nom',
            'owner': 'Avtomobil egasi',
            'tex_number':'Avtomashina raqami',
            'text_series': 'Tex pasport seriyasi',
            'given_date':'Ruxsatnoma berilgan sanasi',
            'expiry_date':'Ruxsatnoma tugash sanasi',
            'ruxsatnoma': 'Litsenziya',
            'tin':'STIR',
            'gov_login': 'id.gov login',
            'gov_password' : 'id.gov parol',
            'jshshir': 'JSHSHIR',
            'phone1' : 'Telefon',
            'phone2' : 'Telefon 2',
            'phone3' : 'Telefon 3',
            'bot_user' : 'Telegram foydalanuvchisi',
            'key': 'Kalit',
            'key_exp':'Kalit muddati',
            'passport':'Pasport',
            'selfy':'Selfi',
            'bot_login': 'Login',
            'bot_password': 'Parol',
        }
        
        class DateInput(forms.DateInput):
            input_type = 'date'
            
        widgets = {
            'key_exp':DateInput(),
            'expiry_date':DateInput(),
            'given_date':DateInput(),
        }

        
       

    def __init__(self, *args, **kvargs):
        super(TaxiCreation, self).__init__(*args, **kvargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'required':'required'})
        self.fields['jshshir'].widget.attrs.update({'required':'required'})
        self.fields['phone1'].widget.attrs.update({'required':'required'})
        self.fields['bot_user'].widget.attrs.update({'class':'form-control js-example-basic-single'})



class IshonchnomaCreation(ModelForm):
    ishonchnoma_files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False, label="Ishonchnomalar")
    class Meta:
        model = Client
        fields = ['picture', 'proxy_owner', 'name', 'tex_number', 'text_series', 'ishonchnoma', 'ishonchnoma_files', 'given_date', 'expiry_date', 
            'gov_login', 'gov_password', 'jshshir', 'phone1', 'phone2', 
            'phone3', 'key', 'key_exp', 'passport', 'selfy', 'bot_login', 'bot_password', 'bot_user']
        labels = {
            'picture':'Rasm',
            'proxy_owner': 'Ishonchnoma oluvchi',
            'name': 'Avtomobil egasi',
            'tex_number':'Avtomashina raqami',
            'text_series': 'Tex pasport seriyasi',
            'given_date':'Ishonchnoma berilgan sanasi',
            'expiry_date':'Ishonchnoma tugash sanasi',
            'ishonchnoma': 'Ishonchnoma',
            'ishonchnoma_files': 'Ishonchnomalar',
            'gov_login': 'id.gov login',
            'gov_password' : 'id.gov parol',
            'jshshir': 'JSHSHIR',
            'phone1' : 'Telefon',
            'phone2' : 'Telefon 2',
            'phone3' : 'Telefon 3',
            'bot_user' : 'Telegram foydalanuvchisi',
            'key': 'Kalit',
            'key_exp':'Kalit muddati',
            'passport':'Pasport',
            'selfy':'Selfi',
            'bot_login': 'Login',
            'bot_password': 'Parol',
        }
        
        class DateInput(forms.DateInput):
            input_type = 'date'
            
        widgets = {
            'key_exp':DateInput(),
            'expiry_date':DateInput(),
            'given_date':DateInput(),
        }

        
       

    def __init__(self, *args, **kvargs):
        super(IshonchnomaCreation, self).__init__(*args, **kvargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['proxy_owner'].widget.attrs.update({'required':'required'})
        self.fields['name'].widget.attrs.update({'required':'required'})
        self.fields['jshshir'].widget.attrs.update({'required':'required'})
        self.fields['phone1'].widget.attrs.update({'required':'required'})
        self.fields['bot_user'].widget.attrs.update({'class':'form-control js-example-basic-single'})



class TanirovkaCreation(ModelForm):
    class Meta:
        model = Client
        fields = ['picture', 'owner', 'name',  'jshshir', 'tex_number', 'text_series', 'given_date',  
            'expiry_date', 'gov_login', 'gov_password', 'passport', 'ruxsatnoma', 'texpas', 'phone1', 
                'phone2', 'phone3', 'bot_user', 'bot_login', 'bot_password']
        labels = {
            'picture':'Rasm',
            'owner': 'Avtomobil egasi',
            'name': 'Kim buyurtma qildi',
            'jshshir': 'JSHSHIR',
            'tex_number':'Tex pasport raqami',
            'text_series': 'Tex pasport seriyasi',
            'given_date':'Ruxsatnoma berilgan sanasi',
            'expiry_date':'Ruxsatnoma tugash sanasi',
            'gov_login' : 'id.gov login',
            'gov_password' : 'id.gov parol',
            'passport': 'Pasport',
            'ruxsatnoma': 'Ruxsatnoma',
            'texpas':'Texpasport',
            'phone1' : 'Telefon',
            'phone2' : 'Telefon 2',
            'phone3' : 'Telefon 3',
            'bot_user' : 'Telegram foydalanuvchisi',
            'bot_login': 'Login',
            'bot_password': 'Parol',
        }
        
        
        class DateInput(forms.DateInput):
            input_type = 'date'
            
        widgets = {
            'given_date':DateInput(),
            'expiry_date':DateInput()

        }

    def __init__(self, *args, **kvargs):
        super(TanirovkaCreation, self).__init__(*args, **kvargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'required':'required'})
        self.fields['owner'].widget.attrs.update({'required':'required'})
        self.fields['jshshir'].widget.attrs.update({'required':'required'})
        self.fields['phone1'].widget.attrs.update({'required':'required'})
        self.fields['bot_user'].widget.attrs.update({'class':'form-control js-example-basic-single'})


class AuctionCreation(ModelForm):
    class Meta:
        model = Client
        fields = ['picture', 'owner', 'name',  'jshshir', 'order1', 'order2', 'order3', 'auc_login', 
            'auc_password', 'gov_login', 'gov_password',  'passport','phone1', 'phone2', 'phone3', 
            'address', 'pledge', 'start_price', 'sold_price', 'stock_market_price', 'service_fee',
            'bot_user', 'bot_login', 'bot_password', 
            ]
        labels = {
            'picture':'Rasm',
            'owner': 'Avtomobil egasi',
            'name': 'Kim buyurtma qildi',
            'jshshir': 'JSHSHIR',
            'order1' : '1-buyurtma',
            'order2' : '2-buyurtma',
            'order3' : '3-buyurtma',
            'auc_login' : 'Auksion login',
            'auc_password' : 'Auksion parol',
            'gov_login' : 'id.gov login',
            'gov_password' : 'id.gov parol',
            'passport':'Pasport nusxasi',
            'phone1' : 'Telefon',
            'phone2' : 'Telefon 2',
            'phone3' : 'Telefon 3',
            'bot_user' : 'Telegram foydalanuvchisi',
            'bot_login': 'Login',
            'bot_password': 'Parol',
            'address': 'Yashash manzili',
            'pledge': 'Oldindan to\'lov',
            'start_price': 'Boshlang\'ich avtoraqam summasi',
            'sold_price': 'Sotib olingan avtoraqam summasi',
            'stock_market_price': 'Yakuniy birja tolovi',
            'service_fee': 'Xizmat haqi',

        }
     
    def __init__(self, *args, **kvargs):
        super(AuctionCreation, self).__init__(*args, **kvargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['owner'].widget.attrs.update({'required':'required'})
        self.fields['order1'].widget.attrs.update({'required':'required'})
        self.fields['jshshir'].widget.attrs.update({'required':'required'})
        self.fields['phone1'].widget.attrs.update({'required':'required'})
        self.fields['auc_login'].widget.attrs.update({'required':'required'})
        self.fields['auc_password'].widget.attrs.update({'required':'required'})
        self.fields['bot_user'].widget.attrs.update({'class':'form-control js-example-basic-single'})


class Auction2Creation(ModelForm):
    class Meta:
        model = Client
        fields = ['picture', 'name',  'jshshir', 'auc_login', 
            'auc_password', 'gov_login', 'gov_password',  'passport','phone1', 'phone2', 'phone3', 
            'address', 'address2', 'start_price', 'up_to_price', 'zaklat', 'pledge', 
            'overall_price', 'win_value', 'service_fee', 'overall_payment', 'bot_user', 'bot_login', 'bot_password', 
            ]
        labels = {
            'picture':'Rasm',
            'name': 'Buyurtmachi',
            'jshshir': 'JSHSHIR',
            'auc_login' : 'Auksion login',
            'auc_password' : 'Auksion parol',
            'gov_login' : 'id.gov login',
            'gov_password' : 'id.gov parol',
            'passport':'Pasport nusxasi',
            'phone1' : 'Telefon',
            'phone2' : 'Telefon 2',
            'phone3' : 'Telefon 3',
            'bot_user' : 'Telegram foydalanuvchisi',
            'bot_login': 'Login',
            'bot_password': 'Parol',
            'address': 'Yashash manzili',
            'address2': 'Mulk manzili',
            'start_price': 'Mulk boshlang\'ich narxi',
            # 'end_price': 'Mulk tugash narxi',
            'up_to_price': 'Qancha summagacha o\'ynaladi',
            'zaklat': 'Auksion zaklat summasi',
            'pledge': 'Oldindan to\'lov',
            'overall_price': 'Umumiy to\'lov',
            'win_value': 'Yutib olingan summa',
            'service_fee': 'Xizmat haqi',
            'overall_payment': 'Jami to\'lov',

        }
     
    def __init__(self, *args, **kvargs):
        super(Auction2Creation, self).__init__(*args, **kvargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'required':'required'})
        self.fields['jshshir'].widget.attrs.update({'required':'required'})
        self.fields['phone1'].widget.attrs.update({'required':'required'})
        self.fields['auc_login'].widget.attrs.update({'required':'required'})
        self.fields['auc_password'].widget.attrs.update({'required':'required'})
        self.fields['bot_user'].widget.attrs.update({'class':'form-control js-example-basic-single'})



class TeacherCreation(ModelForm):
    class Meta:
        model = Client
        fields = ['picture', 'name','school', 'work_as', 'phone1', 'phone2', 'phone3', 'bot_login', 'bot_password', 'bot_user']
        labels = {
            'picture':'Rasm',
            'name': 'F.I.Sh.',
            'school' :'Maktab',
            'work_as' : 'Lavozim',
            'phone1' : 'Telefon',
            'phone2' : 'Telefon 2',
            'phone3' : 'Telefon 3',
            'bot_user' : 'Telegram foydalanuvchisi',
            'bot_login': 'Login',
            'bot_password': 'Parol'
        }
     
    def __init__(self, *args, **kvargs):
        super(TeacherCreation, self).__init__(*args, **kvargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'required':'required'})
        self.fields['bot_user'].widget.attrs.update({'class':'form-control js-example-basic-single'})




class GovernorCreation(ModelForm):
    class Meta:
        model = Client
        fields = ['picture', 'name', 'workplace', 'tin', 'gov_login', 'gov_password', 'jshshir', 'phone1', 'phone2', 
            'phone3', 'key', 'key_exp', 'passport', 'selfy', 'bot_login', 'bot_password', 'bot_user']
        labels = {
            'picture':'Rasm',
            'name': 'Nom',
            'tin':'STIR',
            'gov_login' : 'id.gov login',
            'gov_password' : 'id.gov parol',
            'jshshir': 'JSHSHIR',
            'phone1' : 'Telefon',
            'phone2' : 'Telefon 2',
            'phone3' : 'Telefon 3',
            'bot_user' : 'Telegram foydalanuvchisi',
            'key': 'Kalit',
            'key_exp':'Kalit muddati',
            'passport':'Pasport',
            'selfy':'Selfi',
            'bot_login': 'Login',
            'bot_password': 'Parol',
            'workplace': 'Ish joyi'
        }
        
        class DateInput(forms.DateInput):
            input_type = 'date'
            
        widgets = {
            'key_exp':DateInput()
        }

        
       

    def __init__(self, *args, **kvargs):
        super(GovernorCreation, self).__init__(*args, **kvargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'required':'required'})
        # self.fields['jshshir'].widget.attrs.update({'required':'required'})
        self.fields['phone1'].widget.attrs.update({'required':'required'})
        self.fields['bot_user'].widget.attrs.update({'class':'form-control js-example-basic-single'})


class Daromad12Creation(ModelForm):
    application_files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False, label="Ilova fayllari")
    class Meta:
        model = Client
        fields = ['picture', 'name', 'jshshir', 'phone1', 'phone2', 'key', 'key_exp',
            'card', 'application_files', 'receipt', 'contract', 'period', 'bot_login', 'bot_password', 'bot_user']
        labels = {
            'picture':'Rasm',
            'name': 'Nom',
            'jshshir': 'JSHSHIR',
            'phone1' : 'Telefon',
            'phone2' : 'Telefon 2',
            'bot_user' : 'Telegram foydalanuvchisi',
            'key': 'Kalit',
            'key_exp':'Kalit muddati',
            'bot_login': 'Login',
            'bot_password': 'Parol',
            'card': 'Karta ma\'lumotlari',
            'receipt': 'Kvitansiya ma\'lumotlari',
            'contract': 'Shartnoma qog\'ozi',
            'application_files': 'Ilova fayllari',
            'period': 'Ariza muddati',
        }
        
        class DateInput(forms.DateInput):
            input_type = 'date'
            
        widgets = {
            'key_exp':DateInput(),
            'period':DateInput()
        }

        
       

    def __init__(self, *args, **kvargs):
        super(Daromad12Creation, self).__init__(*args, **kvargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'required':'required'})
        # self.fields['jshshir'].widget.attrs.update({'required':'required'})
        self.fields['phone1'].widget.attrs.update({'required':'required'})
        self.fields['bot_user'].widget.attrs.update({'class':'form-control js-example-basic-single'})



class AviakassaCreation(ModelForm):
    class Meta:
        model = Client
        fields = ['picture', 'name', 'phone1', 'phone2', 'passport', 'fly_direction', 'brom_date', 'fly_date', 'jshshir',
            'ticket', 'ticket_price', 'ticket_selled_price', 'profit', 'discount', 'bot_login', 'bot_password', 'bot_user']
        labels = {
            'picture':'Rasm',
            'name': 'Nom',
            'jshshir': 'JSHSHIR',
            'phone1' : 'Telefon',
            'phone2' : 'Telefon 2',
            'phone3' : 'Telefon 3',
            'fly_direction': 'Parvoz yo\'nalishi', 
            'brom_date': 'Brom sanasi', 
            'fly_date': 'Uchish sanasi', 
            'passport':'Pasport',
            'ticket': 'Chipta', 
            'ticket_price': 'Chipta narxi', 
            'ticket_selled_price': 'Sotilgan narxi', 
            'profit': 'Olingan foyda', 
            'discount': 'Berilgan chegirma', 
            'bot_user' : 'Telegram foydalanuvchisi',
            'bot_login': 'Login',
            'bot_password': 'Parol',
        }
        
        class DateInput(forms.DateInput):
            input_type = 'date'
            
        widgets = {
            'brom_date':DateInput(),
            'fly_date':DateInput()
        }

        
       

    def __init__(self, *args, **kvargs):
        super(AviakassaCreation, self).__init__(*args, **kvargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'required':'required'})
        self.fields['jshshir'].widget.attrs.update({'required':'required'})
        self.fields['phone1'].widget.attrs.update({'required':'required'})
        self.fields['bot_user'].widget.attrs.update({'class':'form-control js-example-basic-single'})



class TaxerCreation(ModelForm):
    class Meta:
        model = Client
        fields = ['picture', 'name', 'work_as', 'phone1', 'phone2', 'phone3', 'bot_login', 'bot_password', 'bot_user']
        labels = {
            'picture':'Rasm',
            'name': 'F.I.Sh.',
            'work_as' : 'Lavozim',
            'phone1' : 'Telefon',
            'phone2' : 'Telefon 2',
            'phone3' : 'Telefon 3',
            'bot_user' : 'Telegram foydalanuvchisi',
            'bot_login': 'Login',
            'bot_password': 'Parol'
        }
     
    def __init__(self, *args, **kvargs):
        super(TaxerCreation, self).__init__(*args, **kvargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'required':'required'})
        self.fields['phone1'].widget.attrs.update({'required':'required'})
        self.fields['bot_user'].widget.attrs.update({'class':'form-control js-example-basic-single'})




class StudentCreation(ModelForm):
    class Meta:
        model = Client
        fields = ['picture', 'name', 'passport', 'jshshir', 'gov_login', 'gov_password', 'phone1', 'phone2', 'phone3', 'profession', 'bot_user']
        labels = {
            'picture':'Rasm',
            'name': 'F.I.Sh.',
            'passport': 'Passport',
            'jshshir': 'Jshshr',
            'gov_login': 'Login',
            'gov_password': 'Parol',
            'phone1' : 'Telefon',
            'phone2' : 'Telefon 2',
            'phone3' : 'Telefon 3',
            'profession' : 'Yo\'nalishi',
            'bot_user' : 'Telegram foydalanuvchisi',

        }
     
    def __init__(self, *args, **kvargs):
        super(StudentCreation, self).__init__(*args, **kvargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'required':'required'})
        self.fields['phone1'].widget.attrs.update({'required':'required'})
        self.fields['bot_user'].widget.attrs.update({'class':'form-control js-example-basic-single'})




class NotesCreation(ModelForm):
    
    class Meta:
        model = Notes
        exclude = ['user', 'status']
        labels = {
            'text': 'Mavzu',
            'period': 'Muddat',
            'client': 'Mijoz',
            'service' : 'Xizmat turi',
            'payment' : 'To\'lov',
            'payed':'To\'landi',
            'comment':'Izoh'
        }
        
        class DateInput(forms.DateInput):
            input_type = 'date'
            

        widgets = {
            'period': DateInput(),
        }
    
    def __init__(self, *args, **kvargs):
        super(NotesCreation, self).__init__(*args, **kvargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['text'].widget.attrs.update({'required':'required'})
        self.fields['client'].widget.attrs.update({'class':'form-control js-example-basic-single'})


class ProfileCreation(ModelForm):
    class Meta:
        model = Profile
        fields = ['picture', 'name', 'status', 'office', 'phone', 'password']
        labels = {
            'picture':'Rasm',
            'name': 'F.I.Sh.',
            'status' : 'Status',
            'office' : 'Ofis',
            'phone' : 'Telefon',
            'password' : 'Parol'
        }
     
    def __init__(self, *args, **kvargs):
        super(ProfileCreation, self).__init__(*args, **kvargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'required':'required'})

class TemplateForm(ModelForm):
    class Meta:
        model = Template
        fields = ['title', 'comment', 'file']
        labels = {
            'title': 'Nom', 
            'comment': 'Izoh', 
            'file': "Fayl"
        }
    def __init__(self, *args, **kvargs):
        super(TemplateForm, self).__init__(*args, **kvargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['title'].widget.attrs.update({'required':'required'})

class Bot_userForm(ModelForm):
    class Meta:
        model = Bot_user
        fields = ['name', 'phone']
        labels = {
            'name': 'Ism',
            'phone': 'Telefon raqam'
        }

    def __init__(self, *args, **kvargs):
        super(Bot_userForm, self).__init__(*args, **kvargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
