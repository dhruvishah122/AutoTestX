# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# import json

# load_dotenv()
# model=ChatGoogleGenerativeAI(model="gemini-1.5-pro")
# response = model.invoke("generate functional testcases for www.flipkart.com in below example json format with correct xpaths with json accepted format and dont write any extra things apart from testcases please just give testcases generated in response without any instructions or description pls and dont even add anything like json before testcases just and just testcases"
# """{
#         "description": "Verify that the search input field is clickable.",
#         "type": "input_field",
#         "action": "click",
#         "xpath": "//*[@id=\"react-application\"]/DIV[1]/DIV[1]/DIV[1]/DIV[1]/DIV[3]/DIV[2]/DIV[1]/DIV[1]/DIV[1]/HEADER[1]/DIV[1]/DIV[2]/DIV[2]/DIV[1]/DIV[1]/DIV[1]/FORM[1]/DIV[1]/DIV[1]/DIV[1]/INPUT[1]",
#         "expected": "no_error"
#     }""")
# # res1= model.invoke("generate selenium code for ${result.content} testcases")
# data = json.loads(result.content)

# Step 1: Remove leading "json" if present
# cleaned = response.content.strip()
# if cleaned.lower().startswith('json'):
#     cleaned = cleaned[4:].strip()

# # Step 2: Wrap in square brackets to form a valid JSON list
# cleaned_json = f'[{cleaned}]'
# if cleaned_json.startswith('[') and cleaned_json.endswith(']'):
#     cleaned_json = cleaned_json[1:-1]  # Remove [ and ]
#     cleaned_json = cleaned_json[7:]    # Remove first 7 (```json\n)
#     cleaned_json = cleaned_json[:-3]   # Remove last 3 (```)
# cleaned_json = f'[{cleaned_json}]'
# print(cleaned_json)
# # Step 3: Parse JSON
# try:
#     data = json.loads(cleaned_json)
#     print("✅ Parsed JSON:", data)
#     with open('test_cases.json', 'w') as json_file:
#         json.dump(data, json_file, indent=4)
# except json.JSONDecodeError as e:
#     print("❌ JSON Decode Error:", e)

# # print(res1.content)
# import fitz  # PyMuPDF - Extracts text from PDFs
# import json  # Saves extracted data in structured format
# import re  # For pattern matching
# from nltk.tokenize import sent_tokenize
# import nltk

# # Download the sentence tokenizer if not already available
# nltk.download("punkt")

# # Define the feature keywords to extract
# feature_keywords = {
#     "login": ["log in", "login", "sign in"],
#     "signup": ["sign up", "register", "create account"],
#     "navbar": ["navigation", "menu", "navbar"],
#     "cart": ["cart", "checkout", "purchase"],
#     "response_time": ["response time", "loading speed", "performance"],
#     "search": ["search", "find", "lookup"]
# }

# # Define the PDF file path
# pdf_path = r"pdf.pdf"  # Use raw string (r"") to avoid path issues


# def extract_text_from_pdf(pdf_path):
#     """Extracts raw text from the given PDF file."""
#     doc = fitz.open(pdf_path)
#     text = ""
    
#     for page in doc:
#         text += page.get_text("text") + "\n"  # Extract text from each page
    
#     return text


# def extract_requirements_from_text(text, feature_keywords):
#     """Extracts relevant requirements based on predefined keywords."""
#     sentences = text.split(".")  # Split text by periods as a fallback
#     extracted_requirements = {}

#     for feature, keywords in feature_keywords.items():
#         pattern = re.compile(r"\b(" + "|".join(keywords) + r")\b", re.IGNORECASE)  # Create regex pattern
#         matched_sentences = [s.strip() for s in sentences if pattern.search(s)]  # Find sentences matching keywords

#         if matched_sentences:
#             extracted_requirements[feature] = matched_sentences  # Store matched sentences
    
#     return extracted_requirements


# # Step 1: Extract raw text from PDF
# pdf_text = extract_text_from_pdf(pdf_path)

# # Step 2: Extract specific requirements from the text
# requirements = extract_requirements_from_text(pdf_text, feature_keywords)

# # Step 3: Save the extracted requirements into a JSON file
# json_output_path = r"extracted_requirements.json"

# with open(json_output_path, "w", encoding="utf-8") as f:
#     json.dump(requirements, f, indent=4)

# # Print extracted requirements
# print("Extracted Requirements (Saved to JSON):")
# print(json.dumps(requirements, indent=4))

# Import necessary libraries
import fitz  # PyMuPDF - Extracts text from PDFs
import json  # Saves extracted data in structured format
import re  # For pattern matching
from nltk.tokenize import sent_tokenize
import nltk
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import subprocess  # To run another Python script

# Download the sentence tokenizer if not already available
nltk.download("punkt")

# Define the feature keywords to extract
feature_keywords = {
    "login/signin": ["log in", "login", "sign in"],
    "signup": ["sign up", "register", "create account"],
    "navbar": ["navigation", "menu", "navbar"],
    "cart": ["cart", "checkout", "purchase"],
    "response_time": ["response time", "loading speed", "performance"],
    "search": ["search", "find", "lookup"]
}

# Define the PDF file path
pdf_path = r"booking_requirements.pdf"  # Use raw string (r"") to avoid path issues
def extract_text_from_pdf(pdf_path):
    """Extracts raw text from the given PDF file."""
    doc = fitz.open(pdf_path)
    text = ""
    
    for page in doc:
        text += page.get_text("text") + "\n"  # Extract text from each page
    
    return text


def extract_requirements_from_text(text, feature_keywords):
    """Extracts relevant requirements based on predefined keywords."""
    sentences = text.split(".")  # Split text by periods as a fallback
    extracted_requirements = {}

    for feature, keywords in feature_keywords.items():
        pattern = re.compile(r"\b(" + "|".join(keywords) + r")\b", re.IGNORECASE)  # Create regex pattern
        matched_sentences = [s.strip() for s in sentences if pattern.search(s)]  # Find sentences matching keywords

        if matched_sentences:
            extracted_requirements[feature] = matched_sentences  # Store matched sentences
    
    return extracted_requirements


# Step 1: Extract raw text from PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Step 2: Extract specific requirements from the text
requirements = extract_requirements_from_text(pdf_text, feature_keywords)
print("Extracted Requirements:")
print(json.dumps(pdf_text, indent=4))
# Step 3: Save the extracted requirements into a JSON file
# json_output_path = r"extracted_requirements.json"

# with open(json_output_path, "w", encoding="utf-8") as f:
#     json.dump(requirements, f, indent=4)

# # Print extracted requirements
# print("Extracted Requirements (Saved to JSON):")
# print(json.dumps(requirements, indent=4))


# Set your Gemini API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyAfIpfBmAkJyOxWAhafhOXdmJDmzApxvhY"

# Load extracted requirements from JSON
with open("extracted_requirements.json", "r", encoding="utf-8") as f:
    extracted_requirements = json.dumps(pdf_text, indent=4)

# Flatten the dictionary into one string
requirements_text = extracted_requirements
# for feature, sentences in extracted_requirements.items():
#     requirements_text += f"\nFeature: {feature}\n"
#     for sentence in sentences:
#         requirements_text += f"- {sentence}\n"

# Define the prompt template

xpaths = []
xpathKeys = []

with open("gen_xpaths.json", 'r', encoding="utf-8") as f:
    data = json.load(f)  # Read JSON once
    xpathKeys = list(data.keys())
    xpaths = list(data.values())
  
# print("XPaths:", xpaths)
template = """
You are a professional QA engineer.
Analyze the following software requirements and generate 20 JSON test cases.

Each test case must follow this format and with xpaths strictly match the testcase description with {xpathKeys} and take xpath from {xpaths} of that key  and dont write any extra text other than testcases xpath must and must support json format so that i can save generated testcases in json file without any error:
must must give xpath from {xpaths} when the description or type or testcases matches to any key of {xpathKeys} take xpath only of the same index from {xpaths} *must give xpath from {xpaths} when the description or type or testcases matches to any key of {xpathKeys} take xpath only of the same index from {xpaths} dont generate random xpaths yourself. the testcases u gave previously are with wrong xpaths so please give testcases strictly with xpaths from {xpaths} *must give xpath from {xpaths} when the description or type or testcases matches to any key of {xpathKeys} take xpath only of the same index from {xpaths} and take some relevant values as examples dont do null values or empty values in testcases and give some relevant values as examples and when user gives the values such as email and password for login/signup must and must use it only.please must generate login and signup testcases with dhruvishah116122@gmail.com as email and Dbms#amazon122 as password and get correct xpaths nly from {xpaths}
must note **must give xpath from {xpaths} when the description or type or testcases matches to any key of {xpathKeys} take xpath only of the same index from {xpaths}
testcases must include testcases for login and signup from credentials given in {requirements}
{{
    "description": "Test case description",
    "type": "input_field/button/navigation",
    "action": "click/send_keys/navigate",
    "xpath": "//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input",
    "value": "Input value non null(take examples based on the requirement)",
    "expected": "Expected outcome"
}}

Requirements:
{requirements}
"""

prompt = PromptTemplate(
    input_variables=["requirements", "xpaths","xpathKeys"],
    template=template
)

# Format the prompt with your extracted requirements
formatted_prompt = prompt.format(requirements=requirements_text, xpaths=xpaths,xpathKeys=xpathKeys)

# Initialize Gemini 1.5 Pro
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.2
)

# Generate test cases
response = llm.invoke(formatted_prompt)
cleaned = response.content.strip()

# If starts with 'json' (sometimes Gemini adds this)
if cleaned.lower().startswith('json'):
    cleaned = cleaned[4:].strip()

# If wrapped in ```json markdown
if cleaned.startswith("```json"):
    cleaned = cleaned[7:].strip()  # Remove ```json
if cleaned.endswith("```"):
    cleaned = cleaned[:-3].strip()  # Remove ```

print("🔹 Cleaned JSON string:\n", cleaned)

# Step 3: Parse JSON
try:
    data = json.loads(cleaned)
    print("✅ Parsed JSON:", data)

    with open('test_cases.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

except json.JSONDecodeError as e:
    print("❌ JSON Decode Error:", e)

# Always print raw response too for debugging
print("\n📢 Raw Model Response:\n", response.content)
print("🚀 Calling xpaths.py...")
subprocess.run(["python", "xpaths.py"])  # This will run chat_gemini.py after saving xpaths
