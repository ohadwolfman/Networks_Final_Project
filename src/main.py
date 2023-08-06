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
            print("Please enter a valid value\n")
        elif answer == '5':
            break
        else:
            load_csv(answer)
    print("Goodbye!!")


def load_csv(number):
    path = '0'
    if number == '1':
        path = "../resources/whatsappMessagesCSV.csv"
        print("---------messages----------")
    elif number == '2':
        path = "../resources/whatsappImagesCSV.csv"
        print("---------Images----------")
    elif number == '3':
        path = "../resources/whatsappAudioCSV.csv"
        print("---------audio----------")
    elif number == '4':
        path = "../resources/whatsappVideosAndFilesCSV.csv"
        print("---------videos_and_files----------")

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
    # Convert the "Time" column to datetime format (if not already in datetime format)
    df["Time"] = pd.to_datetime(df["Time"])

    # Group the data by time intervals (e.g., hours, days, etc.) and count the messages in each interval
    # For example, here we're using "D" to group by day, you can change it to "H" for hourly analysis.
    message_count = df.resample("D", on="Time")["No."].count()

    # Plot the message count over time using a line chart
    plt.figure(figsize=(10, 6))
    plt.plot(message_count.index, message_count.values, marker='o', linestyle='-')
    plt.xlabel("Date")
    plt.ylabel("Message Count")
    plt.title("Message Count and Activity Trends")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    menu()


if __name__ == '__main__':
    main()
