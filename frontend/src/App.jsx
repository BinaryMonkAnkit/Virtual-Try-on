import React from 'react'
import VTRroom from './components/VTRroom/VTRroom.jsx'
import TopGarments from './components/TopGarments/topGarments.jsx'
import styles from './styles/App.module.css'
// import GarmentSelector from './components/GarmentSelector/GarmentSelcetor.jsx'


function App() {  
  
  
  return (
    <div className={styles.parentComponent}>    
        <div className={styles.VTRroom}>            
            <VTRroom />               
        </div>
        {/* <div className={styles.garmentSelector}><GarmentSelector/></div>  */}
        <div className={styles.TopGarments}>
            <TopGarments />
        </div>
    </div>
)}

export default App
