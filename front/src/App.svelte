<script lang="ts">
	import  Chart  from "./Chart.svelte";
	import  Fork  from "./Fork.svelte";
	
</script>

<main>
	<Fork />
	<h1>Aquaponics!</h1>
<div class="grid-container">
<div class="grid-item">
	Cosntruction de notre premier system aquaponic
	avec de la Zéolithe pour le Substrat,
	Raspbery pour avoir un access internet au arduino
	Arduino pour la gestion des capteur et relai eletrique. 
	<Chart />
	Stack -> Nginx, Docker, Python, Raspberry, Svelte
</div>
<div class="grid-item">
	<blockquote class="twitter-tweet"><p lang="en" dir="ltr">My first aquaponic system <a href="https://t.co/TGq3sNmqnT">pic.twitter.com/TGq3sNmqnT</a></p>&mdash; peko (@llpekoll) <a href="https://twitter.com/llpekoll/status/1374414715661688844?ref_src=twsrc%5Etfw">March 22, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
	<blockquote class="twitter-tweet"><p lang="en" dir="ltr">My first aquaponic system <a href="https://t.co/TGq3sNmqnT">pic.twitter.com/TGq3sNmqnT</a></p>&mdash; peko (@llpekoll) <a href="https://twitter.com/llpekoll/status/1374035054658269187?ref_src=twsrc%5Etfw">March 22, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</div>
</div>

</main>

<style>
.grid-container {
	width: 100%;
  	display: grid;
	grid-column-gap: 20px;
	grid-row-gap: 20px;
	 grid-template-columns: 70% 20%;
}
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}
	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}
	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>