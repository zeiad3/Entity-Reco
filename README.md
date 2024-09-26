Named Entity Recognition (NER) App
Overview
The Named Entity Recognition (NER) App is a simple web application that uses the SpaCy library to identify named entities (such as people, organizations, dates, locations, etc.) in a given text. Users can input text, and the app will highlight the detected named entities directly on the web page.

This app is built using Streamlit for the user interface and SpaCy for natural language processing and entity recognition.

Features
Text Input: Users can input any text they want to analyze.
Named Entity Recognition: The app identifies named entities like people, organizations, locations, and dates using SpaCy's pre-trained NER model.
Entity Highlighting: The identified entities are highlighted and displayed interactively using SpaCy's displacy visualizer.
Prerequisites
Before you run the app, ensure that the following are installed:

Python 3.x
Required Python packages:
streamlit
spacy
SpaCy's language model en_core_web_sm
You can install the dependencies by running:

bash
نسخ الكود
pip install streamlit spacy
python -m spacy download en_core_web_sm
How It Works
The user inputs a block of text into the text area.
When the user clicks "Analyze", the app processes the input text using SpaCy's pre-trained English model (en_core_web_sm).
The app identifies various named entities in the text and uses SpaCy's displacy.render to create an HTML visualization of the named entities.
The processed result, with highlighted entities, is displayed on the webpage.
How to Run
Clone the repository or copy the script to a local folder.

Navigate to the folder where the script is located.

Run the following command to launch the app:

bash
نسخ الكود
streamlit run app.py
A browser window will open where you can input text and see the identified named entities.

Code Explanation
st.title("Named Entity Reco"): Sets the title of the web app.
nlp = spacy.load("en_core_web_sm"): Loads the small English language model from SpaCy, which includes NER capabilities.
text = st.text_area("Input Text"): Provides a text area for the user to input the text they want analyzed.
st.button("Analyze"): This button triggers the analysis of the input text.
displacy.render(doc, style="ent", page=True): This line generates an HTML representation of the named entities in the input text, highlighting the entities such as persons, organizations, and locations.
st.write(html, unsafe_allow_html=True): Renders the HTML output from SpaCy's displacy and allows the interactive display of the highlighted named entities.
File Structure
bash
نسخ الكود

Example
Run the app with streamlit run app.py.
Enter text in the text area (e.g., "Apple is looking at buying U.K. startup for $1 billion").
Click "Analyze" and view the highlighted entities such as "Apple" (ORG), "U.K." (GPE), and "$1 billion" (MONEY).
