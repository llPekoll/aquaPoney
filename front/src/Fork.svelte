<!-- https://codepen.io/Scrumplex/pen/QOdNee -->
<style>
.gh-ribbon {
	font-family: Helvetica, Arial, sans-serif;
	width: 600px;
	text-align: center;
	font-weight: bold;
	font-size: 0.8em;
	padding: 10px;
	text-decoration: none;
	position: fixed;
	text-shadow: 0 3px 10px rgba(0, 0, 0, 0.5);
	box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
	z-index: 1000;
}

.gh-ribbon:after {
	content: "";
	position: relative;
	display: block;
	top: 8px;
	left: 0;
	width: 600px;
	border: 1px dashed rgba(255, 255, 255, 0.4);
}

.gh-ribbon:before {
	content: "";
	position: relative;
	display: block;
	bottom: 8px;
	left: 0;
	width: 600px;
	border: 1px dashed rgba(255, 255, 255, 0.4);
}

/* .gh-ribbon.white:after {
	content: "";
	position: relative;
	display: block;
	top: 8px;
	left: 0;
	width: 600px;
	border: 1px dashed rgba(0, 0, 0, 0.4);
} */

/* .gh-ribbon.white:before {
	content: "";
	position: relative;
	display: block;
	bottom: 8px;
	left: 0;
	width: 600px;
	border: 1px dashed rgba(0, 0, 0, 0.4);
} */

.gh-ribbon.right {
	top: 15px;
	right: -285px; /* top - right = width / 2 */
	transform: rotate(45deg) translateY(100%);
}


/* $color-red: #aa0000;
$color-red-text: #ffffff;
$color-green: #007200;
$color-green-text: #ffffff;
$color-darkblue: #121621;
$color-darkblue-text: #ffffff;
$color-gray: #6d6d6d;
$color-gray-text: #ffffff;
$color-white: #ffffff;
$color-white-text: #000000; */

.gh-ribbon.red {
	background-color:  #aa0000;
	color: #ffffff;
}

</style>
<a class="gh-ribbon red right" href="https://github.com/llPekoll/aquaPoney" target="_blank">Fork me on GitHub!</a>