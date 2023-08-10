import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def menu():
    answer = '0'
    while answer != '5':
        answer = input("Please select which Whatsapp Group you want to analyze:\n"
                       "1 - Mostly messages\n"
                       "2 - Mostly Images\n"
                       "3 - Mostly Audio\n"
                       "4 - Mostly videos and files\n"
                       "5 - Exit\n")
        if answer != '1' and answer != '2' and answer != '3' and answer != '4' and answer != '5':
            print("Invalid value. Please enter a valid number\n")
        elif answer == '5':
            break
        else:
            df = load_csv(answer)
            plot_activity_trends(df)
    print("Goodbye!!")


def load_csv(number):
    path = '0'
    if number == '1':
        path = "../resources/whatsappMessagesCSV.csv"
        print("---------Messages----------")
    elif number == '2':
        path = "../resources/whatsappImagesCSV.csv"
        print("---------Images----------")
    elif number == '3':
        path = "../resources/whatsappAudioCSV.csv"
        print("---------Audio----------")
    elif number == '4':
        path = "../resources/whatsappVideosAndFilesCSV.csv"
        print("---------Videos and Files----------")

    df = pd.read_csv(path, sep=',', header=0,
                     usecols=["No.", "Time", "Source", "Destination", "Protocol", "Length", "Info"])
    reformat_columns(df)
    add_delays(df)
    add_lengths(df)
    print(df.head())
    return df


def add_delays(df: pd.DataFrame):
    df["Time_delay"] = df["Time"].diff().fillna(0)


def add_lengths(df: pd.DataFrame):
    df["Length_diff"] = df["Length"].diff().fillna(0)


def reformat_columns(df: pd.DataFrame):
    df["No."] = df["No."].astype(float)
    df["Time"] = df["Time"].astype(float)
    df["Length"] = df["Length"].astype(float)


def plot_activity_trends(df):
    # Plot the message count over time using a line chart
    plt.figure(figsize=(10, 6))
    plt.plot(df["Time_delay"], df["Length_diff"], marker='o', linestyle='-')
    plt.xlabel("Time_delay")
    plt.ylabel("Length_diff")
    plt.title("Message Count and Activity Trends")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Get the absolute path of the "res" directory
    res_directory = os.path.join(os.getcwd(), "res")

    # Create the "res" directory if it doesn't exist
    if not os.path.exists(res_directory):
        os.makedirs(res_directory)

    # Save the plot to the "res" directory with a new image file name
    image_path = os.path.join(res_directory, "new_plot.png")
    plt.savefig(image_path)

    # Show the plot
    plt.show()


if __name__ == '__main__':
    menu()
