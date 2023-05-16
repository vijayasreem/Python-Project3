#!/usr/bin/env python3
# main.py
import sb_conf as conf
import importlib.util
import sb_etc as etc
import sb_acc as accounts
from sb_dbm import DBHandler as db

# Verbose
Debug = True

configPath = "Config.json"
defaultConfig = {
    "host": "localhost",
    "user" : "root",
    "password" : "",
    "port" : "3306",
    "database" : "simplebank" }

# Entry point
if __name__ == '__main__':
    if importlib.util.find_spec('pyfiglet'): from pyfiglet import figlet_format as fig; print(fig("SimpleBank"))
    print("Starting SimpleBank...\n")
    Config = conf.Read(configPath, defaultConfig)
    db.Setup(Config)
    db.Initialize()
    account = accounts.Account("Firstname Lastname", accounts.Gender.MALE, 20)
    card = accounts.Card(account)
    db.CheckDatabase(Config)
