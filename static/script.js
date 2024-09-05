document.addEventListener("DOMContentLoaded", async function(){
    await tablespacesGraph()
    await updateGraph();
    // Actualiza el gráfico cada 5 segundos
    setInterval(updateGraph, 5000);
    setInterval(tablespacesGraph, 60000);
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
    console.log(dataTablespaces)
    return dataTablespaces;
}

async function tablespacesGraph(){
    const dataTablespaces = await fetchTablespaces();

    const nombres = dataTablespaces['Nombres'];
    console.log(dataTablespaces['Nombres']);
    const tamanio_total = dataTablespaces['Tamanio total'];
    console.log(dataTablespaces['Tamanio Total']);
    const memoria_usada = dataTablespaces['Memoria Usada'];
    console.log(dataTablespaces['Memoria Usada']);
    const memoria_libre = dataTablespaces['Memoria libre'];
      
      var trace2 = {x: Object.values(nombres), y: Object.values(memoria_libre), name: 'Memoria Libre (MB)', type: 'bar'};
      var trace1 = {x: Object.values(nombres), y: Object.values(memoria_usada), name: 'Memoria Usada (MB)',type: 'bar'};
      
      var data = [trace1, trace2];
      
      var layout = {barmode: 'stack'};
      Plotly.newPlot('graph_tablespaces', data, layout);
      
     /*
      var trace1 = {
        x: ['giraffes', 'orangutans', 'monkeys'],
        y: [1800, 14, 23],
        name: 'SF Zoo',
        type: 'bar'
      };
      
      var trace2 = {
        x: ['giraffes', 'orangutans', 'monkeys'],
        y: [1750, 18, 29],
        name: 'LA Zoo',
        type: 'bar'
      };
      
      var data = [trace2, trace1];
      
      var layout = {barmode: 'stack'};
      
      Plotly.newPlot('graph_tablespaces', data, layout);*/
}