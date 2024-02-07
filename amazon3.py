import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import requests

'''
api_url = "https://vak-sms.com/api/getNumber/"
api_key = "648ade1e8155477b913c82eeb381ec52"
service = "am"
country = "gb"
operator = "ee"

# Construct the API endpoint URL
url = f"{api_url}?apiKey={api_key}&service={service}&country={country}&operator={operator}"
# Send the HTTP GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()
    print("my phone number:", data)
else:
    print("Failed to retrieve phone number.")
'''

def read_credentials_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        email = lines[0].strip()
        password = lines[1].strip()
    return email, password

def write_credentials_to_file(file_path, email, password, phone_number):
    with open(file_path, 'a') as file:
        file.write(f"{email},{password},{phone_number}\n")


# Specify the path to your text file containing email and password
credentials_file_path = "accounts.txt"
# Read credentials from the file
email, password = read_credentials_from_file(credentials_file_path)
# Open a new file to store results
results_file_path = "results.txt"



api_url = "https://smshub.org/stubs/handler_api.php"
api_key = "196958U41711d3251320bc304a900805d7e9a28"  # Replace with your actual API key

params = {
    "api_key": api_key,
    "action": "getNumber",
    "service": "am",
    "operator": "movistar",
    "country": "33",
    "maxPrice": "10"
}

response = requests.get(api_url, params=params)

access_number_str = f"{response.content.decode('utf-8')}"
# Split the string using ":" as the delimiter
parts = access_number_str.split(":")

# Extract the required numbers
ID_NUM = parts[1]
Phone_number = parts[2]

print(f"ID_NUM: {ID_NUM}")
print(f"Phone number: {Phone_number}")


# Initialize WebDriver
# driver = webdriver.Chrome()  # Replace with your preferred browser driver

# Navigate to the website
# driver.get("https://www.amazon.eg/ap/signin?openid.pape.max_auth_age=3600&openid.return_to=https%3A%2F%2Fgaming.amazon.eg%2Fprime%2Fusamazonlogin%2Feg%3Fconfirm%3DALWAYS%26returnUri%3Dhttps%253A%252F%252Famazon.com%252Fap%252Fsignin%253Fopenid.pape.max_auth_age%253D3600%2526openid.return_to%253Dhttps%25253A%25252F%25252Fgaming.amazon.com%25252Fhome%25253FsignedIn%25253Dtrue%2526openid.identity%253Dhttp%25253A%25252F%25252Fspecs.openid.net%25252Fauth%25252F2.0%25252Fidentifier_select%2526openid.assoc_handle%253Damzn_respawn_desktop_us%2526openid.mode%253Dcheckid_setup%2526openid.claimed_id%253Dhttp%25253A%25252F%25252Fspecs.openid.net%25252Fauth%25252F2.0%25252Fidentifier_select%2526openid.ns%253Dhttp%25253A%25252F%25252Fspecs.openid.net%25252Fauth%25252F2.0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_respawn_desktop_eg&openid.mode=checkid_setup&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=amzn_gaming_prime&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&ssoResponse=eyJ6aXAiOiJERUYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiQTI1NktXIn0.g_wexKo5JfrtATC71uUZt1ONym53Xt2bjiMdFlaYc5_kxwLIFCS3lw.v1GGnu36V8mfg1Mj.fkH8H7Oz6cn6F7WSzzTBrSaQlmj4gvINJJsGPxjpi-Iwps2-9OJm014vhQjyYXdtHofnCi23uSI0KZXPlKpctpvUWgS-eTv1EW-wnUFxa2rlLfDVJoRq2jUHQzRC3GDckLsQft-YsTTYo_VuHINXgMWvXgTnk4reAnpCGJ1POmE4-WcwgydAdLOiPpww91o8v-1xkz2eOQ.Wwbpy1dfgq3cueai73-hqw")
# driver.get("https://www.amazon.co.uk/ap/signin?openid.pape.max_auth_age=3600&openid.return_to=https%3A%2F%2Fgaming.amazon.co.uk%2Fprime%2Fusamazonlogin%2Fuk%3Fconfirm%3DALWAYS%26returnUri%3Dhttps%253A%252F%252Famazon.com%252Fap%252Fsignin%253Fopenid.pape.max_auth_age%253D3600%2526openid.return_to%253Dhttps%25253A%25252F%25252Fgaming.amazon.com%25252Fprime%25252Fsignup%25252Fuk%25253Fingress%25253Damzn%252526ref_%25253Dsm_w_ics_m_f_all%2526openid.identity%253Dhttp%25253A%25252F%25252Fspecs.openid.net%25252Fauth%25252F2.0%25252Fidentifier_select%2526openid.assoc_handle%253Damzn_respawn_desktop_us%2526openid.mode%253Dcheckid_setup%2526openid.claimed_id%253Dhttp%25253A%25252F%25252Fspecs.openid.net%25252Fauth%25252F2.0%25252Fidentifier_select%2526openid.ns%253Dhttp%25253A%25252F%25252Fspecs.openid.net%25252Fauth%25252F2.0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_respawn_desktop_uk&openid.mode=checkid_setup&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=amzn_gaming_prime&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&ssoResponse=eyJ6aXAiOiJERUYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiQTI1NktXIn0.dHNotry1npY7N7zg-I_9bth18zfejWwVBFvH0dIAJsqN4uY_4SNwdA.vAkuG-f7sFx9phtE.qa50uZMGzWByRNGC8M2Pt-wC207IOqZd2gVyXvUWvU_A1oAKyHAw69Df231f503lVn7P_KIMqaL81DG1A59ufAHaah6uoLS0bZQkWxzl3Z6M3MrVallaxNDDww9NwE7TJtxdoU1oNhbr9LSRAf85bxz5LjHm2imbJv5fURcEDBH5gsBHzMBTwq2dq0aZNB97Bv8JZy9EGRRt.TO_FRA28WPHXqO8eL75B1Q")
# driver.get("https://www.amazon.eg/ap/signin?openid.pape.max_auth_age=3600&openid.return_to=https%3A%2F%2Fgaming.amazon.eg%2Fprime%2Fusamazonlogin%2Feg%3Fconfirm%3DALWAYS%26returnUri%3Dhttps%3A%2F%2Famazon.com%2Fap%2Fsignin%3Fopenid.pape.max_auth_age%3D3600%26openid.return_to%3Dhttps%3A%2F%2Fgaming.amazon.com%2Foauth%2Fstart%2Friot%3Foverwrite%3Dtrue%26redirectUrl%3Dhttps%253A%252F%252Fgaming.amazon.com%252Floot%252Flol10%26signedIn%3Dtrue%26openid.identity%3Dhttp%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select%26openid.assoc_handle%3Damzn_respawn_desktop_us%26openid.mode%3Dcheckid_setup%26openid.claimed_id%3Dhttp%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select%26openid.ns%3Dhttp%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_respawn_desktop_eg&openid.mode=checkid_setup&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=amzn_gaming_prime&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&ssoResponse=eyJ6aXAiOiJERUYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiQTI1NktXIn0.gGPpBeTsDb2Cr1j4a1pEJ2BvRAj0knOhC6lZrUGKUtZFdnhD42MVLg.yUupIsLlVWZuEn7P.730Ilyu2WkbnMPQkzd0hVKrRZMG0US8kaoN_A2N5Tf4ObN5WxWUOo1n7RsGZo7L6M9fyLfLVM5MHBZeBmYoiucg_A0zaGgw6Pk6ynl78MCXY36yi__XWgx7CYEMwm88w9_R8ub0DLq1zl0Wiv5HXjCAJt0rZLxNcEf2f_CPqT7n6dDLOG6gshbHFRoUVBv7RZdUmkfkp6Q.zBfiSb8wcEmYyvBloFXkaw")

driver = webdriver.Chrome()
driver.get("https://gaming.amazon.com/home")



 #Inside the loop where you read credentials from the file:
with open(credentials_file_path, 'r') as file:
    for line in file:
        # Extract email and password from each line
        email, password = line.strip().split(',')

        try:
            # Click "Try Prime" button
            try_prime_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[1]/div/div/nav/div/div/div/div/div[2]/div/div[2]")))
            try_prime_button.click()

            # Click "Choose Country" button
            choose_country_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div[6]")))
            choose_country_button.click()

            # Select "United Kingdom"
            uk_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//option[text()='United Kingdom']")))
            uk_option.click()

            # Click "Continue" button
            continue_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div[6]")))
            continue_button.click()
            username_field = driver.find_element(By.ID, "ap_email")
            password_field = driver.find_element(By.ID, "ap_password")
            sign_in_button = driver.find_element(By.ID, "signInSubmit")  # Adjust selector if needed

            # Enter credentials dynamically
            username_field.send_keys(email)
            password_field.send_keys(password)

            # Click the sign-in button
            sign_in_button.click()
            time.sleep(10)
            driver.execute_script("window.open('https://www.amazon.co.uk/ap/profile/mobilephone?ref_=ax_am_landing_add_mobile&openid.assoc_handle=gbflex&referringAppAction=CNEP');")  # Opens a blank new tab

            # Switch to the newly opened tab
            driver.switch_to.window(driver.window_handles[-1])

            click_select_country = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/form/div[2]/div/div[1]")))
            click_select_country.click()

            click_select_colombia = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/ul/li[43]")))
            click_select_colombia.click()

            # Wait for the phone field to be clickable
            phone_field = WebDriverWait(driver, 200).until(EC.element_to_be_clickable((By.ID, "ap_phone_number")))
            phone_field.send_keys(Phone_number)  # Use the actual phone number obtained from the API

            continue_button_phone = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/form/div[5]/span")))
            continue_button_phone.click()
            # Click "Choose Country" button

            click_ok = WebDriverWait(driver, 200).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div/div[2]/div[4]/div[2]/span/span/span")))
            click_ok.click()

            """
            get_sms_api = "https://vak-sms.com/api/getSmsCode/"
            # Construct the API endpoint URL
            sms = f"{get_sms_api}?apiKey={api_key}&idNum={ID_NUM}&all="
            # Send the HTTP GET request
            response_sms = requests.get(sms)

            if response_sms.status_code == 200:
                sms_Code = response_sms.json()
                print("code is :", sms_Code)
            else:
                print("Failed to retrieve phone number.")

            smsCode = sms_Code["smsCode"]
            print("code is :", smsCode[0])
            """

            time.sleep(75)
            params = {
                "api_key": api_key,
                "action": "getStatus",
                "id": ID_NUM
            }

            response_sms = requests.get(api_url, params=params)
            access_sms_code = f"{response_sms.content.decode('utf-8')}"
            # Split the string using ":" as the delimiter
            parts = access_sms_code.split(":")
            sms_status = parts[0]
            print(f"sms status: {sms_status}")
            # Extract the numeric part
            sms_Code = parts[1]
            print(f"sms code: {sms_Code}")

            get_sms_code = WebDriverWait(driver, 200).until(EC.element_to_be_clickable((By.ID, "auth-pv-enter-code")))
            get_sms_code.send_keys(sms_Code)
            click_verify = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "auth-verify-button")))
            click_verify.click()
            password_field_addnumber = driver.find_element(By.ID, "ap_password")
            password_field_addnumber.send_keys(password)
            click_verify = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "auth-cnep-change-email-submit")))
            click_verify.click()
            # Check for CAPTCHA
            while True:
                try:
                    captcha_element = driver.find_element(By.CLASS_NAME,
                                                          "captcha-container")  # Adjust selector if needed
                    # Pause for user to solve CAPTCHA
                    print("CAPTCHA detected! Please solve it manually and press Enter to continue.")
                    input()
                except NoSuchElementException:
                    print("CAPTCHA not found. Continuing...")
                    break
                except TimeoutException:
                    print("Timed out waiting for CAPTCHA. Please check if it's loading correctly.")
                    break



            write_credentials_to_file(results_file_path, email, password, Phone_number)








        except NoSuchElementException:
            time.sleep(100)
            print("Error: Unable to locate login elements. Please verify their IDs/classes.")


        finally:
            # Close the browser
            time.sleep(50)
            driver.quit()
"""



# Locate login elements
try:
    # Click "Try Prime" button
    try_prime_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/nav/div/div/div/div/div[2]/div/div[2]")))
    try_prime_button.click()

    # Click "Choose Country" button
    choose_country_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div[6]")))
    choose_country_button.click()

    # Select "United Kingdom"
    uk_option = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//option[text()='United Kingdom']")))
    uk_option.click()

    # Click "Continue" button
    continue_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div[6]")))
    continue_button.click()
    username_field = driver.find_element(By.ID, "ap_email")
    password_field = driver.find_element(By.ID, "ap_password")
    sign_in_button = driver.find_element(By.ID, "signInSubmit")  # Adjust selector if needed

    # Enter credentials
    username_field.send_keys("Yomnnaali64@hotmail.com")
    password_field.send_keys("123456")
    # Click the sign-in button
    sign_in_button.click()
    time.sleep(7)

    driver.execute_script("window.open('https://www.amazon.co.uk/ap/profile/mobilephone?ref_=ax_am_landing_add_mobile&openid.assoc_handle=gbflex&referringAppAction=CNEP');")  # Opens a blank new tab

    # Switch to the newly opened tab
    driver.switch_to.window(driver.window_handles[-1])

    click_select_country = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/form/div[2]/div/div[1]")))
    click_select_country.click()

    click_select_colombia = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/ul/li[43]")))
    click_select_colombia.click()





    # Wait for the phone field to be clickable
    phone_field = WebDriverWait(driver, 200).until(EC.element_to_be_clickable((By.ID, "ap_phone_number")))
    phone_field.send_keys(Phone_number)  # Use the actual phone number obtained from the API

    continue_button_phone = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/form/div[5]/span")))
    continue_button_phone.click()
    # Click "Choose Country" button

    click_ok = WebDriverWait(driver, 200).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div/div[2]/div[4]/div[2]/span/span/span")))
    click_ok.click()

"""
"""
    get_sms_api = "https://vak-sms.com/api/getSmsCode/"
    # Construct the API endpoint URL
    sms = f"{get_sms_api}?apiKey={api_key}&idNum={ID_NUM}&all="
    # Send the HTTP GET request
    response_sms = requests.get(sms)

    if response_sms.status_code == 200:
        sms_Code = response_sms.json()
        print("code is :", sms_Code)
    else:
        print("Failed to retrieve phone number.")

    smsCode = sms_Code["smsCode"]
    print("code is :", smsCode[0])
"""
"""

    time.sleep(50)
    params = {
        "api_key": api_key,
        "action": "getStatus",
        "id": ID_NUM
    }

    response_sms = requests.get(api_url, params=params)
    access_sms_code = f"{response_sms.content.decode('utf-8')}"
    # Split the string using ":" as the delimiter
    parts = access_sms_code.split(":")
    sms_status = parts[0]
    print(f"sms status: {sms_status}")
    # Extract the numeric part
    sms_Code = parts[1]
    print(f"sms code: {sms_Code}")

    sms_code = WebDriverWait(driver, 200).until(EC.element_to_be_clickable((By.ID, "auth-pv-enter-code")))
    sms_code.send_keys(sms_code)
    click_verify = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "auth-verify-button")))
    click_verify.click()
    password_field_addnumber = driver.find_element(By.ID, "ap_password")
    password_field_addnumber.send_keys("123456")
    click_verify = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID, "auth-cnep-change-email-submit")))
    click_verify.click()
    time.sleep(1000)

    # Check for CAPTCHA
    while True:
        try:
            captcha_element = driver.find_element(By.CLASS_NAME, "captcha-container")  # Adjust selector if needed
            # Pause for user to solve CAPTCHA
            print("CAPTCHA detected! Please solve it manually and press Enter to continue.")
            input()
        except NoSuchElementException:
            print("CAPTCHA not found. Continuing...")
            break
        except TimeoutException:
            print("Timed out waiting for CAPTCHA. Please check if it's loading correctly.")
            break

    # Proceed with actions after login (if CAPTCHA was solved)
    # ...

    time.sleep(1000)
except NoSuchElementException:
    time.sleep(100)
    print("Error: Unable to locate login elements. Please verify their IDs/classes.")"""


