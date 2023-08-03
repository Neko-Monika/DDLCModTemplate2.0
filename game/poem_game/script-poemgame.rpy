## script-poemgame.rpy

# Этот файл содержит код мини-игры про сочинение стихотворений из DDLC (уже улучшенный [наконец-то...])
# Всё ещё сопровождён комментариями Terra.

init python: 
    # Этот словарь хранит все слова и значения предпочтения конкретных персонажей.
    full_wordlist = {}

    # Этот класс определяет искомое слово и значение очков для каждой из четырёх героинь
    class PoemWord:
        def __init__(self, s, n, y, glitch=False):
            self.sPoint = s
            self.nPoint = n
            self.yPoint = y
            self.glitch = glitch

    # На своих ошибках аффтар не учится, мдэ... (прим. пер.)
    with renpy.open_file("poem_game/poemwords.txt", encoding="utf-8") as pf:
        for line in pf:
            line = line.strip()

            # Игнорирование строк, начинающихся с решётки («#»), и пустых строк
            if line == '' or '#' in line: continue

            # Формат файла: word (слово),sPoint (очки Сайори),nPoint (очки Нацуки),yPoint (очки Юри)
            x = line.split(',')

            full_wordlist[x[0]] = PoemWord(int(x[1]), int(x[2]), int(x[3]))

    # Для использования со словами во втором и третьем актах
    glitch_word = PoemWord(0, 0, 0, True)
    monika_word = PoemWord(0, 0, 0, False)

    # Этот класс управляет движениями чиби лучшим образом
    class ChibiTrans(object):
        def __init__(self):
            self.charTime = renpy.random.random() * 4 + 4
            self.charPos = 0
            self.charOffset = 0
            self.charZoom = 1

        def produce_random(self):
            return renpy.random.random() * 4 + 4

        def reset_trans(self):
            self.charTime = self.produce_random()
            self.charPos = 0
            self.charOffset = 0
            self.charZoom = 1

        def randomPauseTime(self, trans, st, at):
            if st > self.charTime:
                self.charTime = self.produce_random()
                return None
            return 0

        def randomMoveTime(self, trans, st, at):
            if st > .16:
                if self.charPos > 0:
                    self.charPos = renpy.random.randint(-1,0)
                elif self.charPos < 0:
                    self.charPos = renpy.random.randint(0,1)
                else:
                    self.charPos = renpy.random.randint(-1,1)
                if trans.xoffset * self.charPos > 5: self.charPos *= -1
                return None
            if self.charPos > 0:
                trans.xzoom = -1
            elif self.charPos < 0:
                trans.xzoom = 1
            trans.xoffset += .16 * 10 * self.charPos
            self.charOffset = trans.xoffset
            self.charZoom = trans.xzoom
            return 0
    
    # Этот словарь хранит всех персонажей в мини-игре и их количество очков.
    chibis = {}

    # Этот класс наследует ChibiTrans и используется для хранения данных об очках, набранных в мини-игре.
    class Chibi(ChibiTrans):
        POEM_DISLIKE_THRESHOLD = 29
        POEM_LIKE_THRESHOLD = 45

        def __init__(self, name):
            if not isinstance(name, str):
                raise Exception(f"Аргумент 'name' должен быть строкой, а не {type(name)}.")
                
            self.charPointTotal = 0
            self.appeal = 0
            super().__init__()
            chibis[name] = self

        def reset(self):
            self.charPointTotal = 0
            self.reset_trans()

        def add(self, point):
            self.charPointTotal += point

        def calculate_appeal(self):
            if self.charPointTotal < self.POEM_DISLIKE_THRESHOLD:
                return -1
            elif self.charPointTotal > self.POEM_LIKE_THRESHOLD:
                self.win = True
                return 1
            return 0

    seen_eyes_this_chapter = False

    # Объявление переменных чиби для трансформаций и очков (за исключением Моники; ей нужно только передвигаться).
    chibi_s = Chibi('sayori')
    chibi_n = Chibi('natsuki')
    chibi_m = ChibiTrans()
    chibi_y = Chibi('yuri')

    # Начало мини-игры под прослойкой Python
    def poem_game_start():
        played_baa = False
        poemgame_glitch = False

        # Сбрасывает очки у каждого персонажа
        for c in chibis:
            chibis[c].reset()

        # Создаёт копию заполненного словаря для дальнейшего редактирования.
        wordList = full_wordlist.copy()

        # Лучшая реализация цикла «пока», чем то, что было у Дэна
        progress = 1
        while progress <= 20:
            # В этом разделе отбирается 10 случайных слов и записывается в список.
            random_words = []
            for w in range(10):
                word = random.choice(list(wordList.keys()))
                random_words.append(word)
                # Удаляет слово, как только оное было выбрано и добавлено из локальной копии.
                del wordList[word]

            # Отображает мини-игру
            poemword = renpy.call_screen("poem_test", words=random_words, progress=progress, poemgame_glitch=poemgame_glitch)

            # Проверяет, что это слово есть в списке и не является уникальным для второго и третьего актов.
            if poemword in full_wordlist:
                t = full_wordlist[poemword]
            else:
                if persistent.playthrough == 2:
                    t = glitch_word
                else:
                    t = monika_word

            # Если мини-игра у нас сейчас не глючная, всё будет проходить как обычно, в противном случае должны начаться глюки
            if not poemgame_glitch:
                if t.glitch: # Это условие указывает, что должно произойти, когда было выбрано глючное слово.
                    poemgame_glitch = True
                    renpy.music.play(audio.t4g)
                    renpy.show("white")
                    renpy.show("y_sticker glitch", at_list=[sticker_glitch], zorder=10)
                elif persistent.playthrough != 3:
                    renpy.play(gui.activate_sound)
                    # Акт 1
                    if persistent.playthrough == 0:
                        if t.sPoint >= 3:
                            renpy.show("s_sticker hop")
                        if t.nPoint >= 3:
                            renpy.show("n_sticker hop")
                        if t.yPoint >= 3:
                            renpy.show("y_sticker hop")
                    else:
                        # Акт 2
                        if persistent.playthrough == 2 and chapter == 2 and random.randint(0,10) == 0: renpy.show("m_sticker hop") # Чиби Моники подпрыгнет с шансом 1/10.
                        elif t.nPoint > t.yPoint: renpy.show("n_sticker hop") # Поскольку во Втором акте остались Юри и Нацуки, та, чьё слово имеет больше очков, подпрыгнет.
                        elif persistent.playthrough == 2 and not persistent.seen_sticker and random.randint(0,100) == 0:
                            renpy.show("y_sticker hopg") # "y_sticker_2g.png". Если мы его ещё не видели, есть шанс 1/100 на то, чтобы его увидеть.
                            persistent.seen_sticker = True
                        elif persistent.playthrough == 2 and chapter == 2: renpy.show("y_sticker_cut hop") # Стикер Юри с порезанными руками.
                        else: renpy.show("y_sticker hop")
            else:
                r = random.randint(0, 10) # Шанс 1/10 на то, чтобы услышать «ба-а» при выборе слова.
                if r == 0 and not played_baa:
                    renpy.play("gui/sfx/baa.ogg")
                    played_baa = True
                elif r <= 5: renpy.play(gui.activate_sound_glitch)

            # Добавляет очки персонажам и увеличивает прогресс на 1.
            chibi_s.charPointTotal += t.sPoint
            chibi_n.charPointTotal += t.nPoint
            chibi_y.charPointTotal += t.yPoint
            progress += 1
    
    # Конец игры
    def poem_game_finish():
        # Акт 1
        if persistent.playthrough == 0:
            # В первой главе это добавляет 5 очков той девушке, на чью сторону мы встали.
            if chapter == 1:
                chibis[ch1_choice].charPointTotal += 5

            poemwinner[chapter] = max(chibis, key=lambda c: chibis[c].charPointTotal)
        else:
            # Акт 2
            if chibi_n.charPointTotal > chibi_y.charPointTotal: poemwinner[chapter] = "natsuki"
            else: poemwinner[chapter] = "yuri"

        # Добавляет очки признания, опираясь на то, кто набрал больше очков в мини-игре
        chibis[poemwinner[chapter]].appeal += 1

        # Устанавливает степень признания
        s_poemappeal[chapter] = chibi_s.calculate_appeal()
        n_poemappeal[chapter] = chibi_n.calculate_appeal()
        y_poemappeal[chapter] = chibi_y.calculate_appeal()

        # У победительницы значение признания всегда будет равно 1 (т.е. стих ей понравился).
        exec(f"{poemwinner[chapter][0]}_poemappeal[chapter] = 1")

screen poem_test(words, progress, poemgame_glitch):
    default numWords = 20
    
    if progress is not None:
        fixed:
            xpos 810
            
            python:
                if persistent.playthrough == 2 and chapter == 2:
                    pstring = ""
                    for i in range(progress):
                        pstring += "1"
                else:
                    pstring = str(progress)

            text f"{pstring}/{numWords}":
                style "poemgame_text"
                ypos 80

        # Две фиксированные зоны для двух разделов мини-игры, которые у нас есть
        fixed:
            xpos 440
            ypos 160

            viewport:
                has vbox
                spacing 56

                for i in range(5):
                    if persistent.playthrough == 3:
                        python:
                            s = list(__("Моника"))
                            for k in range(6): # Применяет различные искажения к словам "Моника".
                                if random.randint(0, 4) == 0:
                                    s[k] = ' '
                                elif random.randint(0, 4) == 0:
                                    s[k] = random.choice(nonunicode)
                            wordString = "".join(s)
                    elif persistent.playthrough == 2 and not poemgame_glitch and chapter >= 1 and progress < numWords and random.randint(0, 400) == 0:
                        python:
                            wordString = glitchtext(80) # Устанавливает небольшой шанс того, что случайное слово во Втором акте будет глючным.
                    else:
                        python:
                            wordString = words[i]

                    textbutton wordString:
                        action Return(wordString)
                        text_style "poemgame_text"

        fixed:
            xpos 680
            ypos 160

            viewport:
                has vbox
                spacing 56

                for i in range(5):
                    if persistent.playthrough == 3:
                        python:
                            s = list(__("Моника"))
                            for k in range(6): # Применяет различные искажения к словам "Моника".
                                if random.randint(0, 4) == 0:
                                    s[k] = ' '
                                elif random.randint(0, 4) == 0:
                                    s[k] = random.choice(nonunicode)
                            wordString = "".join(s)
                    elif persistent.playthrough == 2 and not poemgame_glitch and chapter >= 1 and progress < numWords and random.randint(0, 400) == 0:
                        python:
                            wordString = glitchtext(80) # Устанавливает небольшой шанс того, что случайное слово во Втором акте будет глючным.
                    else:
                        python:
                            wordString = words[5+i]

                    textbutton wordString:
                        action Return(wordString)
                        text_style "poemgame_text"

label poem(transition=True):
    stop music fadeout 2.0

    if persistent.playthrough == 3: # Если мы в режиме Только Моника, то нас перекинет на глючную тетрадь.
        scene bg notebook-glitch
    else:
        scene bg notebook

    if persistent.playthrough == 3: 
        show m_sticker at sticker_mid # Только Моника.
    else:
        if persistent.playthrough == 0:
            show s_sticker at sticker_left # Покажет чиби Сайори только в первом акте.
        show n_sticker at sticker_mid # Чиби Нацуки.
        if persistent.playthrough == 2 and chapter == 2:
            show y_sticker_cut at sticker_right # Заменяет чиби Юри на оный с "порезанными руками".
        else:
            show y_sticker at sticker_right # Чиби Юри.
        if persistent.playthrough == 2 and chapter == 2:
            show m_sticker at sticker_m_glitch # Чиби Моники.

    if transition:
        with dissolve_scene_full

    if persistent.playthrough == 3:
        play music ghostmenu # Изменяет музыку в режиме Только Моника.
    else:
        play music t4

    $ config.allow_skipping = False
    $ allow_skipping = False

    if persistent.playthrough == 0 and chapter == 0: # Показывает модальное окно при первом запуске мини-игры.
        call screen dialog(_p("""Пришло время написать стихотворение!

Выберите слова, которые, по-вашему, подойдут нравящейся вам девушке.
С той девушкой, которой больше всего понравится ваше стихотворение,
у вас может произойти что-то хорошее!"""), ok_action=Return())

    $ poem_game_start()
    $ poem_game_finish()

    # Вызывает новый лейбл со страшными глазами, если мы на Втором акте и ещё не видели их
    if persistent.playthrough == 2 and persistent.seen_eyes == None and renpy.random.randint(0,5) == 0:
        call poem_eye_scare

    $ config.allow_skipping = True
    $ allow_skipping = True

    stop music fadeout 2.0
    show black as fadeout:
        alpha 0
        linear 1.0 alpha 1.0
    pause 1.0
    return

## Код страшных глаз переехал в отдельный лейбл
label poem_eye_scare:
    $ seen_eyes_this_chapter = True
    $ quick_menu = False
    play sound "sfx/eyes.ogg"
    $ persistent.seen_eyes = True
    stop music
    scene black with None
    show bg eyes_move
    pause 1.2
    hide bg eyes_move
    show bg eyes
    pause 0.5
    hide bg eyes
    show bg eyes_move
    pause 1.25
    hide bg eyes with None
    $ quick_menu = True
    return

############ Определения изображений начинаются здесь. #############
image bg eyes_move:
    "images/bg/eyes.png"
    parallel:
        yoffset 720 ytile 2
        linear 0.5 yoffset 0
        repeat
    parallel:
        0.1
        choice:
            xoffset 20
            0.05
            xoffset 0
        choice:
            xoffset 0
        repeat
        
image bg eyes:
    "images/bg/eyes.png"

image s_sticker:
    "gui/poemgame/s_sticker_1.png"
    xoffset chibi_s.charOffset xzoom chibi_s.charZoom
    block:
        function chibi_s.randomPauseTime
        parallel:
            sticker_move_n
        parallel:
            function chibi_s.randomMoveTime
        repeat

image n_sticker:
    "gui/poemgame/n_sticker_1.png"
    xoffset chibi_n.charOffset xzoom chibi_n.charZoom
    block:
        function chibi_n.randomPauseTime
        parallel:
            sticker_move_n
        parallel:
            function chibi_n.randomMoveTime
        repeat

image y_sticker:
    "gui/poemgame/y_sticker_1.png"
    xoffset chibi_y.charOffset xzoom chibi_y.charZoom
    block:
        function chibi_y.randomPauseTime
        parallel:
            sticker_move_n
        parallel:
            function chibi_y.randomMoveTime
        repeat

image y_sticker_cut:
    "gui/poemgame/y_sticker_cut_1.png"
    xoffset chibi_y.charOffset xzoom chibi_y.charZoom
    block:
        function chibi_y.randomPauseTime
        parallel:
            sticker_move_n
        parallel:
            function chibi_y.randomMoveTime
        repeat

image m_sticker:
    "gui/poemgame/m_sticker_1.png"
    xoffset chibi_m.charOffset xzoom chibi_m.charZoom
    block:
        function chibi_m.randomPauseTime
        parallel:
            sticker_move_n
        parallel:
            function chibi_m.randomMoveTime
        repeat

image s_sticker hop:
    "gui/poemgame/s_sticker_2.png"
    xoffset chibi_s.charOffset xzoom chibi_s.charZoom
    sticker_hop
    xoffset 0 xzoom 1
    "s_sticker"

image n_sticker hop:
    "gui/poemgame/n_sticker_2.png"
    xoffset chibi_n.charOffset xzoom chibi_n.charZoom
    sticker_hop
    xoffset 0 xzoom 1
    "n_sticker"

image y_sticker hop:
    "gui/poemgame/y_sticker_2.png"
    xoffset chibi_y.charOffset xzoom chibi_y.charZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image y_sticker_cut hop:
    "gui/poemgame/y_sticker_cut_2.png"
    xoffset chibi_y.charOffset xzoom chibi_y.charZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker_cut"

image y_sticker hopg:
    "gui/poemgame/y_sticker_2g.png"
    xoffset chibi_y.charOffset xzoom chibi_y.charZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image m_sticker hop:
    "gui/poemgame/m_sticker_2.png"
    xoffset chibi_m.charOffset xzoom chibi_m.charZoom
    sticker_hop
    xoffset 0 xzoom 1
    "m_sticker"

image y_sticker glitch:
    "gui/poemgame/y_sticker_1_broken.png"
    xoffset chibi_y.charOffset xzoom chibi_y.charZoom zoom 3.0
    block:
        function chibi_y.randomPauseTime
        parallel:
            sticker_move_n
        parallel:
            function chibi_y.randomMoveTime
        repeat

transform sticker_left:
    xcenter 100 yalign 0.9 subpixel True

transform sticker_mid:
    xcenter 220 yalign 0.9 subpixel True

transform sticker_right:
    xcenter 340 yalign 0.9 subpixel True

transform sticker_glitch:
    xcenter 50 yalign 1.8 subpixel True

transform sticker_m_glitch:
    xcenter 100 yalign 1.35 subpixel True

transform sticker_move_n:
    easein_quad .08 yoffset -15
    easeout_quad .08 yoffset 0

transform sticker_hop:
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
