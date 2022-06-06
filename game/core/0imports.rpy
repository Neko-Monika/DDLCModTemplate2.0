
# __imports__.rpy
# В этом файле импортируются конкретные модули Python, необходимые для DDLC
# и функционирования шаблона, во время запуска игры.

python early:
    # Для Достижений и Галереи
    import math 

    # Для титров
    import datetime

    # Для глитч-текста
    import random

    # Для вступительной заставки
    import re
    import os

    # Для Синего экрана смерти
    import subprocess
    import platform

    # Для Галереи
    import threading
    import renpy.display.image as imgcore

init -19 python:
    # Игровая активность в Дискорде отключена по умолчанию.
    # Для её включения измените значение нижеуказанной переменной на True.
    # Если вы используете Автоматическую перезагрузку (Shift+R), рекомендуется оставить значение переменной как есть.
    persistent.enable_discord = False
    # Для Игровой активности в Дискорде
    if persistent.enable_discord:
        from discord_rpc import DiscordRPC
        from pypresence import DiscordNotFound
        try:
            RPC = DiscordRPC("979471077187125248")
        except DiscordNotFound: pass
