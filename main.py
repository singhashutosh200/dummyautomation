from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://accounts.google.com/signin/v2/identifier?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin#inbox")
print(driver.title)
driver.find_element(By.CLASS_NAME, 'AxOyFc snByac').send_keys(ashumailtou)
driver.find_element(By.CLASS_NAME, 'VfPpkd-vQzf8d').click()