@echo off
TITLE Aurora
:: Enables virtual env mode and then starts Aurora
env\scripts\activate.bat && py -m Aurora
