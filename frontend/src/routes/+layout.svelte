<div id="main-wrapper"><slot /></div>
<style>
    :global(*){
        margin: 0;
        padding: 0;
        color:white;
        font-family: Arial, Helvetica, sans-serif;
        transition: cubic-bezier(0.55, 0.055, 0.675, 0.19);
    }
    :global(body){
        background-color: #24292E;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
    }
    #main-wrapper{
        width: 100%;
        height: 100%;
    }
</style>