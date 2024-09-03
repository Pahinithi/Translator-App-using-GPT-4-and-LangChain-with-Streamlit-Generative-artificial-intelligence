# Lanka Translator App - GPT-4

Welcome to the Lanka Translator App, a Streamlit-based application leveraging GPT-4 for seamless language translation. This app allows users to translate text between multiple languages with an intuitive interface and powerful backend.

## Features

- **Language Selection:** Choose from a variety of input and output languages.
- **Text Translation:** Translate text from one language to another using GPT-4.
- **User-Friendly Interface:** Modern design with custom styling for a better user experience.

## Screenshots

<img width="1728" alt="LLM03" src="https://github.com/user-attachments/assets/c09e7722-965d-4776-934d-834ada4530b6">


## Installation

To set up the Lanka Translator App on your local machine, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Pahinithi/Translator-App-using-GPT-4-and-LangChain-with-Streamlit-Generative-artificial-intelligence
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd Lanka-Translator-App
   ```

3. **Create a Virtual Environment (Optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install the Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up Configuration**

   - Create a file named `config.json` in the `src` directory.
   - Add your OpenAI API key to `config.json` in the following format:

     ```json
     {
       "OPENAI_API_KEY": "your-openai-api-key"
     }
     ```

6. **Run the Application**

   ```bash
   streamlit run src/main.py
   ```

## Usage

1. Open the application in your browser using the local URL provided by Streamlit.
2. Select the input language from the dropdown menu.
3. Select the output language from the dropdown menu.
4. Enter the text you want to translate in the text area.
5. Click the "Translate" button to see the translated text.

## Code Overview

### `main.py`

The main script for the Streamlit application.

- **Page Configuration:** Sets the page title, icon, and layout.
- **Custom CSS Styling:** Applies custom styles to the app.
- **Language Selection:** Dropdown menus for input and output languages.
- **Text Translation:** Calls the `translate` function from `translator_utils.py`.
- **Footer:** Displays a custom footer with "Developed by Nithilan".

### `translator_utils.py`

Contains utility functions for translation.

- **OpenAI API Configuration:** Loads the API key from `config.json`.
- **Translation Function:** Uses GPT-4 to translate text based on the selected languages.

## Requirements

The project requires the following Python packages:

- `streamlit==1.35.0`
- `langchain==0.2.1`
- `langchain-openai==0.1.7`

These dependencies are listed in the `requirements.txt` file.

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or feature requests, please submit them via GitHub issues or pull requests.

### How to Contribute

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request.

## License

This project is licensed under the MIT License

## Contact

Developed by Pahirathan Nithilan  
Feel free to reach out for any questions or feedback.
