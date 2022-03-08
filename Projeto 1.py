#!/usr/bin/env python
# coding: utf-8

# Este código tem como objetivo abrir o navegador, acessar o e-mail e enviar uma mensagem ao destinatário informado.

# # Instalando as blibliotecas

# In[ ]:


get_ipython().system('pip install pyautogui')
get_ipython().system('pip install pyperclip')


# # Importando as bibliotecas

# In[ ]:


import pyautogui
import pyperclip
import time


# # Código para marcar a posição onde o cursor do mouse irá clicar

# In[ ]:


time.sleep(5)
pyautogui.position()


# # Executando o código

# In[ ]:


pyautogui.PAUSE = 1 #intervalo de execução de cada linha de código
pyautogui.hotkey("ctrl","t") #abri nova janela do navegador
pyperclip.copy("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox") #endereço da caixa de e-mail
pyautogui.hotkey("ctrl","v") # cola o endereço copiado na linha anterior
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=81, y=188) #posição do cursor para clicar em escrever e-mail
time.sleep(5) 
pyautogui.write("renatoperen@gmail.com") #digita o endereço de e-mail do destinatário
pyautogui.press("tab") #autocompleta o endereço de e-mail
pyautogui.press("tab") #pula para o campo assunto
pyperclip.copy("Teste de e-mail automático") #digita o texto do assunto
pyautogui.hotkey("ctrl","v")
pyautogui.press("tab") #pula para o campo mensagem

#criando uma variável com o texto já formatado
texto = f"""

Olá Renato,

Este é um teste de envio automático de e-mail.

Se você está lendo esta mensagem, seu código funcionou, parabéns!

Abraços
"""
# escreve o conteúdo da variável texto no campo mensagem
pyperclip.copy(texto)
pyautogui.hotkey("ctrl","v") 
pyautogui.hotkey("ctrl","enter")


# In[ ]:




