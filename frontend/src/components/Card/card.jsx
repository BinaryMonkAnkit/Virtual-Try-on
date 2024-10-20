// import Button from '/src/components/Button/button.jsx'
// import styles from './card.module.css'
// import profileImage from '/src/assets/profile.png'

// function Card(){

// //take pictures of the garments and use them to make cards for every pictures

//     //the card should be clickable

//     return(
//         <div className={styles.card}>
//             <img className= {styles.cardImage} src={profileImage} alt="profile picture"></img>
//             <h2 className={styles.cardTitle}>VTR room</h2>
//             <p className={styles.cardText}>I buld mahcine that can learn by itself and I enjoy gym.</p>
//             <Button/>
//         </div>
//     );

// }

// export default Card


// src/components/Card/Card.jsx
// import React from 'react';
// import Button from '/src/components/Button/button.jsx';
// import styles from './card.module.css';

// function Card({ image, title, text }) {
//     return (
//         <div className={styles.card} onClick={() => console.log(`Clicked on: ${title}`)}>
//             <img className={styles.cardImage} src={image.default} alt={title} />
//             <h2 className={styles.cardTitle}>{title}</h2>
//             <p className={styles.cardText}>{text}</p>
            
//         </div>
//     );
// }

// export default Card;



// src/components/Card/Card.jsx
// import React from 'react';
// import styles from './card.module.css';

// function Card({ image, title, text, onCardClick, isSelected }) {
//     return (
//         <div className={`${styles.card} ${isSelected ? styles.selected : ''}`} onClick={() => onCardClick(image)}>
//             <img className={styles.cardImage} src={image.default} alt={title} />
//             <h3 className={styles.cardTitle}>{title}</h3>
//             <p className={styles.cardText}>{text}</p>
            
//         </div>
//     );
// }

// export default Card;


import React from 'react';
import styles from './card.module.css';

function Card({ image, title, text, onCardClick, isSelected }) {
    return (
        <div
            className={`${styles.card} ${isSelected ? styles.selected : ''}`}
            onClick={() => onCardClick(image)} // `onCardClick` expects an image argument
        >
            <img className={styles.cardImage} src={image.default} alt={title} />
            <h3 className={styles.cardTitle}>{title}</h3>
            <p className={styles.cardText}>{text}</p>
        </div>
    );
}

export default Card;
