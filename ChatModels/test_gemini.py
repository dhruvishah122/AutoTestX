import json
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import subprocess  # To run another Python script
# Step 1: Load test cases from JSON
with open('test_cases.json', 'r') as file:
    test_cases = json.load(file)

# Step 2: Convert test cases to a JSON string for the prompt
test_cases_json = json.dumps(test_cases, indent=4)

# Step 3: Define the Prompt Template
prompt_template = PromptTemplate(
    input_variables=['test_cases'],
    template="""
You are a Selenium WebDriver testing code generator.  
Generate a Python Selenium test script for https://www.booking.com/ based on the following test cases:

{test_cases}

The code must:
1. Use `webdriver.Chrome()`.
2. Handle implicit waits.
3. Perform actions based on `xpath`, `action`, and `value`.
4. After each test, print:
   - "✅ [description]: Passed" if the expected behavior is seen.
   - "❌ [description]: Failed" if not.
5. At the end, output a JSON summary like:
[
  {{"description": "Test case name", "result": "Passed/Failed"}}
] and it should save this output to test_results.json.

**NOTE:** Use try-except to handle errors gracefully so all tests continue even if one fails and if any popups appear code should be able to click cross or ok to come out of it.

Generate only the Python code without explanations also if i am navigating to other pages like login/signup, in the next testcase if the xpath doesnt exist on the current url then go on base url and then test the next testcase.
"""
)

# Step 4: Format the prompt with the actual test cases
formatted_prompt = prompt_template.format(test_cases=test_cases_json)
os.environ["GOOGLE_API_KEY"] = "AIzaSyBDEHjBIjXHndCpDnx_pRKaH-On8QwgMjs"

# Step 5: Initialize Gemini Pro model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.2
)

# Step 6: Invoke the model
response = llm.invoke(formatted_prompt)

# Step 7: Clean the response if wrapped in ```json or ```python
cleaned = response.content.strip()
if cleaned.lower().startswith("```python"):
    cleaned = cleaned[9:].strip()
if cleaned.endswith("```"):
    cleaned = cleaned[:-3].strip()

# Step 8: Save the generated code to a file
with open('generated_selenium_test.py', 'w', encoding='utf-8') as f:
    f.write(cleaned)

print("✅ Selenium Test Code saved to 'generated_selenium_test.py'")
print("🚀 Calling generated_selenium_test.py...")
subprocess.run(["python", "generated_selenium_test.py"])  # This will run chat_gemini.py after saving xpaths
