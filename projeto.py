import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import streamlit as st
#from data import df



st.set_page_config(
    page_title = "Tutorial Streamlit",
    layout = "wide"
)

df = pd.read_csv("entrada")
st.dataframe(df)

r = 1
st.title("JoaoBank")
st.write("Você tem R$", r)

st.sidebar.title("Menu")
opcao = st.sidebar.radio(
    "Esolha um tópico: ",
    [
        "Início",
        "Sua Conta",
        "Configurações",
        "Suporte"
    ]
)

if opcao == "Início":
    brilho = st.slider("Ajuste o brilho", 0, 100, 100, step=5)

    st.header("Bem-vindo ao Streamlit!")
    
    col1, col2 = st.columns(2)

    with col1:
        st.write("Área **PIX**")
        st.info("Nessa área você vai conseguir usar o sistema bancário de transferência por PIX (Made by Banco Central do Brasil)")
        st.text_input("Chave PIX: ", placeholder="CPF, Telefone, e-mail ou aleatória")
        numero = st.number_input("Valor da transferência: R$", value=10, step=5)
    with col2:
        st.write("TED")
        st.info("""
                ### Operações:
                - Transferência em conta
                - Déposito
                - Saque
                - Agendar Transferência
                - Débito Automático""")

    st.write("Como usar esse app: ")
    st.code("""st.set_page_config
    (
    page_title = "Tutorial Streamlit",
    layout = "wide"
    )""", language="python")

elif opcao == "Sua Conta":
    st.header("Widgets básicos")
    st.subheader("1. Botões")
    
    st.markdown("""
        <style>
        .st-key-danger button{
        background-color: #d00000;
        color: white;
        border-radius: 8px;
        font-weight: 600;}
        .st-key-danger button:hover {
        background-color: #ff0000;}
        <style>""", unsafe_allow_html=True)
    
    #st.button("Botao normal")
    #st.container(key="danger").button("Botão perigoso", key="danger")

    if st.button("🙈", key="danger"):
       st.success("Agência: 0001; Conta: 131847-1")
        
    st.divider()

elif opcao == "Configurações":
    st.header("Oi")
    linguagens = st.multiselect(
        "Qual linguagens você conhece?",
        ["Python", "JavaScript", "Java", "C++", "R"],
        #default=["Python"]
        )
    st.write(f"Você selecionou: {', '.join(linguagens)}")

elif opcao == "Suporte":
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Não encontrou sua dúvida? Conte pra gente!")
        nome = st.text_input("Digite sua dúvida: ", placeholder="Ex.: Como ganhar dinheiro sem trabalhar")
        if(nome):
            st.write(f"Sua dúvida é: **{nome}**")
    with col4:
        st.subheader("Dúvidas Frequentes")
    
        dvd = st.selectbox(
            "Escolha uma opção", 
            ["", "Meu pix não funciona", "b", "c"]
            )
        
        if dvd == "Meu pix não funciona":
            st.success("Que pena!")
            st.balloons()

    
