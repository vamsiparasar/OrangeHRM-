class website():
    url = "https://opensource-demo.orangehrmlive.com/index.php/auth/login"

class Configlogin():
    username="Admin"
    pwd="admin123"

class loginlocator():
    userfield ="//input[@id='txtUsername']"
    passwordfield ="//input[@id='txtPassword']"
    loginbutton ="//input[@id='btnLogin']"
    welcomebutton="//a[@id='welcome']"
    logoutbutton ="//a[contains(text(),'Logout')]"

class AdminTabslocater():
    Adminbutton="//b[contains(text(),'Admin')]"
    Usermanagementbutton="//a[@id='menu_admin_UserManagement']"
    UserButton ="//a[@id='menu_admin_viewSystemUsers']"
    UserAddButton ="//input[@id='btnAdd']"
    JobButton ="//a[@id='menu_admin_Job']"
    JobTitleButton = "//a[@id='menu_admin_viewJobTitleList']"
    PayGrades = "//a[@id='menu_admin_viewPayGrades']"
    EmploymentStatus = "//a[@id='menu_admin_employmentStatus']"
    JobCategory = "//a[@id='menu_admin_jobCategory']"
    WorkShift = "//a[@id='menu_admin_workShift']"
    Organization = "//a[@id='menu_admin_Organization']"
    GeneralInformation = "//a[@id='menu_admin_viewOrganizationGeneralInformation']"
    ViewLocations = "//a[@id='menu_admin_viewLocations']"
    CompanyStructure = "//a[@id='menu_admin_viewCompanyStructure']"
    Qualifications = "//a[@id='menu_admin_Qualifications']"
    ViewSkills = "//a[@id='menu_admin_viewSkills']"
    ViewEducation = "//a[@id='menu_admin_viewEducation']"
    Licenses = "//a[@id='menu_admin_viewLicenses']"
    Languages = "//a[@id='menu_admin_viewLanguages']"
    Membership = "//a[@id='menu_admin_membership']"
    Nationality = "//a[@id='menu_admin_nationality']"
    Configuration = "//a[@id='menu_admin_Configuration']"
    MailConfiguration = "//a[@id='menu_admin_listMailConfiguration']"
    EmailSubscriptions = "//a[@id='menu_admin_viewEmailNotification']"
    Localization = "//a[@id='menu_admin_localization']"
    ViewModules = "//a[@id='menu_admin_viewModules']"
    SocialMediaAuthentication = "//a[@id='menu_admin_openIdProvider']"
    RegisterOAuthClient = "//a[@id='menu_admin_registerOAuthClient']"
    Directory = "//b[contains(text(),'Directory')]"

class RecruitmentTabslocater():
    Recruitment = "//b[contains(text(),'Recruitment')]"
    Candidates = "//a[@id='menu_recruitment_viewCandidates']"
    Vacancy = "//a[@id='menu_recruitment_viewJobVacancy']"

class LeaveTabslocater():
    LeaveButton = "//b[contains(text(),'Leave')]"
    ApplyLeave = "//a[@id='menu_leave_applyLeave']"
    MyLeave =  "//a[@id='menu_leave_viewMyLeaveList']"
    Entitlements = "//a[@id='menu_leave_Entitlements']"
    AddEntitlement = "//a[@id='menu_leave_addLeaveEntitlement']"
    EmployeeEntitlements ="//a[@id='menu_leave_viewLeaveEntitlements']"
    MyEntitlements = "//a[@id='menu_leave_viewMyLeaveEntitlements']"
    LeaveList = "//a[@id='menu_leave_viewLeaveList']"
    AssignLeave = "//a[@id='menu_leave_assignLeave']"
    Reports = "//a[@id='menu_leave_Reports']"
    ViewLeaveBalanceReport = "//a[@id='menu_leave_viewLeaveBalanceReport']"
    MyLeaveEntitlementsandUsageReport ="/html[1]/body[1]/div[1]/div[2]/ul[1]/li[3]/ul[1]/li[4]/ul[1]/li[2]/a[1]"
    Configure = "//a[@id='menu_leave_Configure']"
    LeavePeriod = "//a[@id='menu_leave_defineLeavePeriod']"
    LeaveType ="//a[@id='menu_leave_leaveTypeList']"
    WorkingWeek = "//a[@id='menu_leave_defineWorkWeek']"
    HolidayList = "//a[@id='menu_leave_viewHolidayList']"

class TimeTabslocater():
    TimeButton = "//b[contains(text(),'Time')]"
    Timesheets = "//a[@id='menu_time_Timesheets']"
    MyTimesheet = "//a[@id='menu_time_viewMyTimesheet']"
    EmployeeTimesheet = "//a[@id='menu_time_viewEmployeeTimesheet']"
    Attendance = "//a[@id='menu_attendance_Attendance']"
    MyAttendance = "//a[@id='menu_attendance_viewMyAttendanceRecord']"
    PunchIn = "//a[@id='menu_attendance_punchIn']"
    ViewAttendanceRecord = "//a[@id='menu_attendance_viewAttendanceRecord']"
    AttendanceConfigure = "//a[@id='menu_attendance_configure']"
    Reports = "//a[@id='menu_time_Reports']"
    ProjectReport = "//a[@id='menu_time_displayProjectReportCriteria']"
    EmployeeReport = "//a[@id='menu_time_displayEmployeeReportCriteria']"
    SummaryReport = "//a[@id='menu_time_displayAttendanceSummaryReportCriteria']"
    ProjectInfo = "//a[@id='menu_admin_ProjectInfo']"
    Customers = "//a[@id='menu_admin_viewCustomers']"
    Projects = "//a[@id='menu_admin_viewProjects']"

class PerformanceTabLocater():
    Performance = "//b[contains(text(),'Performance')]"
    Configure = "//a[@id='menu_performance_Configure']"
    SearchKpi = "//a[@id='menu_performance_searchKpi']"
    Tracker = "//a[@id='menu_performance_addPerformanceTracker']"
    ManageReviews ="//a[@id='menu_performance_ManageReviews']"
    Review = "//a[@id='menu_performance_searchPerformancReview']"
    MyReviews = "/html[1]/body[1]/div[1]/div[2]/ul[1]/li[7]/ul[1]/li[2]/ul[1]/li[2]/a[1]"
    ReviewList = "//a[@id='menu_performance_searchEvaluatePerformancReview']"
    MyTracker = "//a[@id='menu_performance_viewMyPerformanceTrackerList']"
    EmployeeTracker = "//a[@id='menu_performance_viewEmployeePerformanceTrackerList']"

class PIMButtoneTabLocater():
    PIMButton = "//b[contains(text(),'PIM')]"
    Configuration = "//a[@id='menu_pim_Configuration']"
    ConfigurePim = "//a[@id='menu_pim_configurePim']"
    CustomFields = "//a[@id='menu_pim_listCustomFields']"
    CsvImport = "//a[@id='menu_admin_pimCsvImport']"
    ReportingMethods = "//a[@id='menu_pim_viewReportingMethods']"
    TerminationReasons = "//a[@id='menu_pim_viewTerminationReasons']"
    EmployeeList = "//a[@id='menu_pim_viewEmployeeList']"
    AddEmployee = "//a[@id='menu_pim_addEmployee']"
    Reports = "//a[@id='menu_core_viewDefinedPredefinedReports']"










