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
}

// Actualiza el gráfico cada 5 segundos
setInterval(updateGraph, 5000);

// Llamar a la función una vez para cargar inicialmente
updateGraph();