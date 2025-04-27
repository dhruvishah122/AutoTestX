from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options 
import json 
import time 
import subprocess  # To run another Python script
 
def generate_xpath(driver, element):
    """Generate a more robust absolute XPath for an element"""
    return driver.execute_script("""
        function getFullXPath(element) {
            // If we've hit the root node, return it
            if (!element || element.nodeType !== 1) {
                return '';
            }
            
            if (element === document.body) {
                return '/html/body';
            }
            
            // Get all siblings of the same type
            let siblings = Array.from(element.parentNode.childNodes)
                .filter(node => node.nodeType === 1 && node.tagName === element.tagName);
                
            // Get the index among siblings of same type (1-based for XPath)
            let index = siblings.indexOf(element) + 1;
            
            // Build the XPath step for this element
            let step = element.tagName.toLowerCase();
            if (siblings.length > 1) {
                step += '[' + index + ']';
            }
            
            // Recurse up the DOM tree
            let parentPath = getFullXPath(element.parentNode);
            return parentPath + '/' + step;
        }
        
        // Handle the HTML root element specially
        if (arguments[0].tagName.toLowerCase() === 'html') {
            return '/html';
        }
        
        return getFullXPath(arguments[0]);
    """, element)
 
def get_element_name(el): 
    try: 
        text = el.text.strip() 
        if text: 
            return text[:40] 
        elif el.get_attribute("aria-label"): 
            return el.get_attribute("aria-label") 
        elif el.get_attribute("placeholder"): 
            return el.get_attribute("placeholder") 
        elif el.get_attribute("type"): 
            return f"{el.tag_name} ({el.get_attribute('type')})" 
        else: 
            return el.tag_name 
    except Exception as e: 
        print(f"Error getting name for element: {e}") 
        return "Unnamed" 
 
def extract_key_xpaths(url, max_elements=150): 
    print(f"🌐 Launching browser for URL: {url}") 
    options = Options() 
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options) 
    driver.get(url) 
    print("⏳ Waiting for the page to fully load...") 
    time.sleep(6) 
 
    target_tags = ["a", "button", "input", "span", "div", "body"] 
    named_xpaths = {} 
    total_elements_checked = 0 
 
    for tag in target_tags: 
        print(f"🔍 Scanning tag: {tag}") 
        elements = driver.find_elements(By.TAG_NAME, tag) 
        for el in elements[:max_elements]: 
            try: 
                if el.is_displayed(): 
                    total_elements_checked += 1 
                    name = get_element_name(el) 
                    xpath = generate_xpath(driver, el) 
                    if xpath: 
                        print(f"✅ Element: {name} | XPath: {xpath}") 
                        named_xpaths[name] = xpath 
            except Exception as e: 
                print(f"⚠️ Skipped element due to error: {e}") 
                continue 
 
    driver.quit() 
 
    with open("gen_xpaths.json", "w") as f: 
        json.dump(named_xpaths, f, indent=4) 
 
    print(f"\n📁 Total elements processed: {total_elements_checked}") 
    print("✅ Fast XPaths saved to 'gen_xpaths.json'.") 
    print("🚀 Calling chat_gemini.py...")
    subprocess.run(["python", "chat_gemini.py"])
 
# Run it 
extract_key_xpaths("https://www.booking.com/", max_elements=100)