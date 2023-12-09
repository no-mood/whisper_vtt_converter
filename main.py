import datetime
import whisper
import sys

def convert_audio(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path, language="en", fp16=False, verbose=True)


    save_target = file_path + '.vtt'
    with open(save_target, "w") as file:
        file.write('WEBVTT' + '\n' + '\n')
        for index, segment in enumerate(result['segments']):
            file.write(str(index + 1) + '\n')

            start = format_delta_time(segment['start'])
            end = format_delta_time(segment['end'])

            file.write(str(start) + ' -->  ' + str(end) + '\n')
            file.write(segment['text'].strip() + '\n')
            file.write('\n')


def format_delta_time(seconds):
    delta = datetime.timedelta(seconds=seconds)
    # Format in "0:00:00.xxx"
    formatted_time = "{:0>2}:{:0>2}:{:06.3f}".format(
        delta.seconds // 3600, (delta.seconds % 3600) // 60, delta.total_seconds() % 60
    )
    return formatted_time


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <argument>")
        sys.exit(1)

    filepath = sys.argv[1]

    print("### Starting conversion ###" + '\n')
    convert_audio(filepath)
    print('\n' + "### Done ###")
