import json
import os
import subprocess  # To run another Python script``
# Load xpaths from gen_xpaths.json
xpath_file = 'gen_xpaths.json'
print(f"Loading XPath mappings from {xpath_file}...")

if os.path.exists(xpath_file) and os.path.getsize(xpath_file) > 0:
    with open(xpath_file, 'r', encoding='utf-8') as f:
        try:
            xpaths_dict = json.load(f)
            print(f"Loaded {len(xpaths_dict)} XPath entries.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {xpath_file}: {e}")
            xpaths_dict = {}
else:
    print(f"File {xpath_file} is empty or does not exist.")
    xpaths_dict = {}
print(xpaths_dict)

# Load test cases from test_cases.json
test_cases_file = 'test_cases.json'
print(f"\nLoading test cases from {test_cases_file}...")

if os.path.exists(test_cases_file) and os.path.getsize(test_cases_file) > 0:
    with open(test_cases_file, 'r', encoding='utf-8') as f:
        test_cases = json.load(f)
        print(f"Loaded {len(test_cases)} test cases.")
else:
    print(f"File {test_cases_file} is empty or does not exist.")
    test_cases = []

# Update each test case with the corresponding XPath
print("\nUpdating test cases with corresponding XPaths...")

updated_count = 0
for test_case in test_cases:
    matched = False
    for key in xpaths_dict:
        if key.lower() in test_case.get('description', '').lower():
            print(f"Matching: '{test_case['description']}' with '{key}'")
            test_case['xpath'] = xpaths_dict[key]
            matched = True
            updated_count += 1
            print(f"Updated: '{test_case['description']}' → {xpaths_dict[key]}")
            
    if not matched:
        print(f"No match found for: '{test_case['description']}'")

# Save the updated test cases back to file
with open(test_cases_file, 'w', encoding='utf-8') as f:
    json.dump(test_cases, f, indent=4, ensure_ascii=False)
    print(f"\nSaved updated test cases to {test_cases_file}.")
    print(f"Total updated entries: {updated_count} / {len(test_cases)}")
print("🚀 Calling test_gemini.py...")
subprocess.run(["python", "test_gemini.py"])  # This will run chat_gemini.py after saving xpaths
