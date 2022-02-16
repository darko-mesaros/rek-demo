#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import json
import os
import colorama
from colorama import Fore, Style


def recognize_celebrities(photo):

    
    client=boto3.client('rekognition')

    with open(photo, 'rb') as image:
        response = client.recognize_celebrities(Image={'Bytes': image.read()})

    celeb_faces = response['CelebrityFaces']   
    print(json.dumps(celeb_faces))
    print('Detected faces for ' + photo)    
    for celebrity in celeb_faces:
        print (Fore.YELLOW+'Name: ' + Fore.BLUE + celebrity['Name'])
        print (Fore.YELLOW+'Id: ' + Fore.GREEN + celebrity['Id'])
        print (Fore.YELLOW+'Position:')
        print (Fore.RED+'   Left: ' + Fore.BLUE + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Height']))
        print (Fore.RED+'   Top: ' + Fore.BLUE + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Top']))
        print (Fore.YELLOW+'Info')
        for url in celebrity['Urls']:
            print (Fore.GREEN + '   ' + url)

    return len(celeb_faces)

def main():
    directory='img'

    for entry in os.scandir(directory):
        if (entry.path.endswith(".jpg")
                or entry.path.endswith(".jpeg")
                or entry.path.endswith(".png")) and entry.is_file():
            celeb_count=recognize_celebrities(entry.path)
            print(Fore.WHITE + "Celebrities detected: " + str(celeb_count))


if __name__ == "__main__":
    main()
