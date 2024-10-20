 
//  function VTRroom(){
//      // var ws = new WebSocket('ws://127.0.0.1:8000/ws/ac/')
//    const groupName = JSON.parse(document.getElementById('group-name').textContent)
//    var ws = new WebSocket(
//        'ws://'
//        + window.location.host 
//        + '/ws/ac/' 
//        + groupName 
//        +'/'
//    )

//    console.log(groupName);

//    ws.onopen = function(){
//        console.log('Websocket connection is open.... ');

//        // ws.send("Hi message from client to server...")

       
//    }
//    // runs when message is received from server
//    ws.onmessage = function(event){
//        const eventData = JSON.parse(event.data)

//        console.log("Message from server...", eventData.msg);

//     //    console.log("Type of Message from server...",typeof eventData);

//        // document.getElementById('chat-log').innerText = eventData['msg'] + '\n';
       
//     //    document.querySelector('#chat-log').value += (eventData.msg + '\n')




//        // document.getElementById("liveData").innerText = data.count
//    }

   
//    ws.onerror = function(event){
//        console.log('Websocket error occured.... ', event);
//    }

//    ws.onclose = function(event){
//        console.log('Websocket connection closed.... ', event);
//    }

//    document.getElementById('chat-message-submit').onclick = function(event)
//    {
//        //take the message input 
//        const messageInputDom = document.getElementById('chat-message-input')
//        const message = messageInputDom.value 
//        //sending message to the server it will be stored in event['text'] 
//        if(message != ""){
//            ws.send(JSON.stringify({
//            'msg': message
//        }))
//        messageInputDom.value = '';
//        }       
       
//     }
//     return(
//         <div className={styles.room}>
//             <h1>Video stream component</h1>


//         </div>
//     )

//  }
 
// export default VTRroom


// import { useEffect, useRef, useState } from 'react';
// import styles from './VTRroom.module.css';

// function VTRroom() {
//     const videoRef = useRef(null); // For rendering the video feed in the UI
//     // const ws = useRef(null); // For holding the WebSocket instance
//     const streamRef = useRef(null); // For holding the media stream
//     // const [groupName, setGroupName] = useState(null); // State to hold the group name

//     // useEffect(() => {
//     //     // Get group name from the JSON script tag
//     //     const groupNameElement = document.getElementById("group-name");
//     //     console.log("group name",groupNameElement);
//     //     if (groupNameElement) {
//     //         try {
//     //             setGroupName(JSON.parse(groupNameElement.textContent));
//     //         } catch (error) {
//     //             console.error('Error parsing group name:', error);
//     //         }
//     //     } else {
//     //         console.error('Element with id "group-name" not found');
//     //         return;
//     //     }


            
//     const startVideoFeed = async () => {
//         try {
//             // Access the user's camera
//             const stream = await navigator.mediaDevices.getUserMedia({ video: true });
//             streamRef.current = stream;

//             // Display the video stream in the video element
//             if (videoRef.current) {
//                 videoRef.current.srcObject = stream;
//             }

//             // Start sending frames to the server
//             sendVideoFrames();
//         } catch (error) {
//             console.error('Error accessing camera:', error);
//         }
//     };


//     const stopVideoFeed = () => {
//         // Stop all media tracks (video feed)
//         streamRef.current.getTracks().forEach(track => track.stop());
//     };


//     const sendVideoFrames = () => {
//         const canvas = document.createElement('canvas');
//         const video = videoRef.current;

//         const captureFrame = () => {
//             if (!ws || ws.readyState !== WebSocket.OPEN || !video) {
//                 return;
//             }

//             // Draw the video frame onto the canvas
//             canvas.width = video.videoWidth;
//             canvas.height = video.videoHeight;
//             const ctx = canvas.getContext('2d');
//             ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

//             // Convert the frame to a blob (or alternatively use base64)
//             canvas.toBlob((blob) => {
//                 if (blob) {
//                     // Send the blob over WebSocket
//                     ws.send(blob);
//                 }
//             }, 'image/jpeg'); // Adjust the format and quality as needed

//             // Request the next frame
//             requestAnimationFrame(captureFrame);
//         };

//         // Start capturing frames
//         captureFrame();
//     };

// // Initialize the WebSocket connection after group name is set

//     var ws = new WebSocket(`ws://${window.location.host}/ws/ac/`);
//     console.log("websocket initiated",`ws://${window.location.host}/ws/ac/` );

//     // WebSocket connection opened
//     ws.onopen = () => {
//         console.log('WebSocket connection is open.');
//         ws.send("Hi I am client.");
//         startVideoFeed();

//     };

//     // Handle incoming messages
//     ws.onmessage = (event) => {
//         console.log("Message from server:", event.data);
    

//     };

//     // WebSocket error handling
//     ws.onerror = (error) => {
//         console.error('WebSocket error:', error);
//     };

//     // WebSocket connection closed
//     ws.onclose = (event) => {
//         console.log('WebSocket connection closed:', event);
        

//         // return () => {
//         //     if (ws) {
//         //         ws.close();
//         //     }
//             if (streamRef.current) {
//                 stopVideoFeed();
//             }
//     };


//         // Start the video feed when component mounts
        

//         // Cleanup: close WebSocket and stop video feed when component unmounts
        
//     // }); // Run effect when groupName changes

    
   



//     return (
//         <div className={styles.room}>
//             <h1>Live Video Stream</h1>
//             <video
//                 ref={videoRef}
//                 autoPlay
//                 muted
//                 className={styles.videoFeed} // Add CSS to style the video feed
//             />
//         </div>
//     );

// }

// export default VTRroom;
















//  THIS IS THE WORKING CODE FOR THE CHANNEL
import { useEffect, useRef } from 'react';
import styles from './VTRroom.module.css';
import fullscreen  from '../../assets/png/fullscreen.png';
import zoomout  from '../../assets/png/zoomout.png';


function VTRroom() {
    const videoCanvasRef = useRef(null);  // For rendering the video feed to the canvas
    const ws = useRef(null);              // WebSocket instance reference

    useEffect(() => {
        // Initialize WebSocket connection
        ws.current = new WebSocket(`ws://${window.location.host}/ws/ac/`);
        console.log("WebSocket initiated", `ws://${window.location.host}/ws/ac/`);

        // Handle WebSocket open event
        ws.current.onopen = () => {
            console.log('WebSocket connection is open.');
            startVideoFeed();  // Start video feed after WebSocket connection is established
        };

        // Handle incoming WebSocket messages
        ws.current.onmessage = async (event) => {
            // Handle binary data (Blob) received from the server
            if (event.data instanceof Blob) {
                console.log('Received binary data from server.');

                const arrayBuffer = await event.data.arrayBuffer();
                const blob = new Blob([arrayBuffer], { type: 'image/jpeg' });
                const img = new Image();

                img.src = URL.createObjectURL(blob);

                // Render image when it is loaded
                img.onload = () => {
                    const ctx = videoCanvasRef.current.getContext('2d');
                    const canvas = videoCanvasRef.current;
                    
                    // Set canvas dimensions based on the image received
                    canvas.width = img.width;
                    canvas.height = img.height;
                    
                    // Draw the image onto the canvas
                    ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

                    // Clean up the Blob URL
                    URL.revokeObjectURL(img.src);
                };
            } else {
                console.log("Received non-binary message:", event.data);
            }
        };

        // Handle WebSocket error event
        ws.current.onerror = (error) => {
            console.error('WebSocket error:', error);
        };

        // Handle WebSocket close event
        ws.current.onclose = (event) => {
            console.log('WebSocket connection closed:', event);
        };

        // Cleanup WebSocket connection on component unmount
        return () => {
            if (ws.current) {
                ws.current.close();
            }
        };
    }, []);

    // Access user camera and start streaming video frames
    const startVideoFeed = async () => {
        try {
            // Get user media (camera)
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            const video = document.createElement('video');
            video.srcObject = stream;
            video.play();

            // Send video frames to the server
            sendVideoFrames(video);
        } catch (error) {
            console.error('Error accessing camera:', error);
        }
    };

    // Capture video frames and send to WebSocket
    const sendVideoFrames = (video) => {
        const canvas = document.createElement('canvas');

        const captureFrame = () => {
            if (!ws.current || ws.current.readyState !== WebSocket.OPEN) {
                return;
            }

            // Draw the video frame onto the canvas
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            const ctx = canvas.getContext('2d');
            ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

            // Convert the canvas to a Blob and send it via WebSocket
            canvas.toBlob((blob) => {
                if (blob) {
                    ws.current.send(blob);
                }
            }, 'image/jpeg', 0.6);  // Compress the image (JPEG quality 0.6)

            // Throttle the frame rate to 15 FPS
            setTimeout(captureFrame, 1000 / 15); // 15 FPS
        };

        // Start capturing frames
        captureFrame();
    };

    return (
        <div className={styles.room}>
            <button className={styles.zoomIn} ><img width={30} height={30} src={fullscreen} alt="Icon" /> </button>
            <div className={styles.GarmentColors}>VIRTUAL MIRROR</div>
            <div className={styles.videoWrapper}>
                <canvas
                    ref={videoCanvasRef}
                    className={styles.videoFeed}  // Canvas video feed element
                /> 
            </div>
            <div className={styles.GarmentColors}>CLOTH SIZE</div>
        </div>
    );
}

export default VTRroom;
