## Авторское право 2019-2024 Азариэль Дель Кармен (bronya_rand). Все права защищены.
## Рефакторинг: Amanda Watson

## pronouns.rpy
# В этом файле спрашивают предпочтительные местоимения игрока.

init python:
    def male_tag(tag, argument):
        if persistent.male:
            return [(renpy.TEXT_TEXT, argument)]
        else:
            return [(renpy.TEXT_TEXT, "")]

    def female_tag(tag, argument):
        if not persistent.male:
            return [(renpy.TEXT_TEXT, argument)]
        else:
            return [(renpy.TEXT_TEXT, "")]

    config.self_closing_custom_text_tags["M"] = male_tag
    config.self_closing_custom_text_tags["F"] = female_tag

label pronouns_test:
    menu:
        "Я мальчик":
            $ persistent.male = True
        "Я девочка":
            $ persistent.male = False

    "{M=Путешественник}{F=Путешественница}, ты {M=принёс}{F=принесла} доски?"

    return
