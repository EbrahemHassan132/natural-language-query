# Natural Language Query for SQLite Database

This project demonstrates how to use natural language queries to interact with a SQLite database using the LangChain framework and the Google Generative AI model. It includes steps for loading data from an Excel file into an SQLite database, setting up a language model, and querying the database using natural language.

## Project Structure

- `main.py`: The main Python script that handles data loading, database setup, and query execution.
- `Intern NLP Dataset.xlsx`: Sample Excel file used for this project.

## Prerequisites

Before running the code, ensure you have the following installed:

- Python 3.7 or higher
- Required Python packages (listed in `requirements.txt`)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/EbrahemHassan132/natural-language-query.git
   cd natural-language-query
   ```

2. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Set up your API key:**

   - Obtain a Google API key by visiting [Google AI Studio](https://aistudio.google.com/app/apikey) and pressing "Create API key".
   - Replace `"Your API key"` in `nl_sql.py` with your actual API key.

## Usage

1. **Prepare the Excel File:**

   Ensure the Excel file `Intern NLP Dataset.xlsx` is in the project directory. The file should contain the data you want to load into the SQLite database.

2. **Run the Script:**

   Execute the nl_sql script to load the data into the SQLite database and interact with it using natural language:

   ```sh
   python nl_sql.py
   ```

   You will be prompted to enter a question about the data. The script will process your query and provide a response based on the data in the SQLite database.

## Example

After running the script, you might enter a question like:

```
Which minute had the most visitors?
```

The script will process this question and output the result based on the data in the `Intern_NLP_Dataset.db` database.

## Error Handling

- **Rate Limit Exceeded**: If you receive a 429 HTTP error, it means you've exceeded the API rate limit. Please wait and try again later.
- **General Errors**: If you encounter any other errors, ensure that all dependencies are correctly installed and that your API key is valid.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
