
import streamlit as st
import smtplib
from email.message import EmailMessage

st.set_page_config(page_title="Registo de Cliente — Emporio Italia")

# Inserir logotipo
st.image("Positive.png", width=300)

st.title("📋 Formulário de Registo de Cliente — Emporio Italia")

st.markdown("Por favor preencha os campos abaixo. Após submissão, os dados serão enviados à nossa equipa administrativa.")

with st.form("formulario_cliente"):
    nome_empresa = st.text_input("Nome da empresa")
    nome_estabelecimento = st.text_input("Nome do estabelecimento")
    nif = st.text_input("NIF")
    email_contacto = st.text_input("Email de contacto")
    pessoa_contacto = st.text_input("Pessoa de contacto")
    morada_entrega = st.text_area("Morada de entrega")
    email_financeiro = st.text_input("Email da contabilidade/financeiro")
    horario_entrega = st.text_input("Horário de entrega")
    plafond_credito = st.text_input("Plafond de crédito requerido")
    condicoes_pagamento = st.text_input("Condições de pagamento requeridas")

    submitted = st.form_submit_button("Enviar")

    if submitted:
        corpo = f"""
        NOVO FORMULÁRIO DE CLIENTE:

        Nome da empresa: {nome_empresa}
        Nome do estabelecimento: {nome_estabelecimento}
        NIF: {nif}
        Email de contacto: {email_contacto}
        Pessoa de contacto: {pessoa_contacto}
        Morada de entrega: {morada_entrega}
        Email da contabilidade: {email_financeiro}
        Horário de entrega: {horario_entrega}
        Plafond de crédito requerido: {plafond_credito}
        Condições de pagamento requeridas: {condicoes_pagamento}
        """

        msg = EmailMessage()
        msg['Subject'] = "Novo Registo de Cliente - Emporio Italia"
        msg['From'] = "costa@emporioitalia.pt"
        msg['To'] = "info@emporioitalia.pt"
        msg.set_content(corpo)

        try:
            smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp.login("costa@emporioitalia.pt", "SUA_APP_PASSWORD")
            smtp.send_message(msg)
            smtp.quit()
            st.success("Formulário enviado com sucesso! A nossa equipa entrará em contacto brevemente.")
        except Exception as e:
            st.error("Ocorreu um erro ao enviar o formulário. Por favor contacte info@emporioitalia.pt")
            st.stop()

        st.info("Nota: substitua 'SUA_APP_PASSWORD' pela App Password real da conta Gmail costa@emporioitalia.pt.")
