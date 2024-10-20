from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .runtime_storage import top_garment_image_store

# from .serializer import UserSerializer


        
    # Here we are accessing the group_name variable from the urls.py file and sending it to the index.html file
def index(request):
  
    
    return render(request, 'index.html')# sending group_name in dictionary format to the index.html


# @csrf_exempt
# def upload_image(request):
#     if request.method == 'POST' and request.FILES.get('image'):
#         image_file = request.FILES['image']
        
#         # Read image content
#         image_data = image_file.read()
        
#         # Store the image in the in-memory dictionary
#         # You can use a unique identifier as the key, such as image name or timestamp
#         image_id = image_file.name  # You can make this more unique if needed
#         top_garment_image_store[image_id] = image_data

#         return JsonResponse({'message': 'Image stored in memory', 'image_id': image_id}, status=200)
#     else:
#         return JsonResponse({'error': 'No image found or invalid request'}, status=400)


@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']

        # Save the PNG file in-memory or temporary storage for further processing
        image_data = image_file.read()
        
        # Store in a temporary in-memory dictionary for now (or filesystem)
        image_id = image_file.name  # This could be more unique
        top_garment_image_store[image_id] = image_data

        return JsonResponse({'message': 'PNG image stored successfully', 'image_id': image_id}, status=200)
    else:
        return JsonResponse({'error': 'No image or invalid request'}, status=400)
