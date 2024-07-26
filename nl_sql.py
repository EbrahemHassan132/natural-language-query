import pandas as pd
import sqlite3
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import AgentType
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
import requests

# Step 1: Load the Excel file into a DataFrame
excel_file_path = r'Intern NLP Dataset.xlsx'
df = pd.read_excel(excel_file_path)

# Step 2: Define the path to the SQLite database file
db_file_path = 'Intern_NLP_Dataset.db'

# Step 3: Check if the SQLite database file exists and delete it if it does
if os.path.exists(db_file_path):
    os.remove(db_file_path)
    print(f"Existing database file '{db_file_path}' has been deleted.")

# Step 4: Create a new connection to the SQLite database
conn = sqlite3.connect(db_file_path)

# Step 5: Write the DataFrame to the SQLite database
df.to_sql('visits_table', conn, if_exists='replace', index=False)

# Step 6: Close the connection
conn.close()
print(f"Data has been written to '{db_file_path}' successfully.")

# Initialize the LLM
# To get the free google_api_key visit https://aistudio.google.com/app/apikey and press Create API key
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key="Your API key")

# Load tools for the agent
tools = load_tools(["llm-math"], llm=llm)

# Path to your SQLite database file
db_file_path = r"Intern_NLP_Dataset.db"

# Create the SQLDatabase instance for SQLite
db = SQLDatabase.from_uri(f"sqlite:///{db_file_path}")

# Create the SQLDatabaseToolkit instance
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# Create the SQL agent executor
agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

# Prompt the user for a question
user_question = input("Please enter your question: ")

try:
    # Run the agent with the user's question
    response = agent.invoke(user_question + " Use the whole data you have access to.")
    
    # Check if the response is empty or indicates that it cannot answer
    if response in ["", None, "I don't know", "Unable to answer"]:
        print("This question can't be answered based on the current data.")
    else:
        # Print the response from the agent
        print("Response from agent:")
        print(response)
except requests.exceptions.HTTPError as http_err:
    if http_err.response.status_code == 429:
        print("Rate limit exceeded or quota exhausted. Please try a different question or try again later.")
    else:
        print(f"HTTP error occurred: {http_err}")
except Exception as e:
    # Print a generic error message in case of an exception
    print("An error occurred while processing the question.")
    print(f"Error details: {e}")
