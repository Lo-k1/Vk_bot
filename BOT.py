import vk_api, json, copy, requests, time, random, sqlite3
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.utils import get_random_id
from keyboards import *
from goroda import goroda

posled_buk = ''
goroda_b = []
token = '57c35e1494be81d0b23f1439ca85c50e6178e562e1515989ebf70c0a015c59cc551b00800a978305576d0'
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, group_id='203707737')
sp_saymon = []
sp = [['', '', ''], ['', '', ''], ['', '', '']]
game = True
vremena = []
regim = 0
game_saymon = False
keyboard1_saymon = copy.deepcopy(keyboard_saymon)
keyboard_cat_copy = copy.deepcopy(keyboard_cat)
sp1_saymon = copy.deepcopy(sp_saymon)
colors = ['primary', 'positive', 'negative']
pos = 0
n1 = 0
chey_hod = 0
keyboard1 = copy.deepcopy(keyboard)
sp1 = copy.deepcopy(sp)
d, d1 = 0, 0


def generate():
    a = random.randint(0, 8)
    sp_saymon.append(a)
    sp1_saymon.append(a)


def show(sp_saymon):
    global game
    global vremena
    global keyboard_saymon
    global keyboard1_saymon
    game = False
    vremena = []
    k = 0
    sender('Запоминайте', id, keyboard_saymon)
    for i in sp_saymon:
        keyboard_saymon['buttons'][i // 3][i % 3]['color'] = 'primary'
        k += 1
        sender('&#4448;', id, keyboard_saymon)
        time.sleep(1)
        keyboard_saymon = copy.deepcopy(keyboard1_saymon)
        sender('&#4448;', id, keyboard_saymon)
        time.sleep(0.5)
    sender('Время нажимать', id, keyboard_saymon)
    game = True
    vremena.append(time.time())


def sender(text, id, keyboard):
    vk_session.method('messages.send',
                      {'user_id': id, 'message': text, 'random_id': get_random_id(),
                       'keyboard': json.dumps(keyboard, ensure_ascii=False)})


def ii(sp):
    global n1
    global pos
    if n1 == 1:
        if sp[0].count('') + sp[1].count('') + sp[2].count('') == 9:
            return 2, 2
        else:
            if sp[0][0] == '0' and pos != 4 and (sp[0].count('') + sp[1].count('') + sp[2].count('') == 7):
                pos = 4
                return 2, 0
            elif sp[0][0] == '0' and pos == 4 and (sp[0].count('') + sp[1].count('') + sp[2].count('') == 5):
                if sp[2][1] == '':
                    return 2, 1
                else:
                    return 0, 2
            elif sp[0][0] == '0' and pos == 4 and (sp[0].count('') + sp[1].count('') + sp[2].count('') == 3):
                if sp[1][1] == '':
                    return 1, 1
                else:
                    return 1, 2
            if sp[1][1] == '0' and (sp[0].count('') + sp[1].count('') + sp[2].count('') == 7) and pos != 3:
                pos = 3
                return 0, 0
            elif sp[1][0] == '0' and pos == 3 and sp[1][2] == '':
                return 1, 2
            elif sp[1][2] == '0' and pos == 3 and sp[1][0] == '':
                return 1, 0
            elif sp[0][1] == '0' and pos == 3 and sp[2][1] == '':
                return 2, 1
            elif sp[2][1] == '0' and pos == 3 and sp[0][1] == '':
                return 0, 1
            elif sp[2][0] == '0' and pos == 3 and sp[0][2] == '':
                return 0, 2
            elif sp[0][2] == '0' and pos == 3 and sp[2][0] == '':
                return 2, 0
            elif (sp[2][0] == '0' or sp[2][1] == '0' or sp[1][0] == '0') and (
                    sp[0].count('') + sp[1].count('') + sp[2].count('') == 7) and pos != 1:
                pos = 1
                return 0, 2
            elif (sp[2][0] == '0' or sp[2][1] == '0' or sp[1][0] == '0') and (
                    sp[0].count('') + sp[1].count('') + sp[2].count('') == 5 and pos == 1):
                if sp[1][2] == '':
                    return 1, 2
                else:
                    if sp[1][0] == '0':
                        return 1, 1
                    return 0, 0
            elif (sp[2][0] == '0' or sp[2][1] == '0' or sp[1][0] == '0') and (
                    sp[0].count('') + sp[1].count('') + sp[2].count('') == 3 and pos == 1):
                if sp[0][0] == '' and sp[1][1] == '1':
                    return 0, 0
                elif sp[0][0] == '0' and sp[1][1] == '1':
                    return 2, 0
                if sp[0][1] == '' and sp[0][0] == '1':
                    return 0, 1
                else:
                    return 1, 1
            elif (sp[0][2] == '0' or sp[0][1] == '0' or sp[1][2] == '0') and sp[0].count('') + sp[1].count('') + sp[
                2].count('') == 7 and pos != 2:
                pos = 2
                return 2, 0
            elif (sp[0][2] == '0' or sp[0][1] == '0' or sp[1][2] == '0') and (
                    sp[0].count('') + sp[1].count('') + sp[2].count('') == 5) and pos == 2:
                if sp[2][1] == '':
                    return 2, 1
                else:
                    if sp[0][2] == '0':
                        return 0, 0
                    else:
                        return 1, 1
            elif (sp[0][2] == '0' or sp[0][1] == '0' or sp[1][2] == '0') and (
                    sp[0].count('') + sp[1].count('') + sp[2].count('') == 3 and pos == 2):
                if sp[0][0] == '1':
                    if sp[1][0] == '':
                        return 1, 0
                    else:
                        return 1, 1
                if sp[1][1] == '1' and sp[0][0] == '':
                    return 0, 0
                else:
                    return 0, 2
    elif n1 == 3:
        f = random.randint(1, 2)
        if f == 1:
            for i in range(len(sp)):
                for j in range(len(sp[i])):
                    if sp[i][j] == '':
                        return i, j
        else:
            for i in range(len(sp) - 1, -1, -1):
                for j in range(len(sp[i]) - 1, -1, -1):
                    if sp[i][j] == '':
                        return i, j


def hod(a, b):
    global n1
    global sp
    global id
    global keyboard
    if n1 == 3:
        if sp[a][b] != '':
            sender("Эта клетка уже занята", id, keyboard)
        else:
            sp[a][b] = '0'
            keyboard['buttons'][a][b]['action']['label'] = '&#11093;'
            sender("Ваш ход", event.object.user_id, keyboard)
    else:
        if sp[a][b] != '':
            sender("Эта клетка уже занята", id, keyboard)
        else:
            sp[a][b] = '1'
            keyboard['buttons'][a][b]['action']['label'] = '&#10060;'
            sender("Ваш ход", event.object.user_id, keyboard)


def add(id):
    con = sqlite3.connect('stats.db')
    cur = con.cursor()
    result = cur.execute("""SELECT us_id FROM data""").fetchall()
    for elem in result:
        if id == elem[0]:
            con.close()
            return True
    user = vk_session.method("users.get", {"user_ids": id})
    full = user[0]['first_name'] + ' ' + user[0]['last_name']
    cur.execute("""INSERT INTO data (record_saymon, record, fullname, us_id)
    VALUES (""" + str(0) + """,""" + str(0) + """,\"""" + full + """\",""" + str(id) + """)""")
    con.commit()
    con.close()

    return False


def proverka_hoda_cat(pos, new_pos):
    if new_pos == 4 or new_pos == 7:
        return False
    if (abs(pos - new_pos) == 1 or abs(pos - new_pos) == 3) and (
            (pos % 3 == new_pos % 3) or (pos // 3 == new_pos // 3)):
        return True
    return False


def reyting_up(id, resultat):
    con = sqlite3.connect('stats.db')
    cur = con.cursor()
    if resultat == 0:
        cur.execute("""UPDATE data
        SET record = record + 1
        WHERE us_id = """ + str(id))
    else:
        cur.execute("""UPDATE data
            SET record = record + 2
            WHERE us_id = """ + str(id))
    con.commit()
    con.close()


def reyting_up_saymon(id, reyting):
    con = sqlite3.connect('stats.db')
    cur = con.cursor()
    rec = cur.execute("""SELECT record_saymon FROM data
WHERE us_id = """ + str(id))
    for elem in rec:
        record = elem[0]
    if reyting > record:
        cur.execute("""UPDATE data
                    SET record_saymon = """ + str(reyting) + '\n' +
                    """WHERE us_id = """ + str(id))
    con.commit()
    con.close()


def liders(val):
    s = ''
    con = sqlite3.connect('stats.db')
    cur = con.cursor()
    if val == 1:
        result = cur.execute("""SELECT record, fullname FROM data""").fetchall()
    else:
        result = cur.execute("""SELECT record_saymon, fullname FROM data""").fetchall()
    if len(result) > 10:
        result = result[:10]

    result.sort(key=lambda student: int(student[0]), reverse=True)
    i = 1
    for k in result:
        if k[0] != 0:
            if i == 1:
                s += '&#129351;' + ' ' + k[1] + ' ' + str(k[0]) + '\n'
            elif i == 2:
                s += '&#129352;' + ' ' + k[1] + ' ' + str(k[0]) + '\n'
            elif i == 3:
                s += '&#129353;' + ' ' + k[1] + ' ' + str(k[0]) + '\n'
            else:
                s += str(i) + '. ' + k[1] + ' ' + str(k[0]) + '\n'
        i += 1
    con.commit()
    con.close()
    if s == '':
        s = 'Тут никого нет)'
        return s
    return s


def check_win(s):
    global game
    if (s[0][0] == s[0][1] and s[0][1] == s[0][2] and s[0][0] == '1') or (
            s[1][0] == s[1][1] and s[1][1] == s[1][2] and s[1][0] == '1') or (
            s[2][0] == s[2][1] and s[2][1] == s[2][2] and s[2][0] == '1') or (
            s[0][0] == s[1][0] and s[1][0] == s[2][0] and s[0][0] == '1') or (
            s[0][1] == s[1][1] and s[1][1] == s[2][1] and s[0][1] == '1') or (
            s[0][2] == s[1][2] and s[1][2] == s[2][2] and s[0][2] == '1') or (
            s[0][0] == s[1][1] and s[1][1] == s[2][2] and s[0][0] == '1') or (
            s[0][2] == s[1][1] and s[1][1] == s[2][0] and s[0][2] == '1'):
        sender("Победили крестики", event.object.user_id, keyboard)
        game = False
        return 1
    elif (s[0][0] == s[0][1] and s[0][1] == s[0][2] and s[0][0] == '0') or (
            s[1][0] == s[1][1] and s[1][1] == s[1][2] and s[1][0] == '0') or (
            s[2][0] == s[2][1] and s[2][1] == s[2][2] and s[2][0] == '0') or (
            s[0][0] == s[1][0] and s[1][0] == s[2][0] and s[0][0] == '0') or (
            s[0][1] == s[1][1] and s[1][1] == s[2][1] and s[0][1] == '0') or (
            s[0][2] == s[1][2] and s[1][2] == s[2][2] and s[0][2] == '0') or (
            s[0][0] == s[1][1] and s[1][1] == s[2][2] and s[0][0] == '0') or (
            s[0][2] == s[1][1] and s[1][1] == s[2][0] and s[0][2] == '0'):
        sender("Победили нолики", event.object.user_id, keyboard)
        game = False
        return 2
    elif '' not in s[0] and '' not in s[1] and '' not in s[2]:
        sender("Ничья", event.object.user_id, keyboard)
        game = False
        return 0


def proverka_vremeny():
    global vrem
    global vremena
    vremena.append(time.time())
    if len(vremena) > 1:
        for i in range(len(vremena) - 1):
            if abs(vremena[i + 1] - vremena[i]) > vrem:
                return True
    return False


try:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            add(event.obj.message['from_id'])
            if regim == 0:
                sender('Привет, хотите поиграть?', event.obj.message['from_id'], keyboard_start)
            elif regim == 3:
                if 'хорошо' in event.message.text.lower() or 'ок' in event.message.text.lower() or 'давай' in event.message.text.lower() or 'ладно' in event.message.text.lower():
                    sender(
                        "Я вас не понимаю, нажмите на кнопку",
                        event.obj.message['from_id'], keyboard_slon)
                else:
                    sender('Все говорят \'' + event.message.text + '\', а ты купи слона', event.obj.message['from_id'],
                           keyboard_slon)
            elif regim == 5:
                text = event.message.text.lower().capitalize()
                if '-' in text:
                    text = text.split('-')
                    for i in range(len(text)):
                        text[i] = text[i].lower().capitalize()
                    text = '-'.join(text)
                if text not in goroda:
                    sender('Такой столицы нет', event.obj.message['from_id'], keybord_goroda)
                else:
                    if text in goroda_b:
                        sender('Такой город уже был', event.obj.message['from_id'], keybord_goroda)
                    else:
                        if posled_buk != text[0] and posled_buk != '':
                            sender('Слово должна начинатся на последнюю букву предыдущего слова',
                                   event.obj.message['from_id'], keybord_goroda)
                        else:
                            goroda_b.append(text)
                            sym = text[-1]
                            if sym in ['ъ', 'ы', 'ь']:
                                sym = text[-2]
                            for i in goroda:
                                if sym.upper() == i[0] and i not in goroda_b:
                                    sender(i, event.obj.message['from_id'], keybord_goroda)
                                    goroda_b.append(i)
                                    posled_buk = i[-1]
                                    if posled_buk in ['ъ', 'ы', 'ь']:
                                        posled_buk = i[-2]
                                    break
        elif event.type == VkBotEventType.MESSAGE_EVENT:
            n = int(event.object['payload'])
            id = event.object.user_id
            if n == 1004 or n == 10000:
                sender('Выберите игру', id, keybord_nachalo)
                regim = 0
            elif n == 1000:
                regim = 1
                sender('Выберите режим', id, keybord_vibor)
                keyboard = copy.deepcopy(keyboard1)
                sp = copy.deepcopy(sp1)
                pos = 0
                game = True
            elif n == 10004:
                regim = 5
                sender('Введите название столицы', id, keybord_goroda)
            elif n == 1001:
                regim = 2
                sender('Выберите режим', id, keybord_vibor_saymon)
                keyboard_saymon = copy.deepcopy(keyboard1_saymon)
                sp_saymon = copy.deepcopy(sp1_saymon)
            elif n == 1002:
                regim = 3
                sender('Купи слона', id, keyboard_slon)
            elif n == 1003:
                keyboard_cat = copy.deepcopy(keyboard_cat_copy)
                regim = 4
                position_cat = 6
                sender('Пройдите лабиринт, ходить можно только на белые, соседние по стороне клетки', id, keyboard_cat)
            else:
                if regim == 4:
                    if n == 11:
                        sender('Выберите игру', id, keybord_nachalo)
                        regim = 0
                    elif n == 10:
                        keyboard_cat = copy.deepcopy(keyboard_cat_copy)
                        position_cat = 6
                        sender('Пройдите лабиринт', id, keyboard_cat)
                    else:
                        if proverka_hoda_cat(position_cat, n):
                            if n == 8:
                                otv = requests.get('https://api.thecatapi.com/v1/images/search').json()
                                url = otv[0]['url']
                                vk.messages.sendMessageEventAnswer(
                                    event_id=event.object.event_id,
                                    user_id=event.object.user_id,
                                    peer_id=event.object.peer_id,
                                    event_data=json.dumps({
                                        "type": "open_link",
                                        "link": url
                                    }))
                                sender('Выберите игру', id, keybord_nachalo)
                                regim = 0
                            else:
                                keyboard_cat['buttons'][n // 3][n % 3]['action']['label'] = '&#128008;'
                                keyboard_cat['buttons'][position_cat // 3][position_cat % 3]['action'][
                                    'label'] = '&#4448;'
                                sender('&#4448;', id, keyboard_cat)
                                position_cat = n
                        else:
                            sender('Я не могу туда походить', id, keyboard_cat)
                elif regim == 5:
                    if n == 10:
                        sender('Выберите игру', id, keybord_nachalo)
                        regim = 0
                    elif n == 11:
                        sender('Введите название столицы', id, keybord_goroda)
                        goroda_b = []
                        posled_buk = ''
                elif regim == 2:
                    if n == 10:
                        sp_saymon = []
                        sp1_saymon = []
                        sender('Начинаем', id, keyboard_saymon)
                        generate()
                        show(sp_saymon)
                        game_saymon = True
                    elif n == 101 or n == 102 or n == 103:
                        vrem = n - 98
                        sp_saymon = []
                        sp1_saymon = []
                        sender('Начинаем', id, keyboard_saymon)
                        generate()
                        show(sp_saymon)
                    elif n == 12:
                        st = liders(2)
                        sender(st, id, keybord_vibor_saymon)
                    elif n == 105:
                        sender('&#128313;Запоминайте загорающиеся кнопки\n'
                               '&#128313;С каждымм разом кнопок становится больше\n'
                               '&#128313;Запоминайте загорающиеся кнопки, время ограничено\n', id, keybord_vibor_saymon)
                    elif n == 1100:
                        sender('Выберите игру', id, keybord_nachalo)
                        regim = 0
                    elif n == 11:
                        sender('Выберите режим', id, keybord_vibor_saymon)
                    else:
                        if game_saymon:
                            if n == sp1_saymon[0]:
                                d1 = d
                                if proverka_vremeny():
                                    keyboard_saymon['buttons'][n // 3][n % 3]['color'] = 'negative'
                                    sender('Время вышло', id, keyboard_saymon)
                                    keyboard_saymon['buttons'][n // 3][n % 3]['color'] = 'secondary'
                                    game_saymon = False
                                    continue
                                sp1_saymon.pop(0)
                                keyboard_saymon['buttons'][n // 3][n % 3]['color'] = 'positive'
                                sender('Ok', id, keyboard_saymon)
                                keyboard_saymon['buttons'][n // 3][n % 3]['color'] = 'secondary'
                                sender('&#4448;', id, keyboard_saymon)
                                if len(sp1_saymon) == 0:
                                    reyting_up_saymon(id, len(sp))
                                    generate()
                                    show(sp_saymon)
                                    sp1_saymon = copy.deepcopy(sp_saymon)
                            else:
                                keyboard_saymon['buttons'][n // 3][n % 3]['color'] = 'negative'
                                sender('Игра окончена', id, keyboard_saymon)
                                keyboard_saymon['buttons'][n // 3][n % 3]['color'] = 'secondary'
                                game_saymon = False
                elif regim == 1:
                    if n == 150:
                        sender('&#128313;Рейтинг можно получить играя только против компьютера\n'
                               '&#128313;За победу даётся 2 очка, за ничью 1 очко, за поражение 0 очков', id,
                               keybord_vibor)
                    elif n == 170:
                        sender('Выбирите игру', id, keybord_nachalo)
                    elif n == 100 or n == 11:
                        sender('Выберите режим', id, keybord_vibor)
                        keyboard = copy.deepcopy(keyboard1)
                        sp = copy.deepcopy(sp1)
                        pos = 0
                        game = True
                    elif n == 160:
                        sender('&#128313;Рейтинг можно получить играя только против компьютера\n'
                               '&#128313;За победу даётся 2 очка, за ничью 1 очко, за поражение 0 очков', id,
                               keyboard_start)
                    elif n == 161:
                        st = liders(1)
                        sender(st, id, keybord_vibor)
                    elif n == 150:
                        otv = requests.get('https://api.thecatapi.com/v1/images/search').json()
                        url = otv[0]['url']
                        vk.messages.sendMessageEventAnswer(
                            event_id=event.object.event_id,
                            user_id=event.object.user_id,
                            peer_id=event.object.peer_id,
                            event_data=json.dumps({
                                "type": "open_link",
                                "link": url
                            }))
                    elif n == 102:
                        n1 = 2
                        sender('Начинаем, ходит Игрок1', id, keyboard)
                    elif n == 101:
                        sender('За кого вы хотите играть?', id, keyboard_kresikilinolik)
                    elif n == 106:
                        n1 = 1
                        sender('Начинаем, ходит компьютер', id, keyboard)
                        a, b = ii(sp)
                        hod(a, b)
                        check_win(sp)
                    elif n == 105:
                        n1 = 3
                        sender('Начинаем, ваш ход', id, keyboard)
                    elif n < 11 and n1 == 2:
                        if n != 101:
                            if n == 10:
                                game = True
                                keyboard = copy.deepcopy(keyboard1)
                                sp = copy.deepcopy(sp1)
                                chey_hod = 0
                                sender("Заново", id, keyboard)
                            else:
                                if game:
                                    if sp[n // 3][n % 3] == '' and chey_hod == 0:
                                        keyboard['buttons'][n // 3][n % 3]['action']['label'] = '&#10060;'
                                        sender("Ходит Игрок2", id, keyboard)
                                        sp[n // 3][n % 3] = '1'
                                        chey_hod = 1
                                        check_win(sp)
                                    elif sp[n // 3][n % 3] == '' and chey_hod == 1:
                                        keyboard['buttons'][n // 3][n % 3]['action']['label'] = '&#11093;'
                                        sender("Ходит Игрок1", id, keyboard)
                                        sp[n // 3][n % 3] = '0'
                                        chey_hod = 0
                                        check_win(sp)
                                    else:
                                        sender("Эта клетка уже занята", id, keyboard)
                                else:
                                    sender("Игра окончена", id, keyboard)
                    elif n < 11 and n1 == 1:
                        if n != 101:
                            if n == 10:
                                game = True
                                keyboard = copy.deepcopy(keyboard1)
                                sp = copy.deepcopy(sp1)
                                sender("Заново", id, keyboard)
                                sender('Начинаем, ходит компьютер', id, keyboard)
                                a, b = ii(sp)
                                hod(a, b)
                                check_win(sp)
                                pos = 0
                            else:
                                if game:
                                    if sp[n // 3][n % 3] == '':
                                        keyboard['buttons'][n // 3][n % 3]['action']['label'] = '&#11093;'
                                        sender("Ходит компьютер", id, keyboard)
                                        sp[n // 3][n % 3] = '0'
                                        chey_hod = 0
                                        res = check_win(sp)
                                        if res:
                                            print(res)
                                            reyting_up(id, 0)
                                        if game:
                                            a, b = ii(sp)
                                            hod(a, b)
                                            res = check_win(sp)
                                            if res == 0:
                                                reyting_up(id, res)
                                    else:
                                        sender("Эта клетка уже занята", id, keyboard)
                                else:
                                    sender("Игра окончена", id, keyboard)
                    elif n < 11 and n1 == 3:
                        if n != 101:
                            if n == 10:
                                game = True
                                keyboard = copy.deepcopy(keyboard1)
                                sp = copy.deepcopy(sp1)
                                sender("Заново", id, keyboard)
                                sender('Начинаем, ваш ход', id, keyboard)
                                pos = 0
                            else:
                                if game:
                                    if sp[n // 3][n % 3] == '':
                                        keyboard['buttons'][n // 3][n % 3]['action']['label'] = '&#10060;'
                                        sender("Ходит компьютер", id, keyboard)
                                        sp[n // 3][n % 3] = '1'
                                        res = check_win(sp)
                                        if res:
                                            reyting_up(id, res)
                                        if game:
                                            a, b = ii(sp)
                                            hod(a, b)
                                            res = check_win(sp)
                                            if res == 0:
                                                reyting_up(id, 0)
                                    else:
                                        sender("Эта клетка уже занята", id, keyboard)
                                else:
                                    sender("Игра окончена", id, keyboard)
except requests.exceptions.ReadTimeout:
    time.sleep(3)
