<script>
  import Line from "svelte-chartjs/src/Line.svelte"
  import axios from 'axios';
import { onMount } from 'svelte';

   let options = {
    title: {
      display: true,
      text: 'Sensor Bme280'
    },
    scales: {
      xAxes: [
        {
          type: 'time',
          position: 'bottom',
          ticks: {
            userCallback: function (tick) {
                return tick.toString() + 'h';
            }
          },
          scaleLabel: {
            labelString: 'hours',
            display: true
          }
        }
      ],
      yAxes: [
        {
          type: 'linear',
          ticks: {
            userCallback: function (tick) {
              return tick.toString() + 'C°';
            }
          },
          scaleLabel: {
            labelString: 'Degres°',
            display: true
          }
        }
      ]
    }
  };

	
const url = '../sensor/bme280'



// Axios Test Data.
// axiosTest(url).then(function(axiosTestResult) {
//   console.log('response.JSON:', {
//     message: 'Request received',
//     data: axiosTestResult.data
//   })
// })

	let photos = [];
	let hours = [];
	let data;
	onMount(async () => {
		const res = await fetch(url);
		console.log("res.json()")
		hours = await res.json();
		data = {datasets: [
		{
			label: "Humidity",
			fill: true,
			lineTension: 0.3,
			backgroundColor: "rgba(155, 155, 255, .3)",
			borderColor: "rgb(155, 155, 255)",
			borderCapStyle: "butt",
			borderDash: [],
			borderDashOffset: 0.0,
			borderJoinStyle: "miter",
			pointBorderColor: "rgb(205, 130,1 58)",
			pointBackgroundColor: "rgb(255, 255, 255)",
			pointBorderWidth: 5,
			pointHoverRadius: 4,
			pointHoverBackgroundColor: "rgb(0, 0, 0)",
			pointHoverBorderColor: "rgba(220, 220, 220,1)",
			pointHoverBorderWidth: 2,
			pointRadius: 1,
			pointHitRadius: 10,
			data: [{
				x: hours[0]['date'],
				y: hours[0]['humidity']
			}, {
				x: hours[1]['date'],
				y: 7
			}, {
				x: hours[3]['date'],
				y: 5.3
			}, {
				x: hours[4]['date'],
				y: 8.9
			}, {
				x: hours[5]['date'],
				y: 7
			}, {
				x: hours[6]['date'],
				y: 15
			},{
				x: hours[7]['date'],
				y: 24
			}]
		},
		{
			label: "temperature",
			fill: true,
			lineTension: 0.3,
			backgroundColor: "rgba(184, 185, 210, .3)",
			borderColor: "rgb(35, 26, 136)",
			borderCapStyle: "butt",
			borderDash: [],
			borderDashOffset: 0.0,
			borderJoinStyle: "miter",
			pointBorderColor: "rgb(35, 26, 136)",
			pointBackgroundColor: "rgb(255, 255, 255)",
			pointBorderWidth: 5,
			pointHoverRadius: 4,
			pointHoverBackgroundColor: "rgb(0, 0, 0)",
			pointHoverBorderColor: "rgba(220, 220, 220, 1)",
			pointHoverBorderWidth: 2,
			pointRadius: 1,
			pointHitRadius: 10,
			data: [{
				x: hours[0]['date'],
				y: 22.2
			}, {
				x: hours[1]['date'],
				y: 23.5
			}, {
				x: hours[2]['date'],
				y: 25.2
			}, {
				x: hours[3]['date'],
				y: 31
			}, {
				x: hours[4]['date'],
				y: 21
			}, {
				x: hours[5]['date'],
				y: 23
			},{
				x: hours[6]['date'],
				y: 23
			}]
		}
		]
	};
	});
  

// async function axiosTest() {
//     const response = await axios.get(url)
// 	console.log("response")
// 	console.log(response)
//     return response.data
// }
// axiosTest()
</script>
<Line {data} {options}/>
		<!-- this block renders when photos.length === 0 -->
	<!-- <Line {data} {options}/> -->
	
  