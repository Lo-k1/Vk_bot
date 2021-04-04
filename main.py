import vk_api, json, copy, requests, time, random, sqlite3
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.utils import get_random_id
from vk_api import VkUpload
from keyboards import *

token = '2b34eaef665779c0f7366ab853ec7bf3c43f1c91572b6b29bb019d8360f9c8680d10f2f2c27613b18de4f'
sp = [['', '', ''], ['', '', ''], ['', '', '']]

game = True
keyboard1 = copy.deepcopy(keyboard)
sp1 = copy.deepcopy(sp)
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, group_id='203404027')
upload = VkUpload(vk_session)
pos = 0
n1 = 0
chey_hod = 0


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


def sender(text, id, keyboard):
    vk_session.method('messages.send',
                      {'user_id': id, 'message': text, 'random_id': get_random_id(),
                       'keyboard': json.dumps(keyboard, ensure_ascii=False)})


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
    cur.execute("""INSERT INTO data (record, fullname, us_id)
    VALUES (""" + str(0) + """,\"""" + full + """\",""" + str(id) + """)""")
    con.commit()
    con.close()
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


def liders():
    s = ''
    con = sqlite3.connect('stats.db')
    cur = con.cursor()
    result = cur.execute("""SELECT record, fullname FROM data""").fetchall()
    if len(result) > 10:
        result = result[:10]
    elif len(result) == 0:
        s = 'Тут никого нет)'
        return s
    result.sort(key=lambda student: int(student[0]), reverse=True)
    i = 1
    for k in result:
        s += str(i) + '. ' + k[1] + ' ' + str(k[0]) + '\n'
        i += 1
    con.commit()
    con.close()
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


try:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if add(event.obj.message['from_id']):
                sender('Рады снова вас видеть, хотите поиграть в крестики-нолики?)', event.obj.message['from_id'],
                       keyboard_start)
            else:
                sender('Привет, хотите поиграть в крестики-нолики?)', event.obj.message['from_id'], keyboard_start)
        elif event.type == VkBotEventType.MESSAGE_EVENT:
            n = int(event.object['payload'])
            id = event.object.user_id
            if n == 103:
                sender('Режим в разработке', id, keybord_vibor)
            if n == 100 or n == 11:
                sender('Выберите режим', id, keybord_vibor)
                keyboard = copy.deepcopy(keyboard1)
                sp = copy.deepcopy(sp1)
                pos = 0
                game = True
            elif n == 160:
                sender('1)Рейтинг можно получить играя только против компьютера\n'
                       '2)За победу даётся 2 очка, за ничью 1 очко, за поражение 0 очков', id,
                       keyboard_start)
            elif n == 161:
                st = liders()
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
                                        print(res)
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
