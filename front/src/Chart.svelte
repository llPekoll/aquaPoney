<script>
    import Line from "svelte-chartjs/src/Line.svelte";
    import { onMount } from "svelte";

    let options = {
        title: {
            display: true,
            text: "Sensor Bme280",
        },
        scales: {
            xAxes: [
                {
                    type: "time",
                    scaleLabel: {
                        labelString: "hours",
                        display: true,
                    },
                },
            ],
            yAxes: [
                {
                    // type: "linear",
                    ticks: {
                        userCallback: function (tick) {
                            return tick.toString() + "C°";
                        },
                    },
                    scaleLabel: {
                        labelString: "Degres°",
                        display: true,
                    },
                },
            ],
        },
    };


    let data;

    onMount(async () => {
        const url = "../sensor/bme280";
        const res = await fetch(url);
        const hours = await res.json();
        const dataHum = [];
        const dataTemp = [];
        hours.forEach((element) => {
            dataHum.push({ x: element.date, y: element.humidity });
            dataTemp.push({ x: element.date, y: element.temperature });
        });
        data = {
            datasets: [
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
                    data: dataHum,
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
                    data: dataTemp,
                },
            ],
        };
    });
</script>

<Line {data} {options} />
