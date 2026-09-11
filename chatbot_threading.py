import streamlit as st
from chatbot_langgraph_backend import chatbot
from langchain_core.messages import HumanMessage
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['LANGCHAIN_PROJECT'] = 'chatbot-project'

# ******************************** Utility functions ****************************************

def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread(thread_id)
    st.session_state['message_history'] = []
    st.session_state['thread_names'][thread_id] = str(thread_id)

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)
        
def load_conversation(thread_id):
    state = chatbot.get_state(config={'configurable':{'thread_id':thread_id}})
    return state.values.get('messages',[])

# ******************************** Session Setup ****************************************

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []
    
if "thread_id" not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()
    
if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = []
    
if 'thread_names' not in st.session_state:
    st.session_state['thread_names'] = {}
    
    
add_thread(st.session_state['thread_id'])


# ******************************** Sidebar UI ****************************************

st.sidebar.title("LangGraph chatbot")

if st.sidebar.button("New Chat"):
    reset_chat()

st.sidebar.header("My conversation")

for thread_id in st.session_state['chat_threads'][::-1]:
    thread_name = st.session_state['thread_names'].get(
        thread_id,
        str(thread_id)
    )
    if st.sidebar.button(thread_name,key=f"chat_{thread_id}"):
        st.session_state['thread_id'] = thread_id
        messages = load_conversation(thread_id)
        
        temp_messages = []
        
        for msg in messages:
            if isinstance(msg,HumanMessage):
                role='user'
            else:
                role='ai'
            temp_messages.append({'role':role,'content':msg.content})
        
        st.session_state['message_history'] = temp_messages
    

# ******************************** Main UI ****************************************

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])
    
user_input = st.chat_input("Type here")

if user_input:
    
    thread_id = st.session_state['thread_id']
    
    if len(st.session_state['message_history']) == 0:
        st.session_state['thread_names'][thread_id] = user_input        
    
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message("user"):
        st.text(user_input)
        
    CONFIG = {
        "configurable": {"thread_id": st.session_state["thread_id"]},
        "metadata": {
            "thread_id": st.session_state["thread_id"]
        },
        "run_name": "chat_turn",
    }
        
    with st.chat_message('ai'):
        
        ai_message = st.write_stream(
            message_chunk.content for message_chunk,metadata in chatbot.stream(
                {'messages':[HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode='messages'
            )
        )
    
    st.session_state['message_history'].append({'role':'ai','content':ai_message})
    