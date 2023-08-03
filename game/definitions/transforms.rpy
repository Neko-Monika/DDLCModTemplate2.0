## transforms.rpy

# В этом файле определены размещения и анимации в DDLC.

# Эта трансформация задаёт корректный размер спрайту персонажа в указанной позиции по горизонтали.
transform tcommon(x=640, z=0.80):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.03

transform tinstant(x=640, z=0.80):
    xcenter x yoffset 0 zoom z*1.00 alpha 1.00 yanchor 1.0 ypos 1.03

# Эта трансформация увеличивает спрайт персонажа, когда тот разговаривает.
transform focus(x=640, z=0.80):
    yanchor 1.0 ypos 1.03 subpixel True
    on show:
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.05 alpha 1.00
        yanchor 1.0 ypos 1.03
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.05
        parallel:
            easein .15 yoffset 0

# Эта трансформация немного опускает спрайт персонажа.
transform sink(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .5 ypos 1.06

# Эта трансформация заставляет спрайт персонажа подскочить.
transform hop(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0

# Эта трансформация делает фокус на спрайте персонажа и заставляет его подскочить одновременно.
transform hopfocus(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.05 alpha 1.00 subpixel True
    easein .1 yoffset -21
    easeout .1 yoffset 0

# Эта трансформация сначала опускает спрайт персонажа, а затем возвращает в исходное положение.
transform dip(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 yoffset 25
    easeout .25 yoffset 0

# Эта трансформация заставляет спрайт персонажа качаться на экране.
# Скорее всего, это остаточный код трансформации из DDLC на этапе разработки для сценки с Нацуки в кладовке.
transform panic(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    parallel:
        ease 1.2 yoffset 25
        ease 1.2 yoffset 0
        repeat
    parallel:
        easein .3 xoffset 20
        ease .6 xoffset -20
        easeout .3 xoffset 0
        repeat

# Эта трансформация заставляет спрайт персонажа "вылететь" (войти на сцену) слева.
transform leftin(x=640, z=0.80):
    xcenter -300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x

# Эта трансформация заставляет спрайт персонажа "вылететь" (войти на сцену) справа.
transform rightin(x=640, z=0.80):
    xcenter 2000 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x

# Эта трансформация убирает спрайт персонажа с экрана.
transform thide(z=0.80):
    subpixel True
    transform_anchor True
    on hide:
        easein .25 zoom z*0.95 alpha 0.00 yoffset -20

# Эта трансформация убирает спрайт персонажа, перемещая его влево.
transform lhide:
    subpixel True
    on hide:
        easeout .25 xcenter -300

# Эта трансформация убирает спрайт персонажа, перемещая его вправо.
transform rhide:
    subpixel True
    on hide:
        easeout .25 xcenter 2000

# Эти трансформации заставляют спрайты персонажей стоять неподвижно в заданном 
# положении с учётом того, сколько персонажей находится на экране и какой у них номер.
#     Пример размещения Моники между двумя другими девушками: t32
transform t41:
    tcommon(200)
transform t42:
    tcommon(493)
transform t43:
    tcommon(786)
transform t44:
    tcommon(1080)
transform t31:
    tcommon(240)
transform t32:
    tcommon(640)
transform t33:
    tcommon(1040)
transform t21:
    tcommon(400)
transform t22:
    tcommon(880)
transform t11:
    tcommon(640)

# Эти трансформации заставляют спрайты персонажей выскочить.
transform i41:
    tinstant(200)
transform i42:
    tinstant(493)
transform i43:
    tinstant(786)
transform i44:
    tinstant(1080)
transform i31:
    tinstant(240)
transform i32:
    tinstant(640)
transform i33:
    tinstant(1040)
transform i21:
    tinstant(400)
transform i22:
    tinstant(880)
transform i11:
    tinstant(640)

# Эти трансформации выделяют спрайт говорящего на экране.
transform f41:
    focus(200)
transform f42:
    focus(493)
transform f43:
    focus(786)
transform f44:
    focus(1080)
transform f31:
    focus(240)
transform f32:
    focus(640)
transform f33:
    focus(1040)
transform f21:
    focus(400)
transform f22:
    focus(880)
transform f11:
    focus(640)

# Эти трансформации заставляют спрайты персонажей поникнуть.
transform s41:
    sink(200)
transform s42:
    sink(493)
transform s43:
    sink(786)
transform s44:
    sink(1080)
transform s31:
    sink(240)
transform s32:
    sink(640)
transform s33:
    sink(1040)
transform s21:
    sink(400)
transform s22:
    sink(880)
transform s11:
    sink(640)

# Эти трансформации заставляют спрайты персонажей подскочить.
transform h41:
    hop(200)
transform h42:
    hop(493)
transform h43:
    hop(786)
transform h44:
    hop(1080)
transform h31:
    hop(240)
transform h32:
    hop(640)
transform h33:
    hop(1040)
transform h21:
    hop(400)
transform h22:
    hop(880)
transform h11:
    hop(640)

# Эти трансформации заставляют спрайты персонажей подскочить и быть выделенными среди остальных одновременно.
transform hf41:
    hopfocus(200)
transform hf42:
    hopfocus(493)
transform hf43:
    hopfocus(786)
transform hf44:
    hopfocus(1080)
transform hf31:
    hopfocus(240)
transform hf32:
    hopfocus(640)
transform hf33:
    hopfocus(1040)
transform hf21:
    hopfocus(400)
transform hf22:
    hopfocus(880)
transform hf11:
    hopfocus(640)

# Эти трансформации заставляют спрайты персонажей сначала опуститься вниз, а затем подняться обратно.
transform d41:
    dip(200)
transform d42:
    dip(493)
transform d43:
    dip(786)
transform d44:
    dip(1080)
transform d31:
    dip(240)
transform d32:
    dip(640)
transform d33:
    dip(1040)
transform d21:
    dip(400)
transform d22:
    dip(880)
transform d11:
    dip(640)

# Эти трансформации заставляют спрайты персонажей "вылететь" слева.
transform l41:
    leftin(200)
transform l42:
    leftin(493)
transform l43:
    leftin(786)
transform l44:
    leftin(1080)
transform l31:
    leftin(240)
transform l32:
    leftin(640)
transform l33:
    leftin(1040)
transform l21:
    leftin(400)
transform l22:
    leftin(880)
transform l11:
    leftin(640)

# Эти трансформации заставляют спрайты персонажей "вылететь" справа.
transform r41:
    rightin(200)
transform r42:
    rightin(493)
transform r43:
    rightin(786)
transform r44:
    rightin(1080)
transform r31:
    rightin(240)
transform r32:
    rightin(640)
transform r33:
    rightin(1040)
transform r21:
    rightin(400)
transform r22:
    rightin(880)
transform r11:
    rightin(640)

# Эта трансформация ставит голову спрайта персонажа прямо перед глазами игрока.
transform face(z=0.80, y=500):
    subpixel True
    xcenter 640
    yanchor 1.0 ypos 1.03
    yoffset y
    zoom z*2.00

# Эта трансформация выводит на экран/удаляет с экрана элементы сценки/саму сценку.
transform cgfade:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0

# Эта трансформация заставляет Нацуки во время показа сценки в кладовке трястись, когда та паникует.
transform n_cg2_wiggle:
    subpixel True
    xoffset 0
    easein 0.15 xoffset 20
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -15
    easeout 0.15 xoffset 0
    easein 0.15 xoffset 10
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -5
    ease 0.15 xoffset 0

# Эта трансформация воспроизводит эффект тряски каждую секунду.
transform n_cg2_wiggle_loop:
    n_cg2_wiggle
    1.0
    repeat

# Эта трансформация заставляет Нацуки полететь прямо в экран во время показа сценки в кладовке.
transform n_cg2_zoom:
    subpixel True
    truecenter
    xoffset 0
    easeout 0.20 zoom 2.5 xoffset 200

# Эта переменная определяет эффект растворения ('dissolve'), используемый персонажами.
define dissolve = Dissolve(0.25)

# Эти переменные определяют эффект растворения для сценок и обычных сцен.
define dissolve_cg = Dissolve(0.75)
define dissolve_scene = Dissolve(1.0)

# Эта переменная определяет эффект, при котором экран сначала становится чёрным, а затем появляется другая сцена.
define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

# Эта переменная определяет эффект, при котором сцена на экране растворяется и сменяется другой.
define dissolve_scene_half = MultipleTransition([
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

# Эта переменная определяет эффект, при котором экран плавно становится чёрным; как будто игрок закрывает глаза.
define close_eyes = MultipleTransition([
    False, Dissolve(0.5),
    Solid("#000"), Pause(0.25),
    True])

# Эта переменная определяет эффект, при котором экран плавно проявляется; как будто игрок открывает глаза.
define open_eyes = MultipleTransition([
    False, Dissolve(0.5),
    True])

# Эта переменная определяет эффект, при котором экран мгновенно сменяется чернотой.
define trueblack = MultipleTransition([
    Solid("#000"), Pause(0.25),
    Solid("#000")
    ])

# Эта переменная определяет эффект, при котором спрайт персонажа "стирается" слева направо.
define wipeleft = ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64)

# Эта переменная определяет эффект, при котором текущая сцена "стирается" слева направо, а затем, точно так же, появляется другая сцена.
define wipeleft_scene = MultipleTransition([
    False, ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
    True])

# Эта переменная определяет эффект, при котором спрайт персонажа "стирается" справа налево.
define wiperight = ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64, reverse=True)

# Эта переменная определяет эффект, при котором текущая сцена "стирается" справа налево, а затем, точно так же, появляется другая сцена.
define wiperight_scene = MultipleTransition([
    False, ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64, reverse=True),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64, reverse=True),
    True])

# Эта переменная, скорее всего, является остатками наработок по DDLC.
# Она ставит игру на паузу на .25 секунд.
define tpause = Pause(0.25)

# Это изображение с трансформациями проигрывает анимацию белого шума.
image noise:
    truecenter
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    xzoom -1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    yzoom -1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    xzoom 1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    yzoom 1
    repeat

# Эта трансформация заставляет эффект белого шума отображаться с 25%-ной непрозрачностью.
transform noise_alpha:
    alpha 0.25

# Эта трансформация заставляет эффект белого шума появиться на мгновение и исчезнуть.
transform noisefade(t=0):
    alpha 0.0
    t
    linear 5.0 alpha 0.40

# Это изображение добавляет виньетку для соответствующего эффекта.
image vignette:
    truecenter
    "images/bg/vignette.png"

# Эта трансформация заставляет виньетку проявиться плавно.
transform vignettefade(t=0):
    alpha 0.0
    t
    linear 25.0 alpha 1.00

# Эта трансформация заставляет виньетку моргать.
transform vignetteflicker(t=0):
    alpha 0.0
    t + 2.030
    parallel:
        alpha 1.00
        linear 0.2 alpha 0.8
        0.1
        alpha 0.7
        linear 0.1 alpha 1.00
        alpha 0.0
        1.19
        repeat
    parallel:
        easeout 20 zoom 3.0

# Эта трансформация заставляет экранный слой моргать.
transform layerflicker(t=0):
    truecenter
    t + 2.030
    parallel:
        zoom 1.05
        linear 0.2 zoom 1.04
        0.1
        zoom 1.035
        linear 0.1 zoom 1.05
        zoom 1.0
        1.19
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.6
        easeout_bounce 0.3 xalign 0.4
        repeat

# Эта трансформация создаёт эффект перемотки, который можно быть увидеть во Втором акте.
transform rewind:
    truecenter
    zoom 1.20
    parallel:
        easeout_bounce 0.2 xalign 0.55
        easeout_bounce 0.2 xalign 0.45
        repeat
    parallel:
        easeout_bounce 0.33 yalign 0.55
        easeout_bounce 0.33 yalign 0.45
        repeat

# Эти трансформации применяют эффект сердцебиения к экрану, который можно
# было увидеть случайным образом во время прохождения DDLC.
transform heartbeat:
    heartbeat2(1)

transform heartbeat2(m):
    truecenter
    parallel:
        0.144
        zoom 1.00 + 0.07 * m
        easein 0.250 zoom 1.00 + 0.04 * m
        easeout 0.269 zoom 1.00 + 0.07 * m
        zoom 1.00
        1.479
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.5 + 0.02 * m
        easeout_bounce 0.3 xalign 0.5 - 0.02 * m
        repeat

# Эти трансформация и функция управляют движением глаз Юри во время Второго акта.
transform yuripupils_move:
    function yuripupils_function

init python:
    def yuripupils_function(trans, st, at):
        trans.xoffset = -1 + random.random() * 9 - 4
        trans.yoffset = 3 + random.random() * 6 - 3
        return random.random() * 1.2 + 0.3

# Эта трансформация выводит персонажа поверх остальных с постепенно 
# увеличивающейся непрозрачностью во Втором акте.
transform malpha(a=1.00):
    i11
    alpha a
