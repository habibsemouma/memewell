<script>
  import axios from "axios";

  let media_file, description;
  let status = "";
  const image_extensions = ["jpg", "jpeg", "png"];
  const video_extensions = ["mp4", "avi", "mov"];

  async function send_media() {
    media_file = media_file[0];
    if (description.length > 60) {
      status= "length error"
      return;
    }
    if (media_file.size > 1920 * 1080) {
      status="size error";
      return
    }
    const re = /(?:\.([^.]+))?$/;
    const fileExtension = re.exec(media_file.name)[1];
    if (image_extensions.includes(fileExtension)) {
      if (media_file.size > 1920 * 1080) {
        
        status = "size error";
        console.log("qdqdscsq",media_file.size)
        return;
      } else {
        const api_endpoint = "http://localhost:5000/image_add";
        const media_type ="image"
      }
    } else if (video_extensions.includes(fileExtension)) {
      if (media_file.size > 50 * 1024 * 1024) {
        status = "size error";
        console.log("qdqd",media_file.size)
        return;
      } else {
        const api_endpoint = "http://localhost:5000/video_add";
        const media_type="video"
      }
    } else {
      status = "extension error";
      return;
    }

    const payload = new FormData();
    payload.append(media_type, media_file);
    payload.append("description", description);
    let response = await axios.post(api_endpoint, payload);
    status = response.data["message"];
  }
</script>

<div id="wrapper">
  <div id="sub-wrapper">
    <input bind:files={media_file} type="file" />
    <input bind:value={description} type="text" placeholder="description" />
    <button on:click={send_media}>Submit</button>
    <h1>{status}</h1>
  </div>
</div>

<style>
  #wrapper {
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 20px;
    padding: 1rem;
    justify-content: center;
    align-items: center;
    box-shadow: 1px -1px 17px 0px rgba(0, 0, 0, 0.75);
    -webkit-box-shadow: 1px -1px 17px 0px rgba(0, 0, 0, 0.75);
    -moz-box-shadow: 1px -1px 17px 0px rgba(0, 0, 0, 0.75);
  }
  #sub-wrapper {
    display: flex;
    flex-direction: column;
    row-gap: 100px;
    padding: 1rem;
    justify-content: center;
    align-items: center;
    width: 100%;
  }
  input {
    color: white;
    background-color: #24292e;
    border: none;
    border-bottom: 2px solid orangered;
    font-size: large;
    width: 80%;
    text-align: center;
  }
  button {
    background-color: green;
    border: none;
    font-weight: bold;
    padding: 10px;
    border-radius: 50px;
    font-size: 20px;
  }
  button:hover {
    cursor: pointer;
  }
</style>
