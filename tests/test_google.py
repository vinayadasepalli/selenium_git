from selenium import webdriver
from selenium.webdriver.common.by import By

def test_google_search_field_visible():
    # Launch Chrome browser
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    
    # Verify page title to check Google is running
    assert "Google" in driver.title, "Google page did not load successfully"
    
    # Verify search field is visible
    search_box = driver.find_element(By.NAME, "q")
    assert search_box.is_displayed(), "Search field is not visible"
    
    # Close the browser
    driver.quit()
