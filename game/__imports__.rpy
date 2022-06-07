
# __imports__.rpy
# В этом файле импортируются конкретные модули Python, необходимые для DDLC
# и функционирования шаблона, во время запуска игры.

python early:
    # Для Достижений и Галереи
    import math 
    from collections import OrderedDict 

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
