# Import the necessary libraries
import pandas as pd
from openai import OpenAI
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load the data
df = pd.read_csv("transcriptions.csv")
df.head()
# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("api_key"))

def extract_medical_info(transcription):
    messages = [
        {'role': 'system', 'content': 'use the extract_age_treatement function, DO NOT put your own data, if the fiend is missing create the field and specify "unknown" .'},
        {'role': 'user', 'content':f"extract and return the age and the treatment: {transcription} "}
    ]
    
    
    function_definition = [
        {'type': 'function',
         'function':{
             'name': 'extract_age_treatement',
             'description': 'extract the age and the recomended treatment for each input. always retun both the age and the recomended treatment',
             'parameters': {
                 'type': 'object',
                 'properties': {
                     'age': {
                         'type': 'integer',
                         'description': 'age of the patient'
                     },
                     'treatment':{
                         'type': 'string',
                         'description': 'recomended tratment'
                     }}}}}]
    
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=messages,
        tools = function_definition
    )

    return json.loads(response.choices[0].message.tool_calls[0].function.arguments)


def get_icd_codes(treatment):
    if treatment != 'unknown':
        response = client.chat.completions.create(
            model = 'gpt-4o-mini',
            messages = [{
                'role': 'user',
                'content': f"provide the ICD for the following treatments {treatment}. return a list of code. only include code and no other informations"
            }],
            temperature=0.3
        )
        return response.choices[0].message.content
    else:
        return 'unknown'

# Initialize list to store processed data
processed_data = []

# Process each row in the DataFrame
for index, row in df.iterrows():
    medical_specialty = row['medical_specialty']
    extracted_data = extract_medical_info(row['transcription'])
    icd_code = get_icd_codes(extracted_data["treatment"]) if 'treatment' in extracted_data.keys() else 'unknown'
    extracted_data["Medical Specialty"] = medical_specialty
    extracted_data["ICD Code"] = icd_code

    # Append the extracted information as a new row in the list
    processed_data.append(extracted_data)

# Convert the list to a DataFrame
df_structured = pd.DataFrame(processed_data)   
print(df_structured)