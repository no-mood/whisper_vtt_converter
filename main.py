import datetime
import whisper


def convert_audio(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path, language="en", fp16=False, verbose=True)
    print(f' The text in video: \n {result["text"]}')

    save_target = file_path + '.vtt'
    with open(save_target, "w") as file:
        file.write('WEBVTT' + '\n' + '\n')
        for index, segment in enumerate(result['segments']):
            file.write(str(index + 1) + '\n')
            start = (datetime.timedelta(seconds=segment['start']))
            end = (datetime.timedelta(seconds=segment['end']))

            time_list = []
            for time in [segment['start'], segment['end']]:
                delta = datetime.timedelta(seconds=time)
                # Format in "0:00:00.xxx"
                formatted_time = "{:0>2}:{:0>2}:{:06.3f}".format(
                    delta.seconds // 3600, (delta.seconds % 3600) // 60, delta.total_seconds() % 60
                )
                time_list.append(formatted_time)

            file.write(str(time_list[0]) + ' -->  ' + str(time_list[1]) + '\n')
            file.write(segment['text'].strip() + '\n')
            file.write('\n')


if __name__ == '__main__':
    filepath = "/path/to/filename.mp4"
    convert_audio(filepath)
    print("### Done ###")
