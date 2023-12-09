# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import whisper


def convert_audio(filepath):
    model = whisper.load_model("base")
    result = model.transcribe(filepath, language="pt", fp16=False, verbose=True)
    print(f' The text in video: \n {result["text"]}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    convert_audio("~/Video/polito/21_11_2023.mp4")
    print("### Done ###")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
