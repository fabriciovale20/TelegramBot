# Telegram Bot

## Como rodar o projeto:
1. Clone o repositório;
```
git clone https://github.com/fabriciovale20/TelegramBot.git
```
2. Acesse a pasta do projeto;
```
cd TelegramBot
```
3. Crie um ambiente virtual com Python 3;
```
python -m venv .venv
```
4. Ative o Virtualenv;
```
.venv\Scripts\activate
```
5. Instale as dependências;
```
pipenv install
```
6. Realize a criação do seu Bot pessoal através do Telegram;
```
6.1- Inice o telegram;
6.2- Pesquise por BotFather;
6.3- Realize as configurações necessários do tutorial (Nome do Bot, ID do Bot e Gerar Key);
```
7. Acesse o arquivo *bot_scripts.py*;
```
7.1- Substituia a linha 4
CHAVE_API = config('CHAVE_API')  # Key gerada pelo BotFather, altere para a sua

pela sua Key gerada no BotFather
CHAVE_API = "key geraada"  # Key gerada pelo BotFather, altere para a sua
```


8. Rode o servidor.
```
python bot_scripts.py
```

![alt text](jogo.png)
