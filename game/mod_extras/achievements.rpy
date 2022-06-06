## Авторское право 2019-2022 Азариэль Дель Кармен (GanstaKingofSA). Все права защищены.

## achievements.rpy
# Данный файл содержит код меню достижений и уведомления,
# отображающего прогресс прохождения модификации.

init python:
    achievementList = {}
    selectedAchievement = None

    # Этот класс определяет код для создания достижения.
    # Синтаксис:
    # name - Эта переменная содержит читабельное название достижения.
    # description - Эта переменная содержит читабельное описание достижения.
    # image - Эта переменная содержит путь или тег изображения достижения.
    # persistent - Эта переменная содержит название внутриигровой переменной для
    #              проверки факта получения достижения.
    # count - Эта переменная проверяет, требует ли достижение искомое число для получения.
    # maxCount - Эта переменная хранит максимальное число (maxCount), которое нужно набрать
    #            для получения достижения.
    class Achievements:

        def __init__(self, name, description, image, persistent, count=False, maxCount=100):
            global achievementList

            # Читабельное название достижения.
            self.name = name

            # Описание достижения.
            self.description = description

            # Тег изображения или путь к оному для иллюстрации достижения.
            self.image = image

            # Тег изображения или путь к оному для иллюстрации достижения, если
            # достижение не получено.
            self.locked = im.MatrixColor(image, im.matrix.desaturate())

            # Условие, которое указывает, требуется ли установленное число для получения достижения.
            self.count = count

            # Название переменной для проверки соответствия текущего прогресса требуемому переменной maxCount.
            self.persistent = persistent

            # Максимальное число предметов, которое надо собрать пользователю для получения достижения.
            self.maxCount = maxCount

            achievementList[self.name] = self

    # В этом разделе объявляются достижения. См. класс «Achievements»
    # для объявления своих достижений.
    startup = Achievements(_("Добро пожаловать в DDLC!"), _("Спасибо за принятие условий Отказа от ответственности."),
            "gui/logo.png", "persistent.first_run")

## Экран достижений ################################################################
##
## Этот экран используется для создания галереи доступных в модификации достижений,
## которую можно просмотреть в главном меню.
##
## Синтаксис:
## al.image - Эта переменная содержит путь или тег изображения достижения.
## al.locked - Эта переменная содержит изображение неполученного достижения.
## al.persistent - Эта переменная содержит название внутриигровой переменной 
##                 для проверки факта получения достижения.
## al.maxCount - Эта переменная содержит число, которое необходимо набрать для получения
##               достижения.
## gl.description - Эта переменная содержит описание достижения.
screen achievements():

    tag menu
    style_prefix "achievements"

    use game_menu(_("Награды")):

        fixed:
            # Этот vbox отвечает за отображение достижения над списком всех 
            # доступных достижений для отображения информации о выбранном достижении.
            vbox:
                xpos 0.26
                ypos -0.1

                hbox:

                    if selectedAchievement:

                        python:
                            currentVal = eval(selectedAchievement.persistent)

                            if not currentVal:
                                currentVal = False

                        if selectedAchievement.count:
                            add ConditionSwitch(
                                    currentVal >= selectedAchievement.maxCount, selectedAchievement.image, "True",
                                    selectedAchievement.locked) at achievement_scaler(128)
                        else:
                            add ConditionSwitch(
                                    currentVal, selectedAchievement.image, "True",
                                    selectedAchievement.locked) at achievement_scaler(128)
                    else:
                        null height 128

                    spacing 20

                    vbox:
                        xsize 400
                        ypos 0.2

                        if selectedAchievement:

                            text selectedAchievement.name:
                                font gui.name_font
                                color "#fff"
                                outlines [(2, "#505050", 0, 0)]

                            if selectedAchievement.count:
                                text "[selectedAchievement.description!t] ([currentVal] / [selectedAchievement.maxCount])"
                            else:
                                text "[selectedAchievement.description!t]"
                        else:
                            null height 128

            # Этот vpgrid отвечает за список достижений в игре.
            vpgrid:
                id "avp"
                rows math.ceil(len(achievementList) / 6.0)
                if len(achievementList) > 6: 
                    cols 6
                else: 
                    cols len(achievementList)

                spacing 25
                mousewheel True

                xalign 0.5
                yalign 0.85
                ysize 410

                for name, al in achievementList.items():

                    python:
                        currentVal = eval(al.persistent)

                        if not currentVal:
                            currentVal = False

                    if al.count:

                        imagebutton:
                            idle Transform(ConditionSwitch(
                                    currentVal >= al.maxCount, al.image, "True",
                                    al.locked), size=(128,128))
                            action SetVariable("selectedAchievement", al)
                    else:
                        imagebutton:
                            idle Transform(ConditionSwitch(
                                    currentVal, al.image, "True",
                                    al.locked), size=(128,128))
                            action SetVariable("selectedAchievement", al)

            vbar value YScrollValue("avp") xalign 1.01 ypos 0.2 ysize 400

        textbutton "?":
            style "return_button"
            xpos 0.99 ypos 1.1
            action ShowMenu("dialog", _p("""{b}Справка{/b}
Серые значки означают, что это достижение ещё не получено.
Продолжайте своё прохождение «[config.name]», чтобы открыть все доступные достижения."""), ok_action=Hide("dialog"))

        if config.developer:
            textbutton "Тест увед.":
                style "return_button"
                xpos 0.8 ypos 1.1
                action [Show("achievement_notify", reward=startup), With(Dissolve(1.0))]

## Экран уведомления достижений ###########################################################
##
## Этот экран используется для уведомления пользователя о полученном достижении.
##
## Синтаксис:
## reward.image - Эта переменная содержит путь или тег изображения достижения.
## reward.name - Эта переменная содержит читабельное название достижения.
## 
## Для вызова этого экрана используйте «show screen achievement_notify(X)», где X - само достижение.
## Обязательно настройте переменную, привязанную к нему, иначе достижение будет отображаться как неполученное.
screen achievement_notify(reward):

    style_prefix "achievements"

    frame at achievement_notif_transition:
        xsize 300
        ysize 100
        xpos 0.4

        hbox:
            xalign 0.27
            yalign 0.5
            add reward.image at achievement_scaler(50)
            spacing 20
            vbox:
                spacing 5
                text _("Достижение разблокировано!") size 16
                text reward.name size 14

    timer 5.0 action [Hide("achievement_notify"), With(Dissolve(1.0))]

style achievements_text is gui_text
style achievements_text:
    color "#000"
    outlines []
    size 20

transform achievement_scaler(x):
    xysize(x, x)

transform achievement_notif_transition:
    alpha 0.0
    linear 0.5 alpha 1.0

style achievements_image_button:
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound
