import os
from groq import Groq
from dotenv import load_dotenv


load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Function to get information for a specific location
def get_location_info(location):
    # Create a query based on the user's input location
    query = f"I am relocating to {location.upper()}, is there anything I need to know regarding emergency policies, building infrastructure regarding climate, emergency evacuation plans, and additional resources I can use. Please tell me the following information:\n - A summary of natural disaster and climate risks in {location.upper()} \n- Climate and natural disaster emergency policies in {location.upper()} \n- Things to have in a climate emergency in {location.upper()} \n- Emergency contacts in {location.upper()}"

    # Make the API call
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": f"Provide detailed information about natural disaster risks, emergency policies, and preparation recommendations for {location.upper()}."
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
    for chunk in completion:
        print(chunk.choices[0].delta.content or "", end="")

# Example usage
#location = "Manila, Philippines"  # Replace this with any location you want to query
#get_location_info(location)

