from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from random import randint

sum_candies = 2021
max_step = 28
count = 0

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name
    id = update.effective_user.id
    await update.message.reply_text(f'Привет! {name}!\nЯ - CandyDad! У меня есть для тебя замечательная игра!\n ')
    await update.message.reply_text(f'На столе лежит 2021 конфета.\nТы и я будем делать ходы по очереди.\nМожно взять не более 28 конфет за один ход.\nВыигрывает и получает все конфеты тот, кто ходит последним!!!')
    await update.message.reply_text(f'Если ты отважен и готов сыграть со мной, введи команду /go\n ')
    print(f'Игрок {name}, ID {id} ')
    
async def toss_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global sum_candies, max_step, count, first, second
    player1 = update.effective_user.first_name
    player2 = 'CandyDad'
    await update.message.reply_text(f'Я рад, что мне достался смелый противник!\n Начинаем игру: {player1} против {player2}!')
    await update.message.reply_text(f'Определим, кто ходит первым')

    x = randint(1, 2)
    if x == 1:
        first = player1
        second = player2
    else:
        first = player2
        second = player1
    await update.message.reply_text(f'Игрок {first} ходит первым!')
    
    
    sum_candies = 2021    
    max_step = 28
    count = 0
    
    cur = second if count % 2 else first
    if cur == "CandyDad":
        n = randint(1, max_step)
        await update.message.reply_text(f'Игрок CandyDad взял {n} конфет')
        print(f'Игрок CandyDad взял {n} конфет')
        sum_candies -= n
        count += 1
    await update.message.reply_text(f'Всего конфет {sum_candies}. Ты можешь взять от 1 до {max_step} конфет. Введи количество конфет')
        
async def game_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global sum_candies, max_step, count, first, second
    if max_step*sum_candies == 0:
        await update.message.reply_text(f'Игра окончена. Чтобы начать заново, нажмите /go')
        return
    n = int(update.message.text)
    print(f'Игрок {update.effective_user.first_name} взял {n} конфет')
    if not (n > 0 and n < (max_step+1)):
        await update.message.reply_text(f'Неверное количество. Попробуйте еще раз\nТы можешь взять от 1 до {max_step} конфет')
        return
    else:
        sum_candies -= n
        count += 1        # считаем ходы
    if sum_candies <= max_step:
        max_step = sum_candies
    print(f'Осталось {sum_candies}')
    
    if sum_candies > 0:
        n = randint(1, max_step)
        await update.message.reply_text(f'Игрок CandyDad взял {n} конфет')
        print(f'Игрок CandyDad взял {n} конфет')
        sum_candies -= n
        count += 1
        if sum_candies <= max_step:
            max_step = sum_candies          
    
    if sum_candies <= 0:
        if count % 2 == 1:
            await update.message.reply_text(f'Игрок ' + first + ' победил и забирает все конфеты!')
        else:
            await update.message.reply_text(f'Игрок ' + second + ' победил и забирает все конфеты!')
        return
    await update.message.reply_text(f'Всего конфет {sum_candies}. Ты можешь взять от 1 до {max_step} конфет. Введи количество конфет')