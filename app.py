# Import os to set API key
from apikey import apikey
import os
# Import OpenAI as main LLM service
from langchain.llms import OpenAI

import streamlit as st
from langchain.document_loaders import TextLoader
from langchain.vectorstores import Chroma
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo
)
os.environ['OPENAI_API_KEY'] = apikey

llm = OpenAI(temperature=0.7,
             verbose=True)
loader = TextLoader('./Assets/Transcript1.txt')
pages = loader.load_and_split()
store = Chroma.from_documents(pages, collection_name='input')
vectorstore_info = VectorStoreInfo(
    name="Talk Bit's AI",
    description="Talk to your transcriptions",
    vectorstore=store
)
toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info)
agent_executor = create_vectorstore_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)
st.title("Talk Bit's AI")
prompt = st.text_input('Ask your queries here')

if prompt:
    response = agent_executor.run(prompt)
    st.write(response)
