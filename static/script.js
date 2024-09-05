/*
Autores:
Nombre: Joseph Piñar Baltodano
ID: 1 1890 0308

Nombre: Abigail Salas Ramírez
ID: 4 0257 0890

Nombre: Gianpablo Moreno Castro
ID: 4 0261 0240
*/

document.addEventListener("DOMContentLoaded", async function(){
    await tablespacesGraph()
    await updateGraph();
    await bitacorasGraph();
    // Actualiza el gráfico cada 5 segundos
    setInterval(updateGraph, 5000);
    // Actualiza el gráfico cada minuto
    setInterval(tablespacesGraph, 60000);
    //Actualizar el gráfico cada minuto
    setInterval(bitacorasGraph, 60000);
})

async function fetchData() {
    const response = await fetch('/data');
    const data = await response.json();
    return data;
}
async function updateGraph() {
    const data = await fetchData();
    
    const tasa_hits = data["tasa_hits"];    
    const lecturas_fisicas = data["lecturas_fisicas"];
    const lecturas_logicas = data["lecturas_logicas"];

    const trace1 = { x: tasa_hits, y: Object.values(tasa_hits), name: 'Tasa de Hit', type: 'Scatter and Lines' };
    const trace2 = { x: lecturas_fisicas, y:  Object.values(lecturas_fisicas), name: 'Lecturas Físicas', type: 'Scatter and Lines' };
    const trace3 = { x: lecturas_logicas, y:  Object.values(lecturas_logicas), name: 'Lecturas Lógicas', type: 'Scatter and Lines' };

    const layout = { title: 'Tasa de Hit y Lecturas', xaxis: { title: 'Segundos' }, yaxis: { title: 'Valores' } };
    Plotly.newPlot('graph', [trace1, trace2, trace3], layout);
    
    document.getElementById('lecturas_logicas').textContent = lecturas_logicas[Object.keys(lecturas_logicas)[Object.keys(lecturas_logicas).length - 1]];
    document.getElementById('lecturas_fisicas').textContent = lecturas_fisicas[Object.keys(lecturas_fisicas)[Object.keys(lecturas_fisicas).length - 1]];
    document.getElementById('tasa_hit').textContent = tasa_hits[Object.keys(tasa_hits)[Object.keys(tasa_hits).length - 1]];
}

async function fetchTablespaces() {
    const responseTablespace = await fetch('/tablespaces');
    const dataTablespaces = await responseTablespace.json();
    return dataTablespaces;
}

async function tablespacesGraph(){
    const dataTablespaces = await fetchTablespaces();

    const nombres = dataTablespaces['Nombres'];
    const memoria_usada = dataTablespaces['Memoria Usada'];
    const memoria_libre = dataTablespaces['Memoria Libre'];

    var trace1 = {x: Object.values(nombres), y: Object.values(memoria_usada), name: 'Memoria Usada (MB)',type: 'bar'};
    var trace2 = {x: Object.values(nombres), y: Object.values(memoria_libre), name: 'Memoria Libre (MB)', type: 'bar'};
    
      
    var data = [trace1, trace2];
      
    var layout = {barmode: 'stack'};
    Plotly.newPlot('graph_tablespaces', data, layout);
}

async function fetchBitacoras() {
    console.log("Fetch bitacoras");
    const responseEstructuraFisca = await fetch('/bitacoras');
    const dataEstructuraFisica = await responseEstructuraFisca.json();
    return dataEstructuraFisica;
}

async function bitacorasGraph(){
    console.log("Fetch bitacoras");
    const dataEstructuraFisica = await fetchBitacoras();
    const nombres = dataEstructuraFisica['Nombres']
    const estados = dataEstructuraFisica['Estados']

    var allLabels = ['1st', '2nd', '3rd', '4th', '5th'];

    var allValues = [
    [38, 27, 18, 10, 7],
    [28, 26, 21, 15, 10],
    [38, 19, 16, 14, 13],
    [31, 24, 19, 18, 8]
    ];

    var ultimateColors = [
    ['rgb(56, 75, 126)', 'rgb(18, 36, 37)', 'rgb(34, 53, 101)', 'rgb(36, 55, 57)', 'rgb(6, 4, 4)'],
    ['rgb(177, 127, 38)', 'rgb(205, 152, 36)', 'rgb(99, 79, 37)', 'rgb(129, 180, 179)', 'rgb(124, 103, 37)'],
    ['rgb(33, 75, 99)', 'rgb(79, 129, 102)', 'rgb(151, 179, 100)', 'rgb(175, 49, 35)', 'rgb(36, 73, 147)'],
    ['rgb(146, 123, 21)', 'rgb(177, 180, 34)', 'rgb(206, 206, 40)', 'rgb(175, 51, 21)', 'rgb(35, 36, 21)']
    ];

    var data = [{
    values: allValues[0],
    labels: allLabels,
    type: 'pie',
    name: 'Starry Night',
    marker: {
        colors: ultimateColors[0]
    },
    domain: {
        row: 0,
        column: 0
    },
    hoverinfo: 'label+percent+name',
    textinfo: 'none'
    },{
    values: allValues[1],
    labels: allLabels,
    type: 'pie',
    name: 'Sunflowers',
    marker: {
        colors: ultimateColors[1]
    },
    domain: {
        row: 1,
        column: 0
    },
    hoverinfo: 'label+percent+name',
    textinfo: 'none'
    },{
    values: allValues[2],
    labels: allLabels,
    type: 'pie',
    name: 'Irises',
    marker: {
        colors: ultimateColors[2]
    },
    domain: {
        row: 0,
        column: 1
    },
    hoverinfo: 'label+percent+name',
    textinfo: 'none'
    },{
    values: allValues[3],
    labels: allLabels,
    type: 'pie',
    name: 'The Night Cafe',
    marker: {
        colors: ultimateColors[3]
    },
    domain: {
        x: [0.52,1],
        y: [0, 0.48]
    },
    hoverinfo: 'label+percent+name',
    textinfo: 'none'
    }];

    var layout = {
    height: 400,
    width: 500,
    grid: {rows: 2, columns: 2}
    };

    Plotly.newPlot('graph_bitacoras', data, layout);
    
}