## Авторское право 2019-2023 Азариэль Дель Кармен (GanstaKingofSA). Все права защищены.

## achievements.rpy
# Данный файл содержит код меню достижений и уведомления,
# отображающего прогресс прохождения модификации.

default persistent.achievements = {}

init -1 python in achievements:
    from store import persistent, im
    achievementList = {}

    # Этот класс определяет код для создания достижения (без счётчика).
    # Синтаксис:
    # name - Эта переменная содержит читабельное название достижения.
    # description - Эта переменная содержит читабельное описание достижения.
    # image - Эта переменная содержит путь или тег изображения достижения.
    # locked_desc - Эта переменная содержит читабельное описание неоткрытого достижения.
    # show_desc_while_locked - Эта переменная указывает, какое из описаний достижения
    #                          показывать: настоящее или для неоткрытого.
    #
    # Для разблокировки достижения пропишите `$ X.unlock()` (без знаков `; где X - название переменной вашего достижения).
    class Achievement(object):

        def __init__(self, name, description, image, locked_desc="???", show_desc_while_locked=False):
            # Читабельное название достижения.
            self.name = name

            # Описание достижения.
            self.description = description

            # Тег изображения или путь к оному для иллюстрации достижения.
            self.image = image

            # Тег изображения или путь к оному для иллюстрации достижения, если
            # достижение не получено.
            self.locked = im.MatrixColor(image, im.matrix.desaturate())
            self.locked_desc = locked_desc

            self.show_desc_while_locked = show_desc_while_locked

            if self.name not in persistent.achievements:
                persistent.achievements[self.name] = {
                    "unlocked": False,
                    "current_count": 0,
                }

            self.unlocked = persistent.achievements[self.name]['unlocked']

            achievementList[self.name] = self
        
        def unlock(self):
            self.unlocked = True
            persistent.achievements[self.name]['unlocked'] = True
            renpy.show_screen("achievement_notify", self)
    
    # Этот класс определяет код для создания достижения (без счётчика).
    # У этого класса тот же синтаксис, что и у класса Achievement, но с 1 дополнительным аргументом.
    # Назначение остальных аргументов см. в классе Achievement.
    # Синтаксис:
    # max_count - Итоговое количество, необходимое для открытия достижения.
    class AchievementCount(Achievement):
        def __init__(self, name, description, image, show_desc_while_locked=False, max_count=100):
            Achievement.__init__(self, name, description, image, show_desc_while_locked)

            self.current_count = persistent.achievements[self.name]['current_count']
            self.max_count = max_count

        def increase_count(self):
            self.current_count += 1
            persistent.achievements[self.name]['current_count'] += 1
            if self.current_count == self.max_count:
                self.unlock()

init python:
    selectedAchievement = None
    # В этом разделе объявляются достижения. См. класс Achievements
    # для объявления своих достижений.
    startup = Achievement(_("Добро пожаловать в DDLC!"), _("Спасибо за принятие условий Отказа от ответственности."),
            "gui/logo.png")
    steam = Achievement(_("Steam"), _("Пользователь Steam."),
            "gui/logo.png")
    lets_count = AchievementCount(_("Считалочка"), _("1-3"),
            "gui/logo.png", max_count=3)

    # Быстрая сортировка (НЕ УДАЛЯТЬ)
    achievementList = {k: achievementList[k] for k in sorted(achievementList)}

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

                        add ConditionSwitch(
                                selectedAchievement.unlocked, selectedAchievement.image, "True",
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

                            if not selectedAchievement.unlocked and not selectedAchievement.show_desc_while_locked:
                                if isinstance(selectedAchievement, AchievementCount):
                                    text "[selectedAchievement.locked_desc!t] ([selectedAchievement.current_count] / [selectedAchievement.max_count])"
                                else:
                                    text selectedAchievement.locked_desc
                            else:
                                if isinstance(selectedAchievement, AchievementCount):
                                    text "[selectedAchievement.description!t] ([selectedAchievement.current_count] / [selectedAchievement.max_count])"
                                else:
                                    text selectedAchievement.description
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

                    imagebutton:
                        idle Transform(ConditionSwitch(
                                al.unlocked, al.image, "True",
                                al.locked), size=(128,128))
                        action SetVariable("selectedAchievement", al)

            vbar value YScrollValue("avp") xalign 1.01 ypos 0.2 ysize 400

        textbutton "?":
            style "return_button"
            xpos 0.99 ypos 1.1
            action Show("dialog", _p("""{b}Справка{/b}
Серые значки означают, что это достижение ещё не получено.
Продолжайте своё прохождение «[config.name!t]», чтобы открыть все доступные достижения."""), ok_action=Hide("dialog"))

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
        ysize 90
        xpos 0.4

        hbox:
            xalign 0.27
            yalign 0.5
            add reward.image at achievement_scaler(50)
            spacing 20
            vbox:
                spacing 5
                text _("Достижение разблокировано!") size 16
                text "[reward.name!t]" size 14

    timer 4.0 action [Hide("achievement_notify"), With(Dissolve(1.0))]

style achievements_text is gui_text
style achievements_text:
    color "#000"
    outlines []
    size 20

transform achievement_scaler(x):
    size(x, x)

transform achievement_notif_transition:
    alpha 0.0
    linear 0.5 alpha 1.0

style achievements_image_button:
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound
