#!/usr/bin/python3
# Created by F1neg4n

import os

def welcome():
    welc = 'SSH Connect'
    info = '[INFO] Python script to create SSH connections'
    os.system('clear')
    print(welc + '\n' + '*' * len(welc))
    print(info + '\n' + '-' * len(info))
    return

def getAddress():
    welcome()
    try:
        ipAddress = input('[+] Enter the IP Address: ')
        while(ipAddress == ''):
            ipAddress = input('[+] Please, enter the IP Address: ')
    except(KeyboardInterrupt):
        os.system('clear')
        welcome()
        print('[-] Interrupted by user!')
        exit()
    return ipAddress

def getUser():
    try:
        user = input('[+] User: ')
        while(user == ''):
            user = input('[+] Please, enter the user: ')
    except(KeyboardInterrupt):
        os.system('clear')
        welcome()
        print('[!] Interrupted by user')
        exit()
    return user

def newConnection():
    ipAddress = getAddress()
    user = getUser()
    try:
        welcome()
        print('[+] Creating new SSH connection...')
        print('[+] Connecting to ' + user + '@' + ipAddress + '...')
        print('----')
        os.system('ssh -p 22 ' + user + '@' + ipAddress)
    except(KeyboardInterrupt):
        os.system('clear')
        welcome()
        print('[!] Interrupted by user')
        exit()
    return

if __name__ == '__main__':
    newConnection()
