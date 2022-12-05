## poem_special.rpy

# В этом файле определены особые стихотворения, которые игрок может увидеть во время прохождения Второго акта игры.
# Игроку показываются только три таких стихотворения, которые были выбраны случайным образом во время исполнения
# конкретного цикла в файле «splash.rpy».
image poem_special1 = "poem_special/poem_special1.png" # Счхстлхвые мхсли
image poem_special2 = "poem_special/poem_special2.png" # Ты меня слышишь?
image poem_special3 = "poem_special/poem_special3.png" # Ничто не реально
image poem_special4 = "poem_special/poem_special4.png" # Воспоминания о порезе
image poem_special5: # Пристально смотри на точку/Я люблю тебя
    "poem_special/poem_special5a.png"
    10.0
    "poem_special/poem_special5b.png"
image poem_special6 = "poem_special/poem_special6.png" # Шутка
image poem_special7a = "poem_special/poem_special7a.png" # Искажённый спрайт Моники
image poem_special7b = "poem_special/poem_special7b.png" # Искажённый спрайт Моники 2
image poem_special8 = "poem_special/poem_special8.png" # Сон
image poem_special9 = "poem_special/poem_special9.png" # Что я люблю в папе
image poem_special10 = "poem_special/poem_special10.png" # Я не могу заставить себя сходить к психотерапевту
image poem_special11 = "poem_special/poem_special11.png" # Сон 2

# Это изображение, в зависимости от конкретного условия, показывает либо
# послание Моники, либо послание Дэна.
image poem_end = ConditionSwitch(
    "persistent.clearall == True", "poem_special/poem_end_clearall.png",
    "True", "poem_special/poem_end.png")

# Этот лейбл показывает особое стихотворение, которое игрок может увидеть во время
# прохождения модификации. 
# Чтобы показать такое стихотворение, используйте «call poem_special(X)», где X - номер 
# стихотворения в списке стихотворений выше.
label poem_special(poem=1):
    $ quick_menu = False
    play sound page_turn

    if poem == 7:
        show poem_special7a as ps with Dissolve(1.0)
    else:
        show expression f"poem_special{poem}" as ps with Dissolve(1.0)

    $ pause()

    if poem == 2:
        play sound "sfx/giggle.ogg"
    elif poem == 7:
        show poem_special7b as ps
        $ pause(0.01)

    $ quick_menu = True
    return

# Обратная совместимость
label poem_special_1:
    call poem_special(1)
    return
label poem_special_2:
    call poem_special(2)
    return
label poem_special_3:
    call poem_special(3)
    return
label poem_special_4:
    call poem_special(4)
    return
label poem_special_5:
    call poem_special(5)
    return
label poem_special_6:
    call poem_special(6)
    return
label poem_special_7:
    call poem_special(7)
    return
label poem_special_8:
    call poem_special(8)
    return
label poem_special_9:
    call poem_special(9)
    return
label poem_special_10:
    call poem_special(10)
    return
label poem_special_11:
    call poem_special(11)
    return