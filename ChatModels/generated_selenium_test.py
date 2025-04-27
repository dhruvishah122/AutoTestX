import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def run_tests():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.booking.com/")
    driver.maximize_window()

    test_cases = [
        {
            "description": "Verify the 'Stays' navigation link is present and clickable.",
            "type": "navigation",
            "action": "click",
            "xpath": "/html/body/div[2]/div/div/header/div/nav[2]/div/ul/li[1]/a/span/div",
            "value": None,
            "expected": "Navigates to the stays page."
        },
        {
            "description": "Verify the 'Flights' navigation link is present and clickable.",
            "type": "navigation",
            "action": "click",
            "xpath": "/html/body/div[2]/div/div/header/div/nav[2]/div/ul/li[2]/a/span/div",
            "value": None,
            "expected": "Navigates to the flights page."
        },
        {
            "description": "Verify the 'Car rentals' navigation link is present and clickable.",
            "type": "navigation",
            "action": "click",
            "xpath": "/html/body/div[2]/div/div/header/div/nav[2]/div/ul/li[4]/a/span/div",
            "value": None,
            "expected": "Navigates to the car rentals page."
        },
        {
            "description": "Verify the 'Attractions' navigation link is present and clickable.",
            "type": "navigation",
            "action": "click",
            "xpath": "/html/body/div[2]/div/div/header/div/nav[2]/div/ul/li[6]/a/span/div",
            "value": None,
            "expected": "Navigates to the attractions page."
        },
        {
            "description": "Verify the 'Sign in' link is present and clickable.",
            "type": "navigation",
            "action": "click",
            "xpath": "/html/body/div[2]/div/div/header/div/nav[1]/div[2]/div",
            "value": None,
            "expected": "Opens the sign-in form."
        },
        {
            "description": "Verify the 'Register' link is present and clickable.",
            "type": "navigation",
            "action": "click",
            "xpath": "/html/body/div[2]/div/div/header/div/nav[1]/div[2]/a[2]/span",
            "value": None,
            "expected": "Opens the registration form."
        },
        {
            "description": "Attempt to register with a valid email and password.",
            "type": "input_field",
            "action": "send_keys",
            "xpath": "/html/body/div[1]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div/div/div/form/div[2]/div[1]/input",
            "value": "dhruvishah116122@gmail.com",
            "expected": "Registration is successful."
        },
        {
            "description": "Attempt to register with a valid email and password.",
            "type": "input_field",
            "action": "send_keys",
            "xpath": "/html/body/div[1]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div/div/div/form/div[2]/div[2]/input",
            "value": "Dbms#amazon122",
            "expected": "Registration is successful."
        },
        {
            "description": "Attempt to log in with a registered email and password.",
            "type": "input_field",
            "action": "send_keys",
            "xpath": "/html/body/div[1]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div/div/div/form/div[2]/div[1]/input",
            "value": "dhruvishah116122@gmail.com",
            "expected": "Login is successful."
        },
        {
            "description": "Attempt to log in with a registered email and password.",
            "type": "input_field",
            "action": "send_keys",
            "xpath": "/html/body/div[1]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div/div/div/form/div[2]/div[2]/input",
            "value": "Dbms#amazon122",
            "expected": "Login is successful."
        },
        {
            "description": "Search for hotels in New York.",
            "type": "input_field",
            "action": "send_keys",
            "xpath": "/html/body/div[3]/div[2]/div/form/div[1]/div[1]/div/div/div[1]/div/div/input",
            "value": "New York",
            "expected": "Search results for New York hotels are displayed."
        },
        {
            "description": "Select check-in date.",
            "type": "button",
            "action": "click",
            "xpath": "/html/body/div[3]/div[2]/div/form/div[1]/div[2]/div/div[1]/button/span",
            "value": None,
            "expected": "Calendar opens to select check-in date."
        },
        {
            "description": "Select check-out date.",
            "type": "button",
            "action": "click",
            "xpath": "/html/body/div[3]/div[2]/div/form/div[1]/div[3]/div/div[1]/button/span",
            "value": None,
            "expected": "Calendar opens to select check-out date."
        },
        {
            "description": "Click the search button after selecting dates and location.",
            "type": "button",
            "action": "click",
            "xpath": "/html/body/div[3]/div[2]/div/form/div[1]/div[4]/button/span",
            "value": None,
            "expected": "Search results are displayed based on the criteria."
        },
        {
            "description": "Verify the 'USD' currency selector is present.",
            "type": "button",
            "action": "click",
            "xpath": "/html/body/div[2]/div/div/header/div/nav[1]/div[2]/div[1]/button/span",
            "value": None,
            "expected": "Currency options are displayed."
        },
        {
            "description": "Verify the 'Customer support' link is present and clickable.",
            "type": "navigation",
            "action": "click",
            "xpath": "/html/body/div[2]/div/div/header/div/nav[1]/div[2]/a[1]",
            "value": None,
            "expected": "Navigates to the customer support page."
        },
        {
            "description": "Verify the 'List your property' link is present and clickable.",
            "type": "navigation",
            "action": "click",
            "xpath": "/html/body/div[2]/div/div/header/div/nav[1]/div[2]/a[2]/span",
            "value": None,
            "expected": "Navigates to the property listing page."
        },
        {
            "description": "Verify the 'Airport taxis' navigation link is present and clickable.",
            "type": "navigation",
            "action": "click",
            "xpath": "/html/body/div[2]/div/div/header/div/nav[2]/div/ul/li[7]/a/span/div",
            "value": None,
            "expected": "Navigates to the airport taxis page."
        },
        {
            "description": "Verify the 'Language: English (US)' link is present and clickable.",
            "type": "button",
            "action": "click",
            "xpath": "/html/body/div[6]/div[2]/div[2]/footer/div[3]/div/div[1]/span[1]/button",
            "value": None,
            "expected": "Language options are displayed."
        },
        {
            "description": "Verify the '2 adults · 0 children · 1 room' link is present and clickable.",
            "type": "button",
            "action": "click",
            "xpath": "/html/body/div[3]/div[2]/div/form/div[1]/div[3]/div/div",
            "value": None,
            "expected": "Opens the guest and room selection options."
        }
    ]

    results = []

    for test_case in test_cases:
        description = test_case["description"]
        xpath = test_case["xpath"]
        action = test_case["action"]
        value = test_case["value"]
        expected = test_case["expected"]

        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )

            if action == "click":
                element.click()
            elif action == "send_keys":
                element.send_keys(value)

            print(f"✅ {description}: Passed")
            results.append({"description": description, "result": "Passed"})

        except (NoSuchElementException, TimeoutException) as e:
            print(f"❌ {description}: Failed")
            results.append({"description": description, "result": "Failed"})
            driver.get("https://www.booking.com/")

        except Exception as e:
            print(f"❌ {description}: Failed - Unexpected error: {e}")
            results.append({"description": description, "result": "Failed"})
            driver.get("https://www.booking.com/")

    driver.quit()

    with open("test_results.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    run_tests()