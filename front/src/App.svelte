<script lang="ts">
    import  Chart  from "./Chart.svelte";
    import  Fork  from "./Fork.svelte";

    const imgList = ["../static/img/01.png",
                    "../static/img/02.png",
                    "../static/img/03.png",
                    "../static/img/04.png",
                    "../static/img/05.png"];

    let imgnb = Math.floor(Math.random() * 5);

</script>

<main>
    <Fork />
    <div class='slideshow-wrapper'>
        <h2 class="title">Aquaponics!</h2>
        <img src={imgList[imgnb]} alt="hero pic">
    </div>
    <div class="grid-container">
        <div class="grid-item mmd">
        <p>
            Cosntruction de notre premier system aquaponic
            avec de la Zéolithe pour le Substrat,
            Raspbery pour avoir un access internet au Arduino
            pour la gestion des capteur et relai eletrique. 
        </p>
            <Chart />
        <p>
            Stack -> Nginx, Docker, Python, Raspberry, Svelte
        </p>
        </div>
        <div class="grid-item jose">
            <blockquote class="twitter-tweet"><p lang="und" dir="ltr">Day 4 <a href="https://twitter.com/hashtag/aquqponics?src=hash&amp;ref_src=twsrc%5Etfw">#aquqponics</a> <a href="https://t.co/jjPOqaUqJm">pic.twitter.com/jjPOqaUqJm</a></p>&mdash; peko (@llpekoll) <a href="https://twitter.com/llpekoll/status/1375085356924735495?ref_src=twsrc%5Etfw">March 25, 2021</a></blockquote>
            <blockquote class="twitter-tweet"><p lang="und" dir="ltr">Day 3 <a href="https://twitter.com/hashtag/aquaponics?src=hash&amp;ref_src=twsrc%5Etfw">#aquaponics</a> <a href="https://t.co/EcAHraiGls">https://t.co/EcAHraiGls</a> <a href="https://t.co/mQ41C9l0p9">pic.twitter.com/mQ41C9l0p9</a></p>&mdash; peko (@llpekoll) <a href="https://twitter.com/llpekoll/status/1374779404333760515?ref_src=twsrc%5Etfw">March 24, 2021</a></blockquote>
            <blockquote class="twitter-tweet"><p lang="und" dir="ltr">Day2 <a href="https://twitter.com/hashtag/aquaponics?src=hash&amp;ref_src=twsrc%5Etfw">#aquaponics</a> <a href="https://t.co/0BxXsSF7LK">pic.twitter.com/0BxXsSF7LK</a></p>&mdash; peko (@llpekoll) <a href="https://twitter.com/llpekoll/status/1374414715661688844?ref_src=twsrc%5Etfw">March 23, 2021</a></blockquote>
            <blockquote class="twitter-tweet"><p lang="en" dir="ltr">My first aquaponic system <a href="https://t.co/TGq3sNmqnT">pic.twitter.com/TGq3sNmqnT</a></p>&mdash; peko (@llpekoll) <a href="https://twitter.com/llpekoll/status/1374035054658269187?ref_src=twsrc%5Etfw">March 22, 2021</a></blockquote>
        </div>
    </div>
</main>

<style>
    .slideshow-wrapper {
        position:relative;
        float: left;
        height: 450px;
        width: 100%;
    }
    .title {
        position: absolute;
        left: 0;
        right: 0;
        text-align: center;
        color: white;
        text-transform: uppercase;
        font-size: 4em;
        font-weight: 100;
        z-index: 99;
        top: 180px;
    }
    .slideshow-wrapper:before {
        content: '';
        position:absolute;
        top:0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(to bottom, rgba(0,0,0,0) 0%,rgba(0,0,0,.7) 100%);
        z-index: 1;
    }
    blockquote.twitter-tweet {
        display: inline-block;
        font-family: "Helvetica Neue", Roboto, "Segoe UI", Calibri, sans-serif;
        font-size: 12px;
        font-weight: bold;
        line-height: 16px;
        border-color: #eee #ddd #bbb;
        border-radius: 5px;
        border-style: solid;
        border-width: 1px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.15);
        margin: 10px 5px;
        padding: 0 16px 16px 16px;
        max-width: 468px;
    }

    blockquote.twitter-tweet p {
        font-size: 16px;
        font-weight: normal;
        line-height: 20px;
    }

    blockquote.twitter-tweet a {
        color: inherit;
        font-weight: normal;
        text-decoration: none;
        outline: 0 none;
    }

    blockquote.twitter-tweet a:hover,
    blockquote.twitter-tweet a:focus {
        text-decoration: underline;
    }
    .mmd{
        padding-left:40px;
        padding-right:20px;
    }
    .jose{
        height: 600px;
        overflow: scroll;
    }
    img{
        width:100%;
        height: 450px;
    }
    .grid-container {
        width: 100%;
        display: grid;
        grid-column-gap: 20px;
        grid-row-gap: 20px;
        grid-template-columns: 70% 20%;
        }
    main {
        text-align: center;
        width: 100%;
    }

</style>