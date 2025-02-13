class CbtConstants:
    CBT_PREFIX='pr_'
    CBT_EMPLOYEE=CBT_PREFIX+"employee"
    CBT_EMPLOYEE_DETAIL=CBT_PREFIX+"employee_detail"
    CBT_EMPLOYEE_ADDRESS=CBT_PREFIX+"employee_address"
    CBT_ATTENDANCE=CBT_PREFIX+'attendance'
    CBT_ATTENDANCE_REQ=CBT_PREFIX+'attendancereq'
    CBT_PARTY = CBT_PREFIX+'party'
    CBT_LEAVE_REQ=CBT_PREFIX+'leavereq'
    CBT_EMPLOYEE_TRACK=CBT_PREFIX+'employee_track'
    CBT_COMMON=CBT_PREFIX+'common_data'
    CBT_CONTROL=CBT_PREFIX+'control'
    CBT_CONTROL_PERMISSION=CBT_PREFIX+'control_permission'
    CBT_DEPARTMENT=CBT_PREFIX+'department'
    CBT_DESIGNATION=CBT_PREFIX+'designation'
    CBT_HEAD_QUATER=CBT_PREFIX+'headquater'
    CBT_HOLIDAY=CBT_PREFIX+'holiday'
    CBT_MENU=CBT_PREFIX+'menu'
    CBT_SUBMENU=CBT_PREFIX+'submenu'
    CBT_MENU_PERMISSION=CBT_PREFIX+'menu_permission'
    CBT_PAGE = CBT_PREFIX + 'page'
    CBT_PAGE_CONTROL=CBT_PREFIX+'page_control'
    CBT_ROUTE=CBT_PREFIX+'route'
    CBT_LOGS=CBT_PREFIX+'logs'
    CBT_CITIES=CBT_PREFIX+'cities'
    CBT_COUNTRY=CBT_PREFIX+'country'
    CBT_STATE=CBT_PREFIX+'state'
    CBT_EVENTS=CBT_PREFIX+'events'
    CBT_CLIENTS=CBT_PREFIX+'clients'
    CBT_COMPANY_QR=CBT_PREFIX+'client_qrstring'
    CBT_COMPANY=CBT_PREFIX+'company'
    CBT_COMPANY_ADDRESS=CBT_PREFIX+'company_address'
    CBT_DROP_DOWN=CBT_PREFIX+'dropdown'
    CBT_DAYPLAN = CBT_PREFIX+'dayplan'
    CBT_LEADS = CBT_PREFIX+'leads'
    CBT_LEAD_ASSIGN = CBT_PREFIX+'lead_assign'
    CBT_LEAD_TRANS = CBT_PREFIX+'lead_trans'
    CBT_LEAD_ADDRESS_TRANS = CBT_PREFIX+'lead_address_trans'
    CBT_LEAD_PRODUCT_TRANS = CBT_PREFIX+'lead_product_trans'
    CBT_ALL_LEADS = CBT_PREFIX+'all_leads'
    CBT_NEW_LEADS = CBT_PREFIX+'new_leads'
    CBT_BRAND = CBT_PREFIX+'brand'
    CBT_CATEGORY = CBT_PREFIX+'category'
    CBT_PRODUCT = CBT_PREFIX+'product'
    CBT_PRODUCT_BATCH = CBT_PREFIX+'product_batch'
    CBT_PRODUCT_IMAGE = CBT_PREFIX+'product_image'
    CBT_PRODUCT_MANUFACTURE = CBT_PREFIX+'product_manufacture'
    CBT_WAREHOUSE = CBT_PREFIX+'warehouse'
    CBT_WAREHOUSE_STOCK = CBT_PREFIX+'warehouse_stock'
    CBT_WAREHOUSE_STOCK_TRANS = CBT_PREFIX+'warehouse_stock_trans'

    CBT_MODULE = CBT_PREFIX + 'module'
    CBT_SUB_MODULE = CBT_PREFIX + 'sub_module'
    CBT_MODULE_ACCESS = CBT_PREFIX + 'module_access'

    CBT_HEADER = CBT_PREFIX + 'header'
    CBT_BANNER = CBT_PREFIX + 'banner'
    CBT_ABOUT_US = CBT_PREFIX + 'about_us'
    CBT_CONTACT_US = CBT_PREFIX + 'contact_us'
    CBT_OUR_PRODUCT = CBT_PREFIX + 'our_product'
    CBT_OUR_SERVICES = CBT_PREFIX + 'our_services'
    CBT_OUR_ACHIEVEMENT = CBT_PREFIX + 'our_achievement'
    CBT_SOCIAL_LINK = CBT_PREFIX + 'social_link'
    CBT_ACTIVITY_TRACKING = CBT_PREFIX + 'activity_reporting'
    CBT_CLIENT_TYPE = CBT_PREFIX + 'client_type'
    CBT_ROUTE_TRANS = CBT_PREFIX + 'route_trans'
    CBT_WORK_TYPE = CBT_PREFIX + 'work_type'
    CBT_DWR_TYPE = CBT_PREFIX + 'dwr_type'
    CBT_DAY_PLAN = CBT_PREFIX + 'day_plan'
    CBT_VISIT = CBT_PREFIX + 'visit'
    CBT_VISIT_TRANS = CBT_PREFIX + 'visit_trans'

class CbtArrayName:
    SyncMainArray='SYNC_DATA'
    ControlArray='CONTROL'
    EmployeeArray='EMPLOYEE'
    MenuArray='MENU'
    DropDownArray='DROPDOWN'
    FileListArray='FILE_LIST'
    AssignMentArray='ASSIGNMENT_LIST'
    AttendanceArray='ATTENDANCE_LIST'
    VisitorArray='VISITOR'
    AttendanceArray='ATTENDANCE_REQ_LIST'
    LeaveReqArray='LEAVE_REQ_LIST'
    ExamArray='EXAM_LIST'
    RemarkArray='REMARKS_LIST'
    TrackingArray='TRACKING_LIST'
    BusArray='BUS_LIST'
    RouteArray='ROUTE_LIST'
    VisitorRouteArray='VISIT_ROUTE_LIST'
    VisitorCallArray='VISIT_CALL_LIST'
    WorkWithArray='WORK_WITH'
    Productarray='PRODUCT_LIST'
    CctvArray='CCTV'
    BannerArray='BANNER_LIST'
    CompanyArray='COMPANY_QR_LIST'
    CompanyArray='COUNTRY_LIST'
    StateArray='STATE_LIST'
    CityArray='CITY_LIST'
    ClientArray='client_list'
    Projectarray='PROJECT_LIST'
    ModuleArray='MODULE_LIST'
    ModuleAssignArray='MODULE_ASSIGN_LIST'
    TaskArray='TASK_LIST'
    ProjectTransArray='PROJECT_PAYMENT_TRANS'
    CheckInDetailsArray='USER_CHECKIN_DETAIL'
    Common = 'DATA'
    ErrorDetailArray = 'ERRORS'

class ApiStatus:
    Success='SUCCESS'
    Status="STATUS"
    Exception='EXCAPTION'
    Message='MESSAGE'
    Failure='FAILURE'
    Permission = 'PERMISSION'
    Exist = 'EXIST'
    Pending = 'PENDING'

class CbtMessage:
    Successfully = 'Check-In Successfully!!'
    DataNotFound = 'Data Not Found'
    LoginSuccessMsg = 'Logged in has been successfully!!'
    LoginFailedMsg = "Login credential doesn't exist!!"
    SendSuccessMsg = 'Message has been successfully send!!'
    PermissionMsg = 'You do not have permission!!'
    SubmitSuccessMsg = 'Data has been successfully submited!!'
    PurchaseSuccessMsg = 'Purchase successfully !!'
    UpdateSuccessMsg = 'Date has been successfully updated!!'
    DeleteSuccessMsg = 'Data has been successfully deleted!!'
    DataNotValid = "Data isn't valid!!"
    MessageFailed = "Message isn't send!!"
    MessageNotValid = "Data isn't valid!!"
    MessageException = 'Something went wrong!!'
    ExistMsg = 'already exist!!'
    UserDetailNotValid = "User details does't Valid!!"
    PendingDayplanMsg = "Please close pending day plan then create new one!!"

    def existMsg(message):
        return message+" "+CbtMessage.ExistMsg
    
    def cbtMsg(message):
        return message
    
    def CbtExceptionMsg(ex):
        return f"Something went wrong. Like - {ex}!!"
    
    def cbtImportMsg(count, total):
        return f"Data has been successfully Uploaded {count} in {total}.!!"
    
class ClickType:
    list = "LIST"
    form = "FORM"
    download = "DOWNLOAD"
    convert = "CONVERT"
    web = "WEB"

class BtnClickType:
    native = "NATIVE"
    web = "WEB"

class BtnType:
    add = "A"
    view = "V"
    edit = "E"
    delete = "D"

class CbtDepartmentName:
    cbt_it = 'IT'
    cbt_sales = 'SALES'
    
class CbtDesignationName:
    cbt_admin = 'ADMIN'
    cbt_manager = 'MANAGER'
    cbt_agent_tl = 'AGENT_TL'
    cbt_agent = 'AGENT'
    cbt_verification_tl = 'VERIFICATION_TL'
    cbt_verification_agent = 'VERIFICATION_AGENT'

class CbtLeadStatus:
    CBT_FRESH = 0
    CBT_ACTIVE = True
    CBT_ASSIGN_TO_MANAGER = 1
    CBT_ASSIGN_TO_AGENT_TL = 2
    CBT_ASSIGNED = 55
    CBT_RE_ASSIGNED = 56
    CBT_APPROVED = 57
    CBT_VERIFIED = 58
    CBT_UN_VERIFIED = 59
    CBT_DELIVERED = 60
    CBT_RTO = 61
    CBT_HOLD = 62
    CBT_CANCELED = 63
    CBT_RINGING = 64
    CBT_WRONG_NO = 65
    CBT_CALLBACK = 66
    CBT_SWITCH_OFF = 67
    CBT_NOT_INTRESTED = 68
    CBT_NOT_CONNECTED = 69

    
class CbtRptCode:
    RPT_ATTENDANCE_REPORT = 'RPT_ATTENDANCE_REPORT'
    RPT_LEAVE_REPORT = 'RPT_LEAVE_REPORT'
    RPT_DWR_REPORT = 'RPT_DWR_REPORT'
    PRT_USER_ACTIVITY_REPORT = 'PRT_USER_ACTIVITY_REPORT'
    PRT_HOTEL_BOOKING_REPORT = 'CBT_HOTEL_BOOKING_REPORT'
    PRT_FLIGHT_BOOKING_REPORT = 'CBT_FLIGHT_BOOKING_REPORT'


class CbtCol:
    srNo = "S.No"
    name = "Name"
    sender = "Sender"
    phone = "Phone"
    code = "Code"
    adrress = "Address"
    description = "Description"
    menu = "Menu"
    submenu = "Sub Menu"
    product = "Product"
    category = "Category"
    brand = "Brand"
    image = "Image"
    status = "Status"
    managerRemark = "Manager Remark"
    department = "Department"
    value = "Value"
    state = "State"
    area = "Area"
    date = "Date"
    in_time = "In Time"
    out_time = "Out Time"
    in_image = "In Image"
    out_image = "Out Image"
    in_location = "In Location"
    out_localtion = "Out Location"
    in_qr_img = "In Qr Img"
    out_qr_img = "Out Qr Img"
    start_date = "Start Date"
    end_date = "End Date"
    deviceType = "Device Type"
    serialNo = "Serial No"
    mrpPrice = "MRP Price"
    sellingPrice = "Sell Price"
    manager = "Manager Name"
    doj = "DOJ"
    dob = "DOB"
    due_type = "Due Type"
    headQtr = "Head Qtr"
    mobile = "Mobile"
    designation = "Designation"
    type = "Type"
    subject = "Subject"
    message = "Message"
    end_time = "End Time"
    start_time = "Start Time"
    user_name = "User Name"
    leadId = "Lead Id"
    source = "Source"
    location = "Location"
    ip_address = "IP Address"
    latlong = "Latlong"
    battery = "Battery"
    os = "OS",
    phone_brand = 'Phone Brand',
    km = 'KM'
    activity_type = 'Activity Type'
    day = 'Day'
    holiday = 'Holiday'
    heading = 'Heading'
    title = 'Title'
    imagePath = 'Image Path'
    createdAt = 'Created At'
    modifiedAt = 'Modified At'
    modifiedBy = 'Modified By'
    backgroundColor = 'Background Color'
    position = 'Position'
    bannerType = 'Banner Type'
    moduleType = 'Module Type'
    altTag = 'Alt Tag'
    url = 'Url'
    whatsAppNo = 'Whatsapp No'
    email = 'Email'
    email2 = 'Email2'
    workingType = 'Work Type'
    workingDate = 'Working Date'
    planDate = 'Plan Date'
    planTime = 'Plan Time'
    submitDate = 'Submit Date'
    remarks = 'Remarks'
    dwrStatus = 'DWR Status'
    productName = 'Product'
    quantity = 'Quantity'
    entryDate = 'Entry Date'
    entryDateTime = 'Entry Date/Time'
    exitDateTime = 'Exist Date/Time'
    attStatus = 'Attendance Status'
    assetName = 'Asset Name'
    assignTo = 'Assign To'
    assignDate = 'Assign Date'
    prurchasePrice = 'Prurchase Price'
    routeName = 'Route Name'
    hotelName = 'Hotel Name'
    hotelCode = 'Hotel Code'
    noOfRoom = 'No. Of Room'
    bookingId = 'Booking Id'
    totalAmount = 'Total Amount'
    agent = 'Agent'
    pnrNo = 'PNR NO.'


def cbtStatusTxt(value):
    if value == 1:
        return 'Active'
    elif value == 0:
        return 'Inactive'
    else:
        return 'Inactive'
    



class CBTFlex:
    low = 1
    medium = 2
    normal = 3
    high = 4
    over = 5