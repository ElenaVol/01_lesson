
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    
    
    images = WebDriverWait(driver, 15).until(
        lambda d: [
            img for img in d.find_elements(By.CSS_SELECTOR, "#image-container img")
            if img.get_attribute("complete") and img.get_attribute("naturalWidth") != "0"
        ]
    )
    
    
    WebDriverWait(driver, 10).until(
        lambda d: len(d.find_elements(By.CSS_SELECTOR, "#image-container img")) >= 4
    )
    
    
    all_images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
    
    
    if len(all_images) >= 3:
        third_image = all_images[2]
        third_image_src = third_image.get_attribute("src")
        
        
        print("SRC третьей картинки:", third_image_src)
    else:
        print(f"Ошибка: найдено только {len(all_images)} изображений")

finally:
    driver.quit()