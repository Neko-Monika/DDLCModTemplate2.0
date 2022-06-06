
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


default -20 persistent.enable_discord = True

init -19 python:
    # Для Игровой активности в Discord
    if persistent.enable_discord:
        from discord_rpc import DiscordRPC
        RPC = DiscordRPC("979471077187125248")
