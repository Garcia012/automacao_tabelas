import pyautogui
import time

pyautogui.PAUSE = 0.5

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

#selecionar campo email e fazer login
pyautogui.click(x=608, y=509)
pyautogui.write("fellipemellogarcia@gmail.com")
pyautogui.press("tab")
pyautogui.write("123@#45")
pyautogui.click(x=953, y=711)
time.sleep(3)

#importar base de dados 
import pandas as pd
tabela = pd.read_csv("produtos.csv")
print(tabela)

#cadastrar produtos
for linha in tabela.index:
    #clicar no campo de código
    pyautogui.click(x=876, y=355)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    # cadastra o produto (botao enviar)
    pyautogui.press("enter") 
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)

