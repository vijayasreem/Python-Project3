#!/usr/bin/env python3
# main.py

import sb_conf as conf
import sb_dbm as db


configPath = "Config.json"
defaultConfig = {
    "host": "localhost",
    "user" : "root",
    "password" : "",
    "database" : "simplebank" }

if __name__ == '__main__':
    Config = conf.Read(configPath, defaultConfig)
    Database = db.CreateConnection(
        Config['host',
               Config['user',
                      Config['password'],Config['database']]])

    print(Config)
