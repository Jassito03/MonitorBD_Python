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
    setInterval(bitacorasGraph, 5000);
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
    const dataEstructuraFisica = await fetchBitacoras();
    
    const nombres = dataEstructuraFisica['Nombre']
    const estados = dataEstructuraFisica['Estado']
    const bytes = dataEstructuraFisica['bytes']

    let traces = [];
    const indices = Object.keys(nombres);

    indices.forEach(index =>{
        const nombre = nombres[index];
        const estado = estados[index];
        const tamanioBytes = bytes[index];
        
        const color = estado == 'CURRENT' ? 'green' : 'red';
        var trace = {x: [index], y: [tamanioBytes], name: `${index} - ${nombre}`,type: 'bar', marker:{ color: color } };
        traces.push(trace);
    });

    var layout = { xaxis:{title:'Indice Archivos'}, yaxis:{title:'Tamaño en Bytes'}, barmode:'group'};

    Plotly.newPlot('graph_bitacoras', traces, layout);
    
}