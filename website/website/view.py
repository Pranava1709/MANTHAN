

#import zipfolder

#from django.http import HttpResponse
#from django.shortcuts import render
#from django.core.files.storage import FileSystemStorage
#import sys
#import os
#from django.http import HttpResponseRedirect

#sys.path.insert(1,
#                'Single-Image-Dehazing-Python\\src')
#sys.path.insert(1,
#                'website')


#from passimage import *
#import DEHAZING_IMAGE
#import DENOISING_IMAGE
#import shutil

#def home(request):
#    return render(request, "index.html")


#def dehaze(request):
#    if request.method == "POST":
#        uploaded_images = request.FILES.getlist('dehaze')
#        # print(uploaded_images.name)

#        fs = FileSystemStorage()
#        for f in uploaded_images:
#            name = fs.save(f.name, f)
#        #   context['url'] = fs.url(name)

#        DEHAZING_IMAGE.dehazing()
#        detect()
#        zipfolder.zip_directory('website\\yolov5\\runs\\detect', 'static\\output.zip')

#        dir = 'website\\uploaded_image'

#        for files in os.listdir(dir):
#            path = os.path.join(dir, files)
#            try:
#                shutil.rmtree(path)


#        #for f in os.listdir(dir):
#        #    shutil.rmtree(os.path.join(dir, f))
#            #os.remove(os.path.join(dir, f))

#        dir1 = 'website\\yolov5\\runs'
#         for files in os.listdir(dir1):
#            path = os.path.join(dir1, files)
#            try:
#                shutil.rmtree(path)
#        #for f in os.listdir(dir1):
#        #    #os.remove(os.path.join(dir1, f))
#        #    shutil.rmtree(os.path.join(dir1, f))

#        dir2 = 'website\\yolov5\\images_to_be_processed'
#        for files in os.listdir(dir2):
#            path = os.path.join(dir2, files)
#            try:
#                shutil.rmtree(path)
#        #for f in os.listdir(dir2):
#        #    shutil.rmtree(os.path.join(dir2, f))
#        #    #os.remove(os.path.join(dir2, f))

#        return render(request, "download_dehaze.html")
#    return render(request, "dehaze.html")


#def denoise(request):
#    if request.method == "POST":
#        uploaded_images = request.FILES.getlist('denoise')
#        # print(uploaded_images.name)

#        fs = FileSystemStorage()
#        for f in uploaded_images:
#            name = fs.save(f.name, f)
#        #   context['url'] = fs.url(name)

#        DENOISING_IMAGE.denoising()
#        detect()
#        zipfolder.zip_directory(
#            'website\\yolov5\\runs\\detect', 'static\\result.zip')

#        dir = 'website\\uploaded_image'
#        for f in os.listdir(dir):
#            #os.remove(os.path.join(dir, f))
#            shutil.rmtree(os.path.join(dir, f))
#        #for f in os.listdir(dir):
#        #    #os.remove(os.path.join(dir, f))
#        #    shutil.rmtree(os.path.join(dir, f))
#        dir1 = 'website\\yolov5\\runs\\detect'
#        for f in os.listdir(dir1):
#            #os.remove(os.path.join(dir, f))
#            shutil.rmtree(os.path.join(dir1, f))
#        #for f in os.listdir(dir1):
#        #    #os.remove(os.path.join(dir1, f))
#        #    shutil.rmtree(os.path.join(dir1, f))
#        dir2 = 'website\\yolov5\\result\\result1'
#        for f in os.listdir(dir2):
#            #os.remove(os.path.join(dir, f))
#            shutil.rmtree(os.path.join(dir2, f))
#        #for f in os.listdir(dir2):
#        #    #os.remove(os.path.join(dir2, f))
#        #    shutil.rmtree(os.path.join(dir2, f))
#        dir3 = 'website\\yolov5\\result\\result2'
#        for f in os.listdir(dir3):
#            #os.remove(os.path.join(dir, f))
#            shutil.rmtree(os.path.join(dir3, f))
#        #for f in os.listdir(dir3):
#        #    #os.remove(os.path.join(dir3, f))
#        #    shutil.rmtree(os.path.join(dir3, f))
#        return render(request, "download_denoise.html")
#    return render(request, "denoise.html")


##
## def download_denoise(request):
##     zip_file = open("result.zip", 'rb')
##     return FileResponse(zip_file)
##
##
##
## def download_dehaze(request):
##     zip_file = open("output.zip", 'rb')
##     return FileResponse(zip_file)



from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import sys
import os
from django.http import HttpResponseRedirect

sys.path.insert(1,
                'Single-Image-Dehazing-Python\\src')
sys.path.insert(1,
                'website')


from passimage import *
import DEHAZING_IMAGE
import DENOISING_IMAGE
import shutil
import zipfolder
import filetype
import cv2
import DEHAZING_VIDEO
import DENOISING_VIDEO
def home(request):
    return render(request, "index.html")


def dehaze(request):
    if request.method == "POST":
        uploaded_images = request.FILES.getlist('dehaze')
        # print(uploaded_images.name)
        #####################################################
        #kind = filetype.guess(uploaded_images)
        #if kind is None:
        #    print('Cannot guess file type!')
        #    return

        #print('File extension: %s' % kind.extension)
        #print('File MIME type: %s' % kind.mime)    
        #print()
        #if(kind.extension =='jpg'):
        #    print("jjjjjjjjjjjjjjjjjjjjpppppppppppppppppppppppggggggggggggggggggggggggggggggggggggggggg")
        ########################################################
        fs = FileSystemStorage()
        for f in uploaded_images:
            name = fs.save(f.name, f)
        #   context['url'] = fs.url(name)

        DEHAZING_IMAGE.dehazing()
        detect()
        zipfolder.zip_directory('website\\yolov5\\runs\\detect', 'static\\output.zip')

        dir = 'website\\uploaded_image'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))

        dir1 = 'website\\yolov5\\runs'
        for files in os.listdir(dir1):
            path = os.path.join(dir1, files)
            shutil.rmtree(path)
            
        dir2 = 'website\\yolov5\\images_to_be_processed'
        for f in os.listdir(dir2):
            os.remove(os.path.join(dir2, f))

        return render(request, "download_dehaze.html")
    return render(request, "dehaze.html")


def denoise(request):
    if request.method == "POST":
        uploaded_images = request.FILES.getlist('denoise')
        # print(uploaded_images.name)
        #####################################################
        #kind = filetype.guess(uploaded_images)
        #if kind is None: 
        #    print('Cannot guess file type!')
        #    return

        #print('File extension: %s' % kind.extension)
        #print('File MIME type: %s' % kind.mime)    
        #print()
        #if(kind.extension =='jpg'):
        #    print("jjjjjjjjjjjjjjjjjjjjpppppppppppppppppppppppggggggggggggggggggggggggggggggggggggggggg")
        ########################################################
        fs = FileSystemStorage()
        for f in uploaded_images:
            name = fs.save(f.name, f)
        #   context['url'] = fs.url(name)

        DENOISING_IMAGE.denoising()
        detectdenoise()
        zipfolder.zip_directory(
            'website\\yolov5\\runs\\detect', 'static\\result.zip')

        dir = 'website\\uploaded_image'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        

        dir1 = 'website\\yolov5\\runs\\detect'
        for f in os.listdir(dir1):
            #os.remove(os.path.join(dir, f))
            shutil.rmtree(os.path.join(dir1, f))

        dir2 = 'website\\yolov5\\result'
        for f in os.listdir(dir2):
            os.remove(os.path.join(dir2, f))



        return render(request, "download_denoise.html")
    return render(request, "denoise.html")


#
# def download_denoise(request):
#     zip_file = open("result.zip", 'rb')
#     return FileResponse(zip_file)
#
#
#
# def download_dehaze(request):
#     zip_file = open("output.zip", 'rb')
#     return FileResponse(zip_file)

#def dehaze_vid(request):
#    if request.method == "POST":
#        uploaded_images = request.FILES.getlist('dehaze_vid')
#        # print(uploaded_images.name)

#        fs = FileSystemStorage()
#        for f in uploaded_videos:
#            name = fs.save(f.name, f)
#        #   context['url'] = fs.url(name)

#        #DEHAZING_IMAGE.dehazing()
#        #detect()
#        #zipfolder.zip_directory('website\\yolov5\\runs\\detect', 'static\\output.zip')

#        #dir = 'website\\uploaded_videos'
#        #for f in os.listdir(dir):
#        #    os.remove(os.path.join(dir, f))

#        #dir1 = 'website\\yolov5\\runs'
#        #for files in os.listdir(dir1):
#        #    path = os.path.join(dir1, files)
#        #    shutil.rmtree(path)
            
#        #dir2 = 'website\\yolov5\\images_to_be_processed'
#        #for f in os.listdir(dir2):
#        #    os.remove(os.path.join(dir2, f))

#        return render(request, "dehaze_video.html")
#    return render(request, "dehaze.html")

def process_video(request):
    return render(request, "videoprocess.html")


def dehaze_video(request):
    if request.method == "POST":
        uploaded_videos = request.FILES.getlist('dehaze_video')
        # print(uploaded_images.name)
        #####################################################
        #kind = filetype.guess(uploaded_images)
        #if kind is None:
        #    print('Cannot guess file type!')
        #    return

        #print('File extension: %s' % kind.extension)
        #print('File MIME type: %s' % kind.mime)    
        #print()
        #if(kind.extension =='jpg'):
        #    print("jjjjjjjjjjjjjjjjjjjjpppppppppppppppppppppppggggggggggggggggggggggggggggggggggggggggg")
        ########################################################
        fs = FileSystemStorage()
        for f in uploaded_videos:
            name = fs.save(f.name, f)
        #   context['url'] = fs.url(name)
        DEHAZING_VIDEO.dehaze_video()
        #DEHAZING_IMAGE.dehazing()
        detect()
        zipfolder.zip_directory('website\\yolov5\\runs\\detect', 'static\\output_video_result.zip')

        #cv2.waitKey(3000)
        dir = 'website\\uploaded_image'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))

        dir1 = 'website\\yolov5\\runs'
        for files in os.listdir(dir1):
            path = os.path.join(dir1, files)
            shutil.rmtree(path)
            
        dir2 = 'website\\yolov5\\data_saved'
        for f in os.listdir(dir2):
            os.remove(os.path.join(dir2, f))

        dir2 = 'website\\yolov5\\images_to_be_processed'
        for f in os.listdir(dir2):
            os.remove(os.path.join(dir2, f))

        return render(request, "download_dehaze_video.html")
    return render(request, "dehaze_video_page.html")





def denoise_video(request):
    if request.method == "POST":
        uploaded_videos = request.FILES.getlist('denoise_video')
        # print(uploaded_images.name)
        #####################################################
        #kind = filetype.guess(uploaded_images)
        #if kind is None:
        #    print('Cannot guess file type!')
        #    return

        #print('File extension: %s' % kind.extension)
        #print('File MIME type: %s' % kind.mime)    
        #print()
        #if(kind.extension =='jpg'):
        #    print("jjjjjjjjjjjjjjjjjjjjpppppppppppppppppppppppggggggggggggggggggggggggggggggggggggggggg")
        ########################################################
        fs = FileSystemStorage()
        for f in uploaded_videos:
            name = fs.save(f.name, f)
        #   context['url'] = fs.url(name)
        DENOISING_VIDEO.denoise_video()
        #DEHAZING_IMAGE.dehazing()
        detect()
        #zipfolder.zip_directory('website\\yolov5\\runs\\detect', 'static\\output.zip')
        zipfolder.zip_directory('website\\yolov5\\runs\\detect', 'static\\output_video_result_denoise.zip')



        dir = 'website\\uploaded_image'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))

        dir1 = 'website\\yolov5\\runs'
        for files in os.listdir(dir1):
            path = os.path.join(dir1, files)
            shutil.rmtree(path)
            
        dir2 = 'website\\yolov5\\data_saved'
        for f in os.listdir(dir2):
            os.remove(os.path.join(dir2, f))

        dir2 = 'website\\yolov5\\images_to_be_processed'
        for f in os.listdir(dir2):
            os.remove(os.path.join(dir2, f))

        #dir1 = 'website\\yolov5\\runs'
        #for files in os.listdir(dir1):
        #    path = os.path.join(dir1, files)
        #    shutil.rmtree(path)
            
        #dir2 = 'website\\yolov5\\result'
        #for f in os.listdir(dir2):
        #    os.remove(os.path.join(dir2, f))

        return render(request, "download_denoise_video.html")
    return render(request, "noise_video_page.html")