import os
import zipfile
print("Welcome to the SCR-Autopilot installer for Windows.")
print("This script will:\n- Download scr-autopilot/scr-autopilot from GitHub\n- Download and run Tesseract-OCR installer\n- Download and run AutoHotKey installer\n- Download all required modules for SCR-Autopilot")
proceed = input("\nDo you wish to proceed? (Y/n) ")
if proceed == "n":
    print("canceled")
    exit()
print("Getting requests module...")
os.system("py -m pip install requests")
print("Downloading SCR-Autopilot repository...")
import requests
url = "https://github.com/scr-autopilot/scr-autopilot/archive/refs/heads/main.zip"
r = requests.get(url)
open("scr-autopilot-main.zip", "wb").write(r.content)
with zipfile.ZipFile("./scr-autopilot-main.zip", 'r') as zip_ref:
    zip_ref.extractall("./scr-autopilot")
print("\nDownloading Tesseract-OCR...")
url = "https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v5.0.0-alpha.20201127.exe"
r = requests.get(url)
open("tesseract-ocr-w32-setup-v5.0.0-alpha.20201127.exe", "wb").write(r.content)
print("Download successful.")
input("Setup for Tesseract-OCR will now open. Keep everything in the setup default!\nPress enter to acknowledge.")
os.startfile("tesseract-ocr-w32-setup-v5.0.0-alpha.20201127.exe")
input("\nAfter done with Tesseract-OCR setup, press enter.")
print("Downloading AHK...")
url = "https://github.com/Lexikos/AutoHotkey_L/releases/download/v1.1.33.10/AutoHotkey_1.1.33.10_setup.exe"
r = requests.get(url)
open("AutoHotkey_1.1.33.10_setup.exe", "wb").write(r.content)
print("Download successful.")
input("Setup for AHK will now open. Select Express Installation in the setup.\nPress enter to acknowledge.")
os.startfile("AutoHotkey_1.1.33.10_setup.exe")
input("\nAfter done with AHK setup, press enter.")
print("Deleting setup files...")
os.remove("tesseract-ocr-w32-setup-v5.0.0-alpha.20201127.exe")
os.remove("AutoHotkey_1.1.33.10_setup.exe")
os.remove("scr-autopilot-main.zip")
print("Setup files removed.")
print("Getting all required modules for SCR-Autopilot...")
os.system("py -m pip install opencv_python requests PyDirectInput ahk Flask numpy pytesseract Pillow pywin32")
input("\n\nSCR-AUTOPILOT WAS SUCCESSFULLY INSTALLED! Press enter to exit.")
