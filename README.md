
# 📋 Formulário de Registo de Cliente — Emporio Italia

Este projeto em Streamlit permite recolher dados de faturação e entrega de novos clientes da Emporio Italia, com envio automático por email para `info@emporioitalia.pt`.

## Como publicar

1. Faça fork ou clone deste repositório
2. Aceda a [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Clique em "New app" e selecione este repositório
4. Escolha o ficheiro `formulario_cliente_emporio.py`
5. Clique em "Deploy"

## SMTP

Para funcionar corretamente, deve configurar o envio por Gmail:

- Email: `costa@emporioitalia.pt`
- SMTP server: `smtp.gmail.com`
- Port: 465
- Usar uma App Password válida

No código, substitua `"SUA_APP_PASSWORD"` pela app password real gerada em [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

## Link sugerido

Uma vez publicada, poderá partilhar o link diretamente com clientes.
