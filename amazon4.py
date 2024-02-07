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



"""api_url = "https://smshub.org/stubs/handler_api.php"
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
print(f"Phone number: {Phone_number}")"""

# Initialize an empty list to store emails
email_list = []
password_list = []

# Read credentials from the file
with open(credentials_file_path, 'r') as file:
    for line in file:
        # Extract email and password from each line
        email, password = line.strip().split(',')
        email_list.append(email)
        password_list.append(password)

    # Loop through each email and password
    for i in range(len(email_list)):
        email = email_list[i]
        password = password_list[i]

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
        # Initialize an empty list to store emails
        # Initialize an empty list to store emails
        email_list = []
        password_list = []


        driver = webdriver.Chrome()
        driver.get("https://gaming.amazon.com/home")
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
            continue_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div[6]")))
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
            driver.execute_script(
                "window.open('https://www.amazon.co.uk/ap/profile/mobilephone?ref_=ax_am_landing_add_mobile&openid.assoc_handle=gbflex&referringAppAction=CNEP');")  # Opens a blank new tab

            # Switch to the newly opened tab
            driver.switch_to.window(driver.window_handles[-1])

            click_select_country = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/form/div[2]/div/div[1]")))
            click_select_country.click()

            click_select_colombia = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/ul/li[43]")))
            click_select_colombia.click()

            # Wait for the phone field to be clickable
            phone_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "ap_phone_number")))
            phone_field.send_keys(Phone_number)

            continue_button_phone = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/form/div[5]/span")))
            continue_button_phone.click()
            # Click "Choose Country" button

            click_ok = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div/div[2]/div[4]/div[2]/span/span/span")))
            click_ok.click()

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
            click_verify = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "auth-cnep-change-email-submit")))
            click_verify.click()

            # Check for CAPTCHA
            while True:
                try:
                    captcha_element = driver.find_element(By.CLASS_NAME,"captcha-container")  # Adjust selector if needed
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
            time.sleep(10)
            print("Error: Unable to locate login elements. Please verify their IDs/classes.")

        finally:
            # Close the browser
            time.sleep(10)
            driver.quit()