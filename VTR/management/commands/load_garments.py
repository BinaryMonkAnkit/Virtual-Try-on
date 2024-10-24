# import os
# import django
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# import time

# # # Set up Django's environment
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Virtualroom.settings')
# django.setup()

# from VTR.models import Garment  # Import the model

# # Get the current count of garments to determine the next number
# def get_next_garment_number():
#     count = Garment.objects.count()
#     return count + 1  # Start from 1 if no garments exist

# # Your logic to load and insert garments into the database
# def load_garment(file_path, garment_number=None):
#     if file_path.endswith(('.png', '.jpg', '.jpeg','.mpeg')):
#         with open(file_path, 'rb') as f:
#             image_data = f.read()

#         # Extract the file name without extension
#         file_name = os.path.splitext(os.path.basename(file_path))[0]

#         # If garment number is provided, use it for the name and description
#         if garment_number:
#             name = f"tshirt{garment_number}"
#             description = f"description for {name}"
#         else:
#             # Use file name if garment_number is not specified
#             name = file_name
#             description = f"description for {file_name}"

#         # Create and save the Garment object
#         garment = Garment(
#             name=name,
#             image=image_data,
#             description=description
#         )
#         garment.save()
#         print(f'Successfully added {name}')
#     else:
#         print(f'Skipped {file_path}, not an image file')


# # Watchdog event handler for new files
# class NewFileHandler(FileSystemEventHandler):
#     def __init__(self, garment_number):
#         self.garment_number = garment_number

#     def on_created(self, event):
#         if not event.is_directory:  # We are only interested in files, not directories
#             load_garment(event.src_path, self.garment_number)
#             self.garment_number += 1  # Increment the garment number for the next file


# if __name__ == '__main__':
#     folder_path = r'VTR\garment_images'

#     # Get the next available garment number based on the number of rows in the database
#     garment_number = get_next_garment_number()

#     # Load any pre-existing images in the folder
#     for filename in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, filename)
#         load_garment(file_path, garment_number)
#         garment_number += 1

#     # Create the observer and event handler
#     event_handler = NewFileHandler(garment_number)
#     observer = Observer()

#     # Set observer to watch the directory
#     observer.schedule(event_handler, path=folder_path, recursive=False)

#     # Start the observer
#     observer.start()
#     print(f'Starting to watch folder: {folder_path}')

#     try:
#         # Keep the script running indefinitely
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()

import os
import django
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from django.core.management.base import BaseCommand  # Import BaseCommand

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get the current count of garments to determine the next number
def get_next_garment_number():
    from VTR.models import Garment  # Import the model inside the function to avoid import issues
    count = Garment.objects.count()
    return count + 1  # Start from 1 if no garments exist

# Your logic to load and insert garments into the database
def load_garment(file_path, garment_number=None):
    from VTR.models import Garment  # Import the model inside the function to avoid import issues
    if file_path.endswith(('.png', '.jpg', '.jpeg')):
        try:
            with open(file_path, 'rb') as f:
                image_data = f.read()

            # Extract the file name without extension
            file_name = os.path.splitext(os.path.basename(file_path))[0]

            # If garment number is provided, use it for the name and description
            if garment_number:
                name = f"tshirt{garment_number}"
                description = f"description for {name}"
            else:
                # Use file name if garment_number is not specified
                name = file_name
                description = f"description for {file_name}"

            # Create and save the Garment object
            garment = Garment(
                name=name,
                image=image_data,
                description=description
            )
            garment.save()
            logger.info(f'Successfully added {name}')
        except Exception as e:
            logger.error(f'Error loading {file_path}: {e}')
    else:
        logger.warning(f'Skipped {file_path}, not an image file')

# Watchdog event handler for new files
class NewFileHandler(FileSystemEventHandler):
    def __init__(self, garment_number):
        self.garment_number = garment_number

    def on_created(self, event):
        if not event.is_directory:  # We are only interested in files, not directories
            load_garment(event.src_path, self.garment_number)
            self.garment_number += 1  # Increment the garment number for the next file

# Define the Command class
class Command(BaseCommand):
    help = 'Load garments from a folder and watch for new files'

    def handle(self, *args, **options):
        folder_path = r'VTR\garment_images'  # Update this path if necessary

        # Get the next available garment number based on the number of rows in the database
        garment_number = get_next_garment_number()

        # Load any pre-existing images in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            load_garment(file_path, garment_number)
            garment_number += 1

        # Create the observer and event handler
        event_handler = NewFileHandler(garment_number)
        observer = Observer()

        # Set observer to watch the directory
        observer.schedule(event_handler, path=folder_path, recursive=False)

        # Start the observer
        observer.start()
        logger.info(f'Starting to watch folder: {folder_path}')

        try:
            # Keep the script running indefinitely
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
