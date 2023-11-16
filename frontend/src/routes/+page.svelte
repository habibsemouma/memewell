<script>
  import axios from "axios";
  import { RingLoader } from "svelte-loading-spinners";
  let text, paths;
  let data_loading = false;
  let data_loaded = false;
  let selectedbtn=""

  function select_btn(btn){
    selectedbtn=btn
  }

  async function fetch_memes() {
    data_loaded = false;
    data_loading = true;
    let payload = { text: text,prefix:selectedbtn };
    const response = await axios.post(
      "http://127.0.0.1:5000/images_fetch",
      payload
    );
    paths = response.data.images;
    data_loaded = true;
    data_loading = false;
  }

  async function dl_img(dl_link) {
    let response = await axios.get(dl_link, {
      responseType: "blob",
    });
    const imageBlob = response.data;

    const imageName = dl_link.split("/").pop();

    const downloadUrl = URL.createObjectURL(imageBlob);

    const link = document.createElement("a");
    link.href = downloadUrl;
    link.download = imageName;
    document.body.appendChild(link);
    link.click();
    link.remove();

    URL.revokeObjectURL(downloadUrl);
  }
</script>

<div id="wrapper">
  <input placeholder="Describe your meme" bind:value={text} />

  <div>
    <button  class:active={selectedbtn === "twitterfr"} on:click={() => select_btn("twitterfr")} id="twitterbtn">Twitter francais</button>
    <button class:active={selectedbtn === ""} on:click={() => select_btn("")} id="randombtn">Random</button>
  </div>

  <button on:click={fetch_memes}>Get memes</button>
  <div id="results">
    {#if data_loading}
      <RingLoader />
    {/if}
    {#if data_loaded}
      {#each paths as path}
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
        <img
          src="http://{path}"
          alt="dummy"
          on:click={() => dl_img("http://" + path)}
        />
      {/each}
    {/if}
  </div>
</div>

<style>
  #wrapper {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 30px;
    width: 100%;
  }
  #results {
    min-width: 75%;
    min-height: 65vh;
    height: 65%;
    width: 75%;
    padding: 2rem;
    box-shadow: -1px 0px 23px 0px rgba(0, 0, 0, 0.75);
    -webkit-box-shadow: -1px 0px 23px 0px rgba(0, 0, 0, 0.75);
    -moz-box-shadow: -1px 0px 23px 0px rgba(0, 0, 0, 0.75);
    display: grid;
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    grid-template-rows: repeat(2, 1fr);
    grid-column-gap: 20px;
    grid-row-gap: 20px;
  }
  input {
    background-color: #24292e;
    border: none;
    border-bottom: 1px solid orangered;
    font-size: 20px;
    text-align: center;
    width: 50%;
  }
  input:focus {
    outline: none;
  }
  button {
    background-color: orangered;
    font-weight: bold;
    border: none;
    font-size: 20px;
    padding: 10px;
    border-radius: 50px;
    
  }
  button:hover {
    cursor: pointer;
  }

  #twitterbtn {
    border-radius: 0;
    -webkit-border-top-left-radius: 50px;
    -webkit-border-bottom-left-radius: 50px;
    -moz-border-radius-topleft: 50px;
    -moz-border-radius-bottomleft: 50px;
    border-top-left-radius: 50px;
    border-bottom-left-radius: 50px;
  }
  #randombtn {
    border-radius: 0;
    -webkit-border-top-right-radius: 50px;
    -webkit-border-bottom-right-radius: 50px;
    -moz-border-radius-topright: 50px;
    -moz-border-radius-bottomright: 50px;
    border-top-right-radius: 50px;
    border-bottom-right-radius: 50px;
  }

  img {
    max-width: 100%;
    height: auto;
  }
  img:hover {
    cursor: pointer;
  }
  .active{
    transform: scale(1.1);
    background-color: green;
  }
</style>
