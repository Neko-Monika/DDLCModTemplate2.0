
# 0imports.rpy
# В этом файле импортируются конкретные модули Python, необходимые для DDLC
# и функционирования шаблона, во время запуска игры.
# Примечание переводчика: файл был переименован, т.к. линтер Ренпая подчёркивал
# здесь всё красной волнистой линией из-за того, что название начиналось с "__"

python early:
    # Для Достижений и Галереи
    import math 

    # Для титров
    import datetime

    # Для глитч-текста
    import random

    # Для вступительной заставки
    import re, os

    # Для Синего экрана смерти
    import subprocess, platform

    # Для Галереи
    import threading
    import renpy.display.image as imgcore

    # Перенесено из lockdown_check.rpy, т.к. в definitions.rpy используются f-string
    # и он компилируется раньше первого, из-за чего появляется ошибка
    # "Обработка сценария завершилась неудачно.", которая вгоняет в ступор
    # мододелов-новичков; проверяем, запущен ли мод-шаблон на Ren'Py 8

    if renpy.version_tuple < (8, 0, 0, 22062402):
        raise NotRenPyEight

# Игровая активность Discord будет включена *только* при том условии, если мод
# запущен на Windows, Linux или macOS - прим. пер.
default -20 persistent.enable_discord = renpy.variant("pc")

init -19 python:
    # Для Игровой активности в Discord
    if persistent.enable_discord:
        from discord_rpc import DiscordRPC
        try:
            RPC = DiscordRPC("979471077187125248")
        except DiscordNotFound:
            persistent.enable_discord = False
