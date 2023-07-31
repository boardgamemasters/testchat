import streamlit as st
from time import sleep 
import pandas as pd
from streamlit_chat import message
from streamlit_carousel import carousel


games = pd.Series(['lama', 'cow', 'lama', 'beetle', 'lama',
               'hippo'])

# test_items = [
#     dict(
#         title="Slide 1",
#         text="A tree in the savannah",
#         interval=None,
#         img="https://cf.geekdo-images.com/EVfMwPiHmxDUvY32BbghBg__imagepage/img/vFmU3UHOT8CT0ssjOw4OFmwR2jA=/fit-in/900x600/filters:no_upscale():strip_icc()/pic7378384.jpg",
#     ),
#     dict(
#         title="Slide 2",
#         text="A wooden bridge in a forest in Autumn",
#         img="https://cf.geekdo-images.com/x3zxjr-Vw5iU4yDPg70Jgw__imagepage/img/-17KkOmxbTu2slJTabGrkO8ZW8s=/fit-in/900x600/filters:no_upscale():strip_icc()/pic3490053.jpg",
#     ),
#     dict(
#         title="Slide 3",
#         text="A distant mountain chain preceded by a sea",
#         img="https://img.freepik.com/free-photo/aerial-beautiful-shot-seashore-with-hills-background-sunset_181624-24143.jpg?w=1380&t=st=1688825798~exp=1688826398~hmac=f623f88d5ece83600dac7e6af29a0230d06619f7305745db387481a4bb5874a0",
#     ),
# ]

# carousel(items=test_items, width=1)

# def on_input_change():
#     user_input = st.session_state.user_input
#     st.session_state.responses.append(user_input)




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

with st.container():
    selecthor = 0
    count =0
    # while 1==1:
    for response in (st.session_state.responses):
        count +=1
        if selecthor == 0:
            message(response, is_user = True, key=f"a1{count}")
            if games.str.fullmatch(response, case = False).any():
                sel_game = games.loc[games.str.fullmatch(response, case = False)][0]
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


with st.container():
    st.text_input("User Response:", on_change=on_input_change, key="user_input")
