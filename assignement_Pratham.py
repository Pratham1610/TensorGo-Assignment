import speech_recognition
import moviepy.editor as mp

recognizer = speech_recognition.Recognizer()

def recognize_audio(audio):
    try:
        recognizer.adjust_for_ambient_noise(audio, duration=0.2)
        print("Listening...")
        audio_data = recognizer.listen(audio)
        text = recognizer.recognize_google(audio_data)
        text = text.lower()
        print("Transcription:", text)
    except speech_recognition.UnknownValueError:
        print("Could not understand audio")

def main():
    while True:
        try:
            print("Enter '1' to input from microphone or '2' to input from video file:")
            choice = input()

            if choice == '1':
                with speech_recognition.Microphone() as mic:
                    recognize_audio(mic)

            elif choice == '2':
                video_clip = mp.VideoFileClip("./video.mp4")
                audio_clip = video_clip.audio
                audio_clip.write_audiofile("temp_audio.wav")  # Save audio to a temporary file
                with speech_recognition.AudioFile("temp_audio.wav") as audio_file:
                    recognize_audio(audio_file)

            else:
                print("Invalid choice")

        except KeyboardInterrupt:
            print("Stopping program...")
            break

if __name__ == "__main__":
    main()
