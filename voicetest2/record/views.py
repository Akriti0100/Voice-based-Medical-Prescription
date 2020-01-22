import datetime
import logging
import os
import uuid

import stats
from django.core.exceptions import SuspiciousFileOperation
from django.http import JsonResponse
import wave
from django.shortcuts import render, redirect

from voicetest import settings


def home(request):
    return render(request, 'index.html')


def upload(request):
    if request.method == 'POST':
        logging.info("Received Upload POST request: %s" % request.META)
        baseDir = settings.BASE_DIR

        try:
            recordingLength = float(request.META['HTTP_LENGTH'])

            if request.user.is_anonymous():
                path = baseDir + "/media/recordings/AnonymousUser/"
                userID = None
            else:
                path = baseDir + "/media/recordings/" + request.user.username + "/"
                userID = request.user.id
            filename = str(uuid.uuid1()) + "-" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            logging.info("Filepath: %s" % path)
            if not os.path.exists(path):
                logging.info("Creating new Folder: %s" % path)
                os.makedirs(path)
            logging.info("Writing file: %s" % filename)
            extension = ".wav"
            with open(path + filename + extension, 'wb+') as destination:
                for chunk in request.FILES['blob'].chunks():
                    destination.write(chunk)

            # AudioSegment.from_file(path+filename+".ogg").export(path+filename+".mp3", format="mp3").close()
            # os.remove(path+filename+".ogg")

            # Recording.objects.create(path=path, name=filename + extension, created=timezone.now(),
            #                          user_id=userID,
            #                          length=recordingLength)
        except:
            logging.critical("Error while trying to upload! Please check previous Log Messages")
            raise SuspiciousFileOperation
        else:
         response = {'total_recordings': stats.total_recordings,}

        return JsonResponse(response, safe=False)

    else:
        return redirect('/recorder')