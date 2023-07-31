import streamlit as st
from streamlit_chat import message

# The rest of your code...

#with st.container():
with st.sidebar(): # Place the chatbot code inside the sidebar
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

# Define the layout with columns and rows
col1, col2 = st.beta_columns(2)

# Place the chat input box in the first column
with col1:
    st.text_input("User Response:", on_change=on_input_change, key="user_input")

# Place the chat output (chatbot messages) in the second column
with col2:
    chat_placeholder = st.empty()
    st.button("Clear message", on_click=on_btn_click)

    message(st.session_state.questions[0])

