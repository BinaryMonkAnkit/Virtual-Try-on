// src/assets/topGarmentsStatics/topGarments.js

// Update the glob pattern to include WebP and other image formats
const topgarments = import.meta.glob('./*.{png,jpg,jpeg,svg,gif,webp}', { eager: true });

const topGarmentList = Object.keys(topgarments).map((key) => ({
    title: key.split('/').pop().split('.')[0], // Extracting filename without extension
    image: topgarments[key],
    text: 'Description for ' + key.split('/').pop().split('.')[0],
}));

export default topGarmentList;
