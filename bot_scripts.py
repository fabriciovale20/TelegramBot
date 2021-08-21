import telebot
from decouple import config

CHAVE_API = config('CHAVE_API')  # Key gerada pelo BotFather, altere para a sua Key
bot = telebot.TeleBot(CHAVE_API)


# COMANDO APÓS OPÇÃO SELECIONADA
@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    O que você deseja? (Clique em uma opção)
        /pizza Pizza
        /hamburguer Hamburguer
        /salada Salada"""
    bot.send_message(mensagem.chat.id, texto)


# ITENS DA OPÇÃO 1
@bot.message_handler(commands=["pizza"])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "Sua pizza está saindo para sua casa: Tempo de espera em 20 minutos.")


@bot.message_handler(commands=["hamburguer"])
def hamburguer(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo o Brabo: em 10 minutos chega aí.")


@bot.message_handler(commands=["salada"])
def salada(mensagem):
    bot.send_message(mensagem.chat.id, "Não tem salada não, clique aqui para iniciar: /iniciar")


# EXECUÇÃO OPÇÃO 2
@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    return bot.send_message(mensagem.chat.id, "Para enviar uma reclamação, mande um e-mail para reclamacao@email.com")


# EXECUÇÃO OPÇÃO 3
@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    return bot.send_message(mensagem.chat.id, "Valeu! Fabrício mandou um abraço de volta.")


# VERIFICANDO SE FOI ENVIADO ALGUMA MENSAGEM PARA O BOT
def verificar(mensagem):
    global name

    name = f'{mensagem.from_user.first_name}'
    return True


# MENU DE INICIALIZAÇÃO DO BOT
@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = f"""
    Olá {name}!
    Escolha uma opção para continuar (Clique no item):
        /opcao1 Fazer um pedido
        /opcao2 Reclamar de um pedido
        /opcao3 Mandar uma abraço pro Fabrício
    Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)


# LOOP PARA MANTER O BOOT FUNCIONANDO
bot.polling()
