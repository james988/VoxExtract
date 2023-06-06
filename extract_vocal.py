# This code extracts vocal from audio file
import os
import librosa
import soundfile as sf

from datetime import date


def Extract(audio_name, save_path, vocal_path):

    todaydate  = date.today().strftime('%d%m%Y')

    audio_file = os.path.join(save_path, audio_name)
    # Load the file
    audio, sr  = librosa.load(audio_file)

    '''
    Perform vocal extraction: Librosa does not have 
    a built-in vocal extraction function, but you can use 
    other techniques such as source separation or harmonic/percussive 
    source separation (HPSS) to achieve a similar effect.
    '''
    harmonic, percussive = librosa.effects.hpss(audio)
    vocals               = audio - percussive
    print('Separation of Harmonic/Percussive Source\n')

    output_file = vocal_path + todaydate + f'/{audio_name[:-5]}.wav'
    sf.write()
    librosa.output.write_wav(output_file, vocals, sr)
    print('Done')


if __name__ == '__main__':
    print('Vocal extraction\n')
    Extract()