# Execute the whole script
import sys

from API_Connect import API
from extract_vocal import Extract

def main():
    ''' try:
        print('okay')'''
    # Le vecteur principal du sytème 
    audio_name, save_path, vocal_path  = API()

    # Actioner la séparation du vocal avec HPSS
    Extract(audio_name, save_path, vocal_path)
    ''' except:
        print('Error')
        sys.exit()'''


#if __name__ == '__main':
main()
