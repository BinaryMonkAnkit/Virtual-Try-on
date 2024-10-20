

#ORIGINAL WORKING CODE
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import StopConsumer
from .runtime_storage import top_garment_image_store
from .video_processing import process_frame
from .video_processing import process_frame_async
import asyncio


class MyAsyncConsumer(AsyncWebsocketConsumer):
    async def websocket_connect(self, event):
        print("Websocket connected...", event)
        await self.channel_layer.group_add('programmers', self.channel_name)
        await self.accept()  # Accept the WebSocket connection

    async def websocket_receive(self, event):
        print("Message received from WebSocket.")

        # Check if the message contains binary data (frame)
        if 'bytes' in event:
            frame_data = event['bytes']  # Extract the binary frame data
            frame_size = len(frame_data)
            print(f"Received binary frame of size: {frame_size} bytes")

            try:
                # Broadcast the binary frame to the group for processing
                await self.channel_layer.group_send(
                    'programmers',
                    {
                        'type': 'video.frame',  # Event type for handling video frames
                        'frame': frame_data
                    }
                )
            except Exception as e:
                print(f"Error broadcasting frame to group: {e}")
        else:
            print("Received non-binary message, ignoring.")
    
    async def video_frame(self, event):
        frame = event.get('frame')
        
        # Sanity check: ensure the frame exists and is not empty
        if frame:
            try:
                # Process the frame asynchronously
                future = process_frame_async(frame, top_garment_image_store)
                
                # Wait for the processed frame to be ready
                processed_video = await asyncio.wrap_future(future)

                # Send the processed frame to the clients
                await self.send(bytes_data=processed_video)
                print(f"Sent processed frame of size {len(processed_video)} bytes to clients.")
            except Exception as e:
                print(f"Error sending frame to WebSocket clients: {e}")
        else:
            print("Received empty frame, not sending.")

    async def websocket_disconnect(self, event):
        print("Websocket Disconnected....", event)
        await self.channel_layer.group_discard('programmers', self.channel_name)
        raise StopConsumer()
