import streamlit as st
from time import sleep 
import pandas as pd
from streamlit_chat import message
from streamlit_carousel import carousel


games = pd.Series(['lama', 'cow', 'lama', 'beetle', 'lama',
               'hippo'])

def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.responses.append(user_input)
    st.session_state.user_input = ""  # Clear the input after processing



def on_btn_click():
    del st.session_state['questions']
    del st.session_state['responses']
    selecthor = 0

st.session_state.setdefault('questions', [])

st.title("Survey QA Bot")
questions_list = [
    # 0
    '''I would like to recommend you some Boardgames.
    What is your favorite one?'''    
    # 1
    , '''I dont know this Game.
    Please enter another one'''
    # 2
    , '''How many recommendations do you want to get?
    'Please enter a Number between 1 and 5'''
]

if 'responses' not in st.session_state.keys():
    st.session_state.questions.extend(questions_list)
    st.session_state.responses = []
  



chat_placeholder = st.empty()
st.button("Clear message", on_click=on_btn_click)

message(st.session_state.questions[0]) 

# Add custom CSS to position the chatbot in the bottom right corner and size it as Samsung S22 mobile
st.markdown("""
<style>
    .main-container {
        display: flex;
        justify-content: flex-end;
        align-items: flex-end;
        height: 100vh;
        width: 100vw;
        overflow: hidden;
    }

    .chatbot-box {
        width: 375px; /* Samsung S22 mobile width */
        height: 860px; /* Samsung S22 mobile height */
        max-height: calc(100vh - 40px); /* Limit height to fit screen */
        overflow-y: auto;
        border: 1px solid black;
        border-radius: 10px;
        background-color: #f0f0f0; /* Change background color as needed */
        padding: 10px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Place the chatbot code inside the div with the chatbot-box class

with st.container():
#with st.sidebar(): # Place the chatbot code inside the sidebar
    selecthor = 0
    count =0
    # while 1==1:
    for response in (st.session_state.responses):
        count +=1
        #response = response.lower()  # Convert user response to lowercase
        if selecthor == 0:
            message(response, is_user = True, key=f"a1{count}")
            if games.str.fullmatch(response, case = False).any():
              if ((games.str.fullmatch(response, case = False)).sum())!=1:
                sel_game = games.loc[games.str.fullmatch(response, case = False)][0]
              else:
                sel_game = games.loc[games.str.fullmatch(response, case = False)]
              selecthor = 1
              message(st.session_state.questions[2], key=f"b2{count}")  
              continue
            else:
                message(st.session_state.questions[1], key=f"b1{count}")
        if selecthor == 1:
            # message(st.session_state.questions[2], key=f"b2{count}")
            message(response, is_user = True, key=f"a2{count}")
            if response.isnumeric():
                alt = response
                selecthor = 3
                message(f'''Your favorite boardgame is {sel_game}.
                And you would like to get {alt} recommendations for similar games.
                Is that correct?
                (y) , (n)''', key=f"b4{count}")
                continue
            else:
                message('Please enter a numeric value', key=f"b3{count}")
        if selecthor== 2:
            # message(f'''Your favorite boardgame is {sel_game}.
            # And you would like to get {alt} recommendations for similar games.
            # Is that correct?
            # (y) , (n)''', key=f"b4{count}")
            selecthor = 3
            continue
        if selecthor== 3:
            message(response, is_user = True, key=f"a3{count}")  
            if (pd.Series(['y', 'Y', 'yes', 'Yes'])).isin([response]).any():
                message('I can recommend you the following games:', key=f"b5{count}")
            elif (pd.Series(['n', 'N', 'no', 'No'])).isin([response]).any():
                message('Lets try again', key=f"b6{count}")
                selecthor = 0
                continue
            else:
                message(f'''{response} is not a valid input. Please try again
                What is your favorite Boardgame?''', key=f"b7{count}")
                selecthor = 0
                continue
                
                     
                   
    
    # for response, question in zip(st.session_state.responses, st.session_state.questions[1:]):
    #     message(response, )
    #     message(response)
    #     message(question)

st.markdown('</div>', unsafe_allow_html=True)
#with st.container():
    #st.text_input("User Response:", on_change=on_input_change, key="user_input")

