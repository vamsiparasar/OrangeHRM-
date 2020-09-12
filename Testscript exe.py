import OrangeHrmTestScript
import time
if __name__ == '__main__':
    OrangeHrmTestScript.login()
    OrangeHrmTestScript.admin_user_management()
    OrangeHrmTestScript.admin_job()
    OrangeHrmTestScript.admin_Organization()
    OrangeHrmTestScript.admin_Qualifications()
    OrangeHrmTestScript.admin_Nationality()
    OrangeHrmTestScript.admin_Configuration()
    OrangeHrmTestScript.Directory()
    OrangeHrmTestScript.Recruitment()
    OrangeHrmTestScript.admin_Leave()
    OrangeHrmTestScript.admin_time()
    OrangeHrmTestScript.admin_Performance()
    OrangeHrmTestScript.admin_PIM()
    OrangeHrmTestScript.logout()
    time.sleep(2)
    OrangeHrmTestScript.driver.close()

