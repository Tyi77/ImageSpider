# 失敗的方法，但以後可以深究
import mechanize        

def gmaillogin():
    browser = mechanize.Browser(factory=mechanize.RobustFactory())
    browser.set_handle_robots(False)
    r = browser.open("https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=http://mail.google.com/mail/&scc=1&ltmpl=default&ltmplcache=2&emr=1") 
    browser.select_form(nr=0)               
    browser.form["Email"] = "emailid"
    browser.form["Passwd"] = "password"    
    browser.submit()                        

    html = browser.response().readlines()    
    
    print(html)  

if __name__ == "__main__":
    gmaillogin()