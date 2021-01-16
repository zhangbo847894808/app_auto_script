import os, pytest


def generate_report():
    os.system('allure ' + 'generate' + './report ' + ' - o ' + './report/html ' + '–clean')
