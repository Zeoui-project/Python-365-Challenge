# %% [markdown]
# # PDF to Audio using Python

# %%
import PyPDF2, pyttsx3

path = open('test.pdf', 'rb')

pdfReader = PyPDF2.PdfReader(path)

# Get an Engine instance for the speech synthesis
speak = pyttsx3.init()

for page_num in range(len(pdfReader.pages)):
    text = pdfReader.pages[page_num].extract_text()
    speak.say(text)
    speak.runAndWait()

speak.stop()