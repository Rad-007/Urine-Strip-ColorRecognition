from django.shortcuts import render

# Create your views here.
import cv2
import json
from django.http import JsonResponse
from django.shortcuts import render,redirect
from .forms import StripImageForm

from .rgb_value import values


def reading(my_dict):
    values=list(my_dict.values())
    print(values)

    colors={
        'URO':list(values[0]),
        'BIL':list(values[1]),
        'KET':list(values[2]),
        'BLD':list(values[3]),
        'PRO':list(values[4]),
        'NIT':list(values[5]),
        'LEU':list(values[6]),
        'GLU':list(values[7]),
        'SG':list(values[8]),
        'PH':list(values[9]),
    }

    return(colors)


def analyze_strip(request):
    if request.method == 'POST':
        form = StripImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded image
            form.save()

            # Read the uploaded image using OpenCV
            image_path = form.instance.image.path
            image = cv2.imread(image_path)

            colors=values(image_path=image_path)

            content=reading(colors)


            # Perform color analysis on the image and extract the RGB values
            # Modify this section according to your color analysis requirements

            # Example code: Extracting the RGB values of the top-left pixel
            

            # Return the color results as JSON
            return render(request,'index.html',{'data': content})
    else:
        form = StripImageForm()
    return render(request, 'index.html', {'form': form})
