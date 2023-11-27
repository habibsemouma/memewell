import { useState } from "react";
import axios from "axios";
import '../styles/Home.css'

function Home() {
    async function get_data(description, prefix) {
        const payload = { text: description, prefix: prefix };
        const response = await axios.post("http://localhost:5000/images_fetch", payload);
        setImages(response.data.images);
    }

    const [description, setDescription] = useState("");
    const [images, setImages] = useState([]);
    const [prefix, setPrefix] = useState("random");

    const handleDescription = (event) => {
        setDescription(event.target.value);
    };

    return (
        <div id="home-wrapper">
            <input onChange={handleDescription} placeholder="Describe your meme"></input>
            <button id="submitbtn" onClick={() => get_data(description, prefix)}>Get memes</button>
            <div id="images-container">
                {images.map((item) => (
                    <img key={item} src={item}></img>
                ))}
            </div>
        </div>
    );
}
export default Home;
