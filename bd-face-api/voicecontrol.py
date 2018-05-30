import wave
from pyaudio import PyAudio,paInt16
import api2
import io
from pydub import AudioSegment
from pydub.playback import play


framerate=16000
NUM_SAMPLES=2000
channels=1
sampwidth=2
TIME=2



def save_wave_file(filename,data):
    '''save the date to the wavfile'''
    wf=wave.open(filename,'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b"".join(data))
    wf.close()

def my_record(lan=1536):
    pa=PyAudio()
    stream=pa.open(format = paInt16,channels=1,
                   rate=framerate,input=True,
                   frames_per_buffer=NUM_SAMPLES)
    my_buf=[]
    count=0
    while count<TIME*5:#控制录音时间
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
        count+=1
        print(TIME*5-count)
    #save_wave_file('01.wav',my_buf)
    stream.close()
    print("...")
    player("好的")
    return api2.asr(b"".join(my_buf),lan)



def player(text):
    aud = io.BytesIO(api2.synthesis(text)) # data的格式是mp3数据的bytestring
    sound = AudioSegment.from_file(aud, format='mp3')
    play(sound)



if __name__ == '__main__':
    print(my_record())
    print('Over!')
    #play()
