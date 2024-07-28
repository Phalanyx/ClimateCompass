import os
from groq import Groq
from decouple import config





# Function to get information for a specific location
def get_location_info_goverment_aid_polices(location):
    client = Groq(
    api_key = config('GROQ_API_KEY')
    
)

    # Create a query based on the user's input location
    query = (
        f"I am currently residing in {location.upper()}, is there anything I need to know regarding"
        "emergency policies for natural disasters and government aid? do not add or use asterisks or number them\n"
        f"- Summary of emergency policies for different natural disasters in {location.upper()}do not add or use asterisks or number them\n"
        f"- Summary of government aid for different natural disasters in {location.upper()} do not add or use asterisks or number them"
    )

    # Make the API call
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": f"Provide detailed information about emergency policies and government aid related to natural disasters in {location.upper()} do not add or use asterisks or number them."
            },
            {
                "role": "user",
                "content": query
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    # Print the response
    ret = []
    ret.append("GOVERNMENT AID AND POLICIES:")
    for chunk in completion:
        ret.append(chunk.choices[0].delta.content)
    return ret

def get_location_info_relocations(location):
    client = Groq(
    api_key = config('GROQ_API_KEY')
    
)

    # Create a query based on the user's input location
    query = (
        f"I am currently residing in {location.upper()}, is there anything I need to know regarding"
        "possible permanent and temporary relocations when there are natural disasters? do not add or use asterisks or number them\n"
        f"- Give me a list of possible relocations that the government would advise the people of {location.upper()} "
        "to move to in the event of a natural disaster. do not add or use asterisks or number them"
    )

    # Make the API call
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
       messages=[
            {
                "role": "system",
                "content": f"Provide detailed information about possible permanent and temporary relocations in case of natural disasters for people residing in {location.upper()}.do not add or use asterisks or number them"
            },
            {
                "role": "user",
                "content": query
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    # Print the response
    i = 0
    ret = []
    ret.append("RELOCATIONS:")
    for chunk in completion:
        if (i==5):
            break
        
        ret.append(chunk.choices[0].delta.content)
        i+=1
    return ret

# Function to get information for a specific location
def get_location_info_useful_knowledge(location):
    client = Groq(
    api_key = config('GROQ_API_KEY')
    
)

    # Create a query based on the user's input location
    query = (
        f"I am currently residing in {location.upper()}, is there anything I need to know regarding "
        "food banks, essentials to have in a climate emergency, gas stations, and counseling for people "
        "who were traumatized from natural disasters?do not add or use asterisks or number them\n"
        f"- Things to have in a climate emergency (e.g., residents in Canada must have KI pills in the event of a nuclear accident) in {location.upper()} do not add or use asterisks or number them\n"
        f"- Food banks in the area in {location.upper()} do not add or use asterisks or number them"
        f"- Emergency contacts in {location.upper()}do not add or use asterisks or number them\n"
        f"- Counseling for people who were traumatized from natural disasters in {location.upper()} do not add or use asterisks or number them"
    )


    # Make the API call
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": f"Provide detailed information about essentials to have in a climate emergency, food banks, emergency contacts, and counseling for trauma from natural disasters in {location.upper()}."
            },
            {
                "role": "user",
                "content": query
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    # Print the response
    i = 0
    ret = []
    ret.append("USEFUL KNOWLEDGE:")
    for chunk in completion:
        if (i==5):
            break
        ret.append(chunk.choices[0].delta.content)
        i+=1
    return ret

# Function to get information for a specific location
def get_location_info_emergency_contacts(location):
    client = Groq(
    api_key = config('GROQ_API_KEY')
    
)

    # Create a query based on the user's input location
    query = (
        f"I am currently residing in {location.upper()}, is there anything I need to know regarding "
        "emergency contacts for natural disasters and in general?\n"
        f"- Summary of all emergency contacts for natural disasters and in general in {location.upper()}"
    )

    # Make the API call
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": f"Provide detailed information about emergency contacts for natural disasters and general emergencies in {location.upper()}. do not add or use asterisks or number them"
            },
            {
                "role": "user",
                "content": query
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    # Print the response
    i = 0
    ret = []
    for chunk in completion:
        if (i==5):
            break
        ret.append(chunk.choices[0].delta.content)
        i+=1
    return ret

# Example usage
#location = "Manila, Philippines"  # Replace this with any location you want to query
#get_location_info_goverment_aid_polices(location)
#get_location_info_relocations(location)
#get_location_info_useful_knowledge(location)
#get_location_info_emergency_contacts(location)

