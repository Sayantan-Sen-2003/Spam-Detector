# import streamlit as st 
# import pickle
# import nltk
# import string
# from nltk.corpus import stopwords
# from nltk.stem.porter import PorterStemmer

# # from joblib import dump, load

# ps= PorterStemmer()

# def transform_text(text):
#     text = text.lower()
#     text = nltk.word_tokenize(text)
    
#     y = []
#     for i in text:
#         if i.isalnum():
#             y.append(i)
    
#     text = y[:]
#     y.clear()
    
#     for i in text:
#         if i not in stopwords.words('english') and i not in string.punctuation:
#             y.append(i)
            
#     text = y[:]
#     y.clear()
    
#     for i in text:
#         y.append(ps.stem(i))
    
            
#     return " ".join(y)
# # a= transform_text("This is me cooking!!")



# tfidf = pickle.load(open('vectorizer.pkl','rb'))
# model= pickle.load(open('model.pkl','rb'))

# # dump(tfidf, 'vectorizer.joblib') #to convert and save pkl file into joblib file
# # dump(model, 'model.joblib') ##to convert and save pkl file into joblib file

# # tfidf = load('vectorizer.joblib') #loadiing joblib files
# # model = load('model.joblib')     #loadiing joblib files

# st.title("Email/SMS Spam Classifier")

# input_sms = st.text_area("Enter the message")

# if st.button('Predict'):

#     #1. PreProcess
#     transformed_sms = transform_text(input_sms)
#     #2. Vectorize
#     vector_input = tfidf.transform([transformed_sms])
#     #3. Predict
#     result = model.predict(vector_input)
#     #4. Display
#     if result[0] == 1:
#         st.header("Spam")
#     else:
#         st.header("Not Spam")


import streamlit as st
import pickle
import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

st.image('res/spam-icon.jpg', use_column_width=True)


# css = '''
#  <style>
# body {
#     margin: 0;
#     padding: 0;
#     font-family: Arial, sans-serif;
#     display: flex;
#     justify-content: center;
#     align-items: center;
#     height: 100vh;
#     background-color: #000; /* Set background color to black */
# }

# .card {
#     background-color: #fff; /* Set card background color to white */
#     border-radius: 10px;
#     padding: 20px;
#     box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
#     transition: background-color 0.5s ease;
# }

# .card:hover {
#     background-color: #87CEEB; /* Change card background color on hover */
# }

# '''

# index = '''
# <body>
#  <div class="card">
#  </div>
# </body>
# '''
# st.write(index,  unsafe_allow_html=True)
# st.write(css,  unsafe_allow_html=True)


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("Spam Detector")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
  # 1. PreProcess
    transformed_sms = transform_text(input_sms)
    # 2. Vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. Predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")





text_data ="""
Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T&C's apply 08452810075over18's.

SMS. ac Sptv: The New Jersey Devils and the Detroit Red Wings play Ice Hockey. Correct or Incorrect? End? Reply END SPTV.

07732584351 - Rodger Burns - MSG = We tried to call you re your reply to our sms for a free nokia mobile + free camcorder. Please call now 08000930705 for delivery tomorrow.

Urgent UR awarded a complimentary trip to EuroDisinc Trav, Aco&Entry41 Or å£1000. To claim txt DIS to 87121 18+6*å£1.50(moreFrmMob. ShrAcomOrSglSuplt)10, LS1 3AJ			

Please call our customer service representative on 0800 169 6031 between 10am-9pm as you have WON a guaranteed å£1000 cash or £5000 prize!

Your free ringtone is waiting to be collected. Simply text the password MIX  to 85069 to verify. Get Usher and Britney. FM  PO Box 5249	 MK17 92H. 450Ppw 16"	
			
Sunshine Quiz Wkly Q! Win a top Sony DVD player if u know which country the Algarve is in? Txt ansr to 82277. å£1.50 SP:Tyrone			

You'll not rcv any more msgs from the chat svc. For FREE Hardcore services text GO to: 69988 If u get nothing u must Age Verify with yr network & try again	

Customer service annoncement. You have a New Years delivery waiting for you. Please call 07046744435 now to arrange delivery.
			
URGENT! We are trying to contact you. Last weekends draw shows that you have won a å£900 prize GUARANTEED. Call 09061701939. Claim code S89. Valid 12hrs only			
		
"""

# Create a download button for the text file
st.download_button(
    label="Download Sample Spam Text File",
    data=text_data,
    file_name="sample.txt",
    mime="text/plain"
)


navbar_html = """
<style>
    .navbar {
        position: relative;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #333;
        color: white;
        text-align: center;
        padding: 10px;
        box-shadow: 0px -2px 5px 0px rgba(0,0,0,0.2);
        z-index: 9999;
    }
    .navbar a {
        color: white;
        padding: 14px 20px;
        text-decoration: none;
        display: inline-block;
    }
    .navbar a:hover {
        background-color: #ddd;
        color: black;
    }
</style>
<div class="navbar">
    <a href="https://github.com/Sayantan-Sen-2003" target="_self">Github</a>
    <a href="https://leetcode.com/u/Sayantan_Sen/" target="_self">LeetCode</a>
</div>
"""

# Display the navbar using st.markdown
st.markdown(navbar_html, unsafe_allow_html=True)
