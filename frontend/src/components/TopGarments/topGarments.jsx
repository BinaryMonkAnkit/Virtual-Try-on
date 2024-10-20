
// //Original code 
// import React, {useState} from 'react';
// import axios from 'axios';  // You need to install axios: npm install axios
// import Card from '/src/components/Card/card.jsx';
// import styles from './topGarments.module.css';
// import topGarmentList from '/src/assets/topGarmentsStatics/topGarments.js';

// function TopGarments() {
//     const sendSelectedImage = (image, key) => {

//         const [selectedCardKey, setSelectedCardKey] = useState(null);        
//         setSelectedCardKey(key);
        
//         // Create a new image object
//         const img = new Image();
//         img.src = image.default;  // Assuming image.default is the URL of the PNG image

//         img.onload = () => {
//             // Create a canvas to draw the image
//             const canvas = document.createElement('canvas');
//             canvas.width = img.width;
//             canvas.height = img.height;
//             const ctx = canvas.getContext('2d');
//             ctx.drawImage(img, 0, 0);

//             // Convert the canvas to a PNG Blob and send it via HTTP
//             canvas.toBlob((blob) => {
//                 if (blob) {
//                     // Create a FormData object to package the blob and metadata
//                     const formData = new FormData();
//                     formData.append('image', blob, 'selected-image.png'); // Keep it as PNG

//                     // Send image to the backend via HTTP POST request
//                     const backendUrl = `${window.location.protocol}//${window.location.host}/upload_image/`;
//                     axios.post(backendUrl, formData, {
//                         headers: {
//                             'Content-Type': 'multipart/form-data'
//                         }
//                     })
//                     .then((response) => {
//                         console.log('Image uploaded successfully:', response.data);
//                     })
//                     .catch((error) => {
//                         console.error('Error uploading image:', error);
//                     });
//                 }
//             }, 'image/png'); // Keep the format as PNG
//         };
//     };

//     return (
//         <div className={styles.gallery}>
//             {topGarmentList.length > 0 ? (
//                 topGarmentList.map((garment, index) => (
//                     <Card
//                         className={styles.card}
//                         key={index}
//                         image={garment.image}
//                         title={garment.title}
//                         text={garment.text}
//                         onCardClick={sendSelectedImage(garment.image, index)}
//                         isSelected={selectedCardKey === garment.key}
//                     />
//                 ))
//             ) : (
//                 <p>No garments available.</p>
//             )}
//         </div>
//     );
// }
// export default TopGarments;



import React, { useState } from 'react';
import axios from 'axios';  // You need to install axios: npm install axios
import Card from '/src/components/Card/card.jsx';
import styles from './topGarments.module.css';
import topGarmentList from '/src/assets/topGarmentsStatics/topGarments.js';

function TopGarments() {
    const [selectedCardKey, setSelectedCardKey] = useState(null); // Moved state outside

    const sendSelectedImage = (image, key) => {
        setSelectedCardKey(key); // This will now set the selected card by key

        // Create a new image object
        const img = new Image();
        img.src = image.default;  // Assuming image.default is the URL of the PNG image

        img.onload = () => {
            // Create a canvas to draw the image
            const canvas = document.createElement('canvas');
            canvas.width = img.width;
            canvas.height = img.height;
            const ctx = canvas.getContext('2d');
            ctx.drawImage(img, 0, 0);

            // Convert the canvas to a PNG Blob and send it via HTTP
            canvas.toBlob((blob) => {
                if (blob) {
                    // Create a FormData object to package the blob and metadata
                    const formData = new FormData();
                    formData.append('image', blob, 'selected-image.png'); // Keep it as PNG

                    // Send image to the backend via HTTP POST request
                    const backendUrl = `${window.location.protocol}//${window.location.host}/upload_image/`;
                    axios.post(backendUrl, formData, {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    })
                    .then((response) => {
                        console.log('Image uploaded successfully:', response.data);
                    })
                    .catch((error) => {
                        console.error('Error uploading image:', error);
                    });
                }
            }, 'image/png'); // Keep the format as PNG
        };
    };

    return (
        <div className={styles.GarmentHeading} ><h1>Tops</h1>

            <div className={styles.topGarmentCards}>            
                {topGarmentList.length > 0 ? (
                    topGarmentList.map((garment, index) => (
                        <Card
                            className={styles.card}
                            key={index}
                            image={garment.image}
                            title={garment.title}
                            text={garment.text}
                            onCardClick={() => sendSelectedImage(garment.image, index)} // Corrected to pass image and key
                            isSelected={selectedCardKey === index} // Compare with selectedCardKey state
                        />
                    ))
                ) : (
                    <p>No garments available.</p>
                )}
            </div>
        </div> 
    );
}

export default TopGarments;
