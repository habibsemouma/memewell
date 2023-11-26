import { useState } from 'react'
import axios from 'axios'

async function get_data(description,prefix){
    const payload={"text":description,"prefix":prefix}

    const response= await axios.post("http://localhost:5000/images_fetch",payload)
    setImages(response.data)
}

function Home(){
    const [description,setDescription]=useState('')
    const [images,setImages]=useState('')
    const [prefix,setPrefix]=useState("random")


    const handleDescription=(event)=>{
        setDescription(event.target.value)
    }

    return(
        <div >
            <input onChange={handleDescription} placeholder="Describe your meme"></input>
            <button onClick={()=>get_data(description,prefix)}>Get memes</button>
            <div>
                {images.map(item =>(
                    <img src={item}></img>
                ))}

            </div>
        </div>

    )
}
export default Home