import streamlit as st
from streamlit_chat import message

games = pd.Series(['lama', 'cow', 'lama', 'beetle', 'lama', 'hippo'])

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

with st.sidebar(): # Place the chatbot code inside the sidebar
    selecthor = 0
    count =0
    # while 1==1:
    for response in (st.session_state.responses):
        count +=1
        if selecthor == 0:
            message(response, is_user=True, key=f"a1{count}")
            if games.str.fullmatch(response, case=False).any():
                if ((games.str.fullmatch(response, case=False)).sum()) != 1:
                    sel_game = games.loc[games.str.fullmatch(response, case=False)][0]
                else:
                    sel_game = games.loc[games.str.fullmatch(response, case=False)]
                selecthor = 1
                message(st.session_state.questions[2], key=f"b2{count}")
                continue
            else:
                message(st.session_state.questions[1], key=f"b1{count}")
        if selecthor == 1:
            message(response, is_user=True, key=f"a2{count}")
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
        if selecthor == 2:
            selecthor = 3
            continue
        if selecthor == 3:
            message(response, is_user=True, key=f"a3{count}")  
            if (pd.Series(['y', 'Y', 'yes', 'Yes'])).isin([response]).any():
                message('I can recommend you the following games:', key=f"b5{count}")
                amey_games = pd.DataFrame({'bgg_id': af.game_of_my_life(user_favorite_game=sel_game, data=amey_df, z=alt)})
                amey_games = ursula.get_feature(result_file=amey_games, feature_file=games_info)
                res_co = 0
                for i in range(len(amey_games)):
                    message(
                        f'<img width="100%" height="200" src="{amey_games.iloc[res_co]["image"]}"/>',
                        key=f"img_{count}_{res_co}",
                        allow_html=True
                    )
                    res_co += 1

col1, col2 = st.beta_columns(2)

# Place the chat input box in the first column
with col1:
    st.text_input("User Response:", on_change=on_input_change, key="user_input")

# Place the chat output (chatbot messages) in the second column
with col2:
    chat_placeholder = st.empty()
    st.button("Clear message", on_click=on_btn_click)
    message(st.session_state.questions[0])

