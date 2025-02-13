from django.db import models

# ========= USER MODEL ===========
class EduaddaUser(models.Model):
    USER_ID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=255, null=True, blank=True, default='')
    EMAIL = models.CharField(max_length=255, null=True, blank=True, default='')
    ABOUT_ME = models.CharField(max_length=255, null=True, blank=True, default='')
    IS_ACTIVE = models.IntegerField(null=True, blank=True, default=1)
    PR_OTP = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_OTP_TIME = models.CharField(max_length=255,null=True, blank=True, default='')
    PASSWORD = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'Eduadda_user'
        
        
class UserSession(models.Model):
    SESSION_ID = models.AutoField(primary_key=True)
    USER = models.ForeignKey(EduaddaUser, on_delete=models.CASCADE)
    TOKEN = models.CharField(max_length=500)  # Store a unique token here
    DEVICE_INFO = models.CharField(max_length=255, null=True, blank=True)  # e.g., "iPhone", "Chrome on Windows"
    IP_ADDRESS = models.GenericIPAddressField(null=True, blank=True)  # To track login IP
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    EXPIRES_AT = models.DateTimeField()  # To handle token expiration

        
        
# ========= COURSE MODEL ===========
class EduaddaCourse(models.Model):
    COURSE_ID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=255, null=True, blank=True, default='')
    DESCRIPTION = models.TextField(null=True, blank=True, default='')
    THUMBNAIL = models.CharField(max_length=255, null=True, blank=True, default='/media/default-img.png')
    VIDEO = models.CharField(max_length=255, null=True, blank=True, default='')
    PRICE = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS = models.IntegerField(null=True, blank=True, default=0)
    CATEGORY = models.IntegerField(null=True, blank=True, default=0)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "Eduadda_course"
        
        
        
        
        
# ========= NOTES MODEL ===========
class EduaddaNotes(models.Model):
    NOTES_ID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=255, null=True, blank=True, default='')
    DESCRIPTION = models.TextField(null=True, blank=True, default='')
    THUMBNAIL = models.CharField(max_length=255, null=True, blank=True, default='/media/default-img.png')
    PDF = models.CharField(max_length=255, null=True, blank=True, default='')
    PRICE = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS = models.IntegerField(null=True, blank=True, default=0)
    CATEGORY = models.IntegerField(null=True, blank=True, default=0)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "Eduadda_notes"
        
        
# ========= COURSE PURCHASE MODEL ===========
class EduaddaCoursePurchase(models.Model):
    PURCHASE_ID = models.AutoField(primary_key=True)
    USER = models.ForeignKey(EduaddaUser, on_delete=models.CASCADE)
    COURSE = models.ForeignKey(EduaddaCourse, on_delete=models.CASCADE)
    razorpay_order_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=255, blank=True, null=True)
    PURCHASE_DATE = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "Eduadda_course_purchase"


# ========= NOTES PURCHASE MODEL ===========
class EduaddaNotesPurchase(models.Model):
    PURCHASE_ID = models.AutoField(primary_key=True)
    USER = models.ForeignKey(EduaddaUser, on_delete=models.CASCADE)
    NOTE = models.ForeignKey(EduaddaNotes, on_delete=models.CASCADE)
    razorpay_order_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=255, blank=True, null=True)
    PURCHASE_DATE = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "Eduadda_notes_purchase"
        
 
# ========= BANNER  MODEL ===========     
class EduaddaBanner(models.Model):
    PR_BANNER_ID = models.AutoField(primary_key=True)
    PR_TITLE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_IMAGE = models.CharField(max_length=255, null=True, blank=True, default='/media/default-img.png')
    PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
  
  
    class Meta:
        db_table = 'Eduadda_banner'
        
        
class EduaddaFileData(models.Model):
    PR_FILE_ID = models.AutoField(primary_key=True)
    PR_FILE = models.FileField(upload_to='media/file-data/', null=True, blank=True)
    PR_META_TAG = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Eduadda_file_data'