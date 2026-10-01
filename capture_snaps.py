import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def capture_screenshots():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,780")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        url = "http://127.0.0.1:8000"
        driver.get(url)
        time.sleep(2)
        
        # 1. Placement Predictor
        driver.find_element(By.ID, "tab-btn-predictor").click()
        time.sleep(1)
        driver.save_screenshot(r"C:\Users\SUMIT\.gemini\antigravity\scratch\codebhaiya\screenshot_predictor.png")
        print("Captured: screenshot_predictor.png")
        
        # 2. PyTorch Tab - click train to show live training!
        driver.find_element(By.ID, "tab-btn-pytorch").click()
        time.sleep(1)
        driver.find_element(By.ID, "btn-train-pt").click()
        time.sleep(2) # wait for training completion
        driver.save_screenshot(r"C:\Users\SUMIT\.gemini\antigravity\scratch\codebhaiya\screenshot_pytorch.png")
        print("Captured: screenshot_pytorch.png")
        
        # 3. AI Debugger Tab
        driver.find_element(By.ID, "tab-btn-debugger").click()
        time.sleep(1)
        # click debug
        driver.find_element(By.ID, "btn-debug").click()
        time.sleep(1.5)
        driver.save_screenshot(r"C:\Users\SUMIT\.gemini\antigravity\scratch\codebhaiya\screenshot_debugger.png")
        print("Captured: screenshot_debugger.png")
        
        # 4. NLP Interview Tab
        driver.find_element(By.ID, "tab-btn-interview").click()
        time.sleep(1)
        driver.find_element(By.ID, "btn-nlp-score").click()
        time.sleep(1.5)
        driver.save_screenshot(r"C:\Users\SUMIT\.gemini\antigravity\scratch\codebhaiya\screenshot_interview.png")
        print("Captured: screenshot_interview.png")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    capture_screenshots()
