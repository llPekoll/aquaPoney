<script lang="ts">
    import  Chart  from "./Chart.svelte";
    import  Fork  from "./Fork.svelte";
	const imgList = ["../static/img/01.png",
					"../static/img/02.png",
					"../static/img/03.png",
					"../static/img/04.png",
					"../static/img/05.png"]
	let imgnb = Math.floor(Math.random() * 5);
	
</script>

<main>
    <Fork />
	<img src={imgList[imgnb]} alt="hero pic">
    <h1>Aquaponics!</h1>
	<div class="grid-container">
		<div class="grid-item mmd">
		<p>
			Cosntruction de notre premier system aquaponic
			avec de la Zéolithe pour le Substrat,
			Raspbery pour avoir un access internet au arduino
			Arduino pour la gestion des capteur et relai eletrique. 
		</p>
			<Chart />
			<p>
			Stack -> Nginx, Docker, Python, Raspberry, Svelte
			</p>
		</div>
		<div class="grid-item jose">
			<blockquote class="twitter-tweet"><p lang="und" dir="ltr">Day 3 <a href="https://twitter.com/hashtag/aquaponics?src=hash&amp;ref_src=twsrc%5Etfw">#aquaponics</a> <a href="https://t.co/EcAHraiGls">https://t.co/EcAHraiGls</a> <a href="https://t.co/mQ41C9l0p9">pic.twitter.com/mQ41C9l0p9</a></p>&mdash; peko (@llpekoll) <a href="https://twitter.com/llpekoll/status/1374779404333760515?ref_src=twsrc%5Etfw">March 24, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
			<blockquote class="twitter-tweet"><p lang="und" dir="ltr">Day2 <a href="https://twitter.com/hashtag/aquaponics?src=hash&amp;ref_src=twsrc%5Etfw">#aquaponics</a> <a href="https://t.co/0BxXsSF7LK">pic.twitter.com/0BxXsSF7LK</a></p>&mdash; peko (@llpekoll) <a href="https://twitter.com/llpekoll/status/1374414715661688844?ref_src=twsrc%5Etfw">March 23, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
			<blockquote class="twitter-tweet"><p lang="en" dir="ltr">My first aquaponic system <a href="https://t.co/TGq3sNmqnT">pic.twitter.com/TGq3sNmqnT</a></p>&mdash; peko (@llpekoll) <a href="https://twitter.com/llpekoll/status/1374035054658269187?ref_src=twsrc%5Etfw">March 22, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
		</div>
	</div>

</main>

<style>
.mmd{
	padding-left:40px;
	padding-right:20px;
}
.jose{
	height: 600px;
	/* width: 150px; */
	overflow: scroll;
}
img{
    width:100%;
    height: auto;
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
    h1 {
        margin-top:-80px;
        color: white;
        text-transform: uppercase;
        font-size: 4em;
        font-weight: 500;
    }
</style>