from django.db import models

USER_CHOICES = (('admin','admin'),
                ('custmer','custmer'),
                ('user','user'),
                )
class role(models.Model):
    id = models.BigAutoField(primary_key=True)
    Usertypename = models.CharField(choices=USER_CHOICES,max_length=50)
    def __str__(self):
            return  self.Usertypename


STATUS_CHOICES = (('ACTIVE','ACTIVE'),
                ('inactie','inactive'),
                )
class userdetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    userpass = models.CharField(max_length=50)
    useremail = models.EmailField()
    userphone = models.IntegerField()
    urole = models.ForeignKey(role,on_delete=models.CASCADE)
    u_status = models.CharField(choices=STATUS_CHOICES,max_length=50)
    def __str__(self):
            return  self.username

COUNTY_CHOICES = (('INDIA','INDIA'),
                ('america','america'),
                  ('caneda','caneda'),
                )
class county(models.Model):
    id = models.BigAutoField(primary_key=True)
    countyname = models.CharField(choices=COUNTY_CHOICES,max_length=50)
    def __str__(self):
            return  self.countyname

STATE_CHOICES = (('BHARAT','BHARAT'),
                ('BIHAR','BIHAR'),
                  ('KASMIR','KSM'),
                )
class state(models.Model):
    id = models.BigAutoField(primary_key=True)
    countyid =models.ForeignKey(county,on_delete=models.CASCADE,null=True)
    statename = models.CharField(choices=STATE_CHOICES,max_length=50)
    def __str__(self):
            return  self.statename

CITY_CHOICES = (('SURAT','SURAT'),
                ('BHAVNAGAR','BHAVNAGAR'),
                  ('AMEDABAD','AMD'),
                )
class city(models.Model):
    id = models.BigAutoField(primary_key=True,)
    stateid = models.ForeignKey(state,on_delete=models.CASCADE,null=True)
    cityname = models.CharField(choices=CITY_CHOICES,max_length=50)
    def __str__(self):
        return self.cityname

class useraddress(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.ForeignKey(userdetail,on_delete=models.CASCADE)
    buildingname = models.TextField(max_length=10)
    streetname = models.TextField(max_length=20)
    cityname = models.ForeignKey(city,on_delete=models.CASCADE)
    pincode = models.CharField(max_length=50)

MONTH_CHOICES = (('jan','jan'),
                ('feb','feb'),
                  ('march','march'),
                 ('apr','apr'),
                 ('may','may'),
                 ('jun','jun'),
                 ('jul','jul'),
                 ('aug','aug'),
                 ('sep','sep'),
                 ('oct','oct'),
                 ('nov','nov'),
                 ('dec','dec'),
                 )
YEAR_CHOICES = (('2020','2020'),
                ('2021','2021'),
                  ('2022','2022'),
                  ('2023','2023'),
                 ('2024','2024'),
                 ('2025','2025'),
                 ('2026','2026'),
                 ('2027','2027'),
                 ('2028','2028'),
                 ('2029','2029'),
                ('2030','2030'),
                )

class bankdetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    buserdetail=models.ForeignKey(userdetail, on_delete=models.CASCADE)
    bankname = models.CharField(max_length=50)
    acnumbr = models.CharField(max_length=20)
    Endmonth = models.CharField(choices=MONTH_CHOICES,max_length=10)
    endyear = models.CharField(choices=YEAR_CHOICES,max_length=20)

