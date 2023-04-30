# %% [markdown]
# # Make an Audiobook using Python

# %%
import PyPDF2
import pyttsx3

# Read the pdf by specifying the path in your computer
pdfReader = PyPDF2.PdfReader(open('zeoui-project.pdf', 'rb'))
# Get the handle to speaker
speaker = pyttsx3.init()
# Split the pages and read one by one
for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()

# Stop the speaker after completion
speaker.stop()
# Save the audiobook at the specified path
pyttsx3.engine.save_to_file(text, 'E:\Python\Project-365-Challenge\day-80-audiobook')
pyttsx3.engine.runAndWait()



