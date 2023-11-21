<script>
  import axios from "axios";

  let image_file, description;
  let status=""

  async function send_image() {
    image_file=image_file[0]
    if (description.length > 60) {
      return "length error";
    }
    if (image_file.size > 1920 * 1080) {
      return "size error";
    }
    const re = /(?:\.([^.]+))?$/;
    const fileExtension = re.exec(image_file.name)[1];
    const allowedExtensions = ["jpg", "jpeg", "png"];
    if (!allowedExtensions.includes(fileExtension)) {
      status= "extension error";
      return
    }
    if (image_file.size > 1920 * 1080) {
      status="size error";
      return
    }

    const payload = new FormData();
    payload.append("image", image_file);
    payload.append("description", description);
    let response = await axios.post("http://localhost:5000/image_add", payload);
    status= response.data["message"];
  }
</script>

<div id="wrapper">
  <div id="sub-wrapper">
    <input bind:files={image_file} type="file" />
    <input bind:value={description} type="text" placeholder="description" />
    <button on:click={send_image}>Submit</button>
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
    gap: 100px;
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
</style>
