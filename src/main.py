import pandas as pd
import numpy as np

def load_whatsapp():
    wa = pd.read_csv("../resources/whatsappCSV.csv", sep=',', header=0, usecols=["No.", "Time", "Source", "Destination", "Protocol", "Length", "Info"])
    print(wa.head())

def load_telegram():
    tg = pd.read_csv("../resources/telegramCSV.csv", sep=',', header=0, usecols=["No.", "Time", "Source", "Destination", "Protocol", "Length", "Info"])
    print(tg.head())


def main():
    # ------------ WhatsApp analysis ------------------
    wa = load_whatsapp()

    # ------------ Telegram analysis ------------------
    tg = load_telegram()


if __name__ == '__main__':
    main()