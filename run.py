#!/usr/bin/env python3.8
# before running the program on terminal Type: chmod +x run.py to gain access

from password import Cridential,User
import random
import string

# User-----------------------------------------
# 1. Creating created_user_password details
def save_user(login):
    """
    Function to save created_username created_user_password details
    """
    login.save_password()


# Cridentials----------------------------------------------------
# 1. Creating an account 
def create_password(account,username,password):
    '''
    Function to create a new Account
    '''
    new_password = Cridential(account,username,password)
    return new_password

# 1. Save the account
def save_password(account):
    '''
    Function to save Account
    '''
    account.save_password()


# 3. Delete account
def del_password(account):
    '''
    Function to delete an account
    '''
    account.delete_password()

# 4. Finding account
def find_account(account):
    '''
    Function that finds password by account and returns the account
    '''
    return Cridential.find_by_account(account)


# Check if an account exists
def check_existing_password(account):
    """
    Function that returs all the accounts
    """
    return Cridential.password_exists(account)

# Display all password and account
def display_password():
    """
    Function returns all accounts and their passwords
    """
    return Cridential.display_all_passwords()

