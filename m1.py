import pinecone

import openai

import requests

 

# Initialize Pinecone and OpenAI API

pinecone.init(api_key="pcsk_4FqKa9_2xMgJNhy8WMYbzgY5tFAcgnomSpPTtdbam5dLZLd8xzU8LwcVboYY4bo1jqU6rW")

openai.api_key = "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"

 

# Define Pinecone index

index = pinecone.Index("job-market")

 

# Function to get real-time job trends

def get_job_trends(query):

    response = requests.get(f'https://api.serper.io/job-trends?q={query}')

    return response.json()

 

# Function to retrieve user preferences from Pinecone

def retrieve_user_preferences(user_id):

    result = index.query(user_id, top_k=5)  # Retrieve the top 5 relevant memories

    return result

 

# Function to generate a response with the agent's LLM

def generate_response(user_query, user_id):

    # Retrieve past user data (career goals, preferences)

    user_data = retrieve_user_preferences(user_id)

   

    # Fetch real-time job trends

    job_trends = get_job_trends(user_query)

   

    # Combine historical data and real-time data for personalized response

    response = openai.Completion.create(

        model="gpt-4",

        prompt=f"User preferences: {user_data}. Current trends: {job_trends}. Query: {user_query}",

        max_tokens=150

    )

    return response.choices[0].text.strip()

 

 

 
