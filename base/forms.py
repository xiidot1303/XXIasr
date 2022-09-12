import imp
from pyexpat import model
from re import L
from django import forms
from django.forms import DateInput, ModelForm, fields, widgets
from .models import Client, Notes, Profile, Service, Task, Upload


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
            'phone1', 'phone2', 'phone3', 'address', 'key', 'key_exp', 'guvohnoma_file', 'passport', 'selfy', 'bot_user', 'bot_login', 'bot_password']
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
            'key':'Kalit',
            'key_exp':'Kalit muddati',
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
        
        fields = ['picture', 'name', 'tin', 'gov_login', 'gov_password','director', 'director_tin', 'jshshir', 
            'phone1', 'phone2', 'phone3', 'key', 'key_exp', 'guvohnoma_file', 'ustav','passport', 'selfy', 'bot_user', 'bot_login', 'bot_password']
        labels = {
            'picture':'Rasm',
            'name': 'Nom',
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
            'key_exp':DateInput()
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
        }
        
        class DateInput(forms.DateInput):
            input_type = 'date'
            
        widgets = {
            'key_exp':DateInput()
        }

        
       

    def __init__(self, *args, **kvargs):
        super(JismoniyCreation, self).__init__(*args, **kvargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
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
            'address', 'address2', 'start_price', 'end_price', 'up_to_price', 'zaklat', 'pledge', 
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
            'end_price': 'Mulk tugash narxi',
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