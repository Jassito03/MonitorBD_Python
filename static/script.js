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
    /*
        Función que se ejecuta cuando la página ha cargado completamente.
        Llama a las funciones para graficar los tablespaces, las bitácoras y los datos de caché.
        Además, establece intervalos para actualizar los gráficos periódicamente.
    */

    await tablespacesGraph();  // Inicializa el gráfico de los tablespaces
    await updateGraph();       // Inicializa el gráfico de las lecturas y tasa de hit
    await bitacorasGraph();    // Inicializa el gráfico de las bitácoras (redo logs)

    // Actualiza el gráfico de lecturas y tasa de hit cada 5 segundos
    setInterval(updateGraph, 5000);

    // Actualiza el gráfico de tablespaces cada minuto
    setInterval(tablespacesGraph, 60000);

    // Actualiza el gráfico de bitácoras cada 5 segundos
    setInterval(bitacorasGraph, 5000);
});

async function fetchData() {
    /*
        Función para obtener datos del buffer caché.
        Realiza una petición a la ruta '/data' del servidor para obtener
        la tasa de hits, total de lecturas lógicas y físicas en formato JSON.
    */
    const response = await fetch('/data');
    const data = await response.json();
    return data;
}

async function updateGraph() {
    /*
        Función para actualizar el gráfico que muestra la tasa de hits, 
        lecturas físicas y lecturas lógicas del buffer caché.
        Usa los datos obtenidos a través de fetchData() y los dibuja en un gráfico usando Plotly.
    */
    const data = await fetchData();
    
    const tasa_hits = data["tasa_hits"];    
    const lecturas_fisicas = data["lecturas_fisicas"];
    const lecturas_logicas = data["lecturas_logicas"];

    // Definir los trazos para el gráfico
    const trace1 = { x: tasa_hits, y: Object.values(tasa_hits), name: 'Tasa de Hit', type: 'Scatter and Lines' };
    const trace2 = { x: lecturas_fisicas, y:  Object.values(lecturas_fisicas), name: 'Lecturas Físicas', type: 'Scatter and Lines' };
    const trace3 = { x: lecturas_logicas, y:  Object.values(lecturas_logicas), name: 'Lecturas Lógicas', type: 'Scatter and Lines' };

    // Definir el diseño del gráfico
    const layout = { title: 'Tasa de Hit y Lecturas', xaxis: { title: 'Segundos' }, yaxis: { title: 'Valores' } };

    // Graficar los datos usando Plotly
    Plotly.newPlot('graph', [trace1, trace2, trace3], layout);
    
    // Actualizar los valores mostrados en el DOM
    document.getElementById('lecturas_logicas').textContent = lecturas_logicas[Object.keys(lecturas_logicas)[Object.keys(lecturas_logicas).length - 1]];
    document.getElementById('lecturas_fisicas').textContent = lecturas_fisicas[Object.keys(lecturas_fisicas)[Object.keys(lecturas_fisicas).length - 1]];
    document.getElementById('tasa_hit').textContent = tasa_hits[Object.keys(tasa_hits)[Object.keys(tasa_hits).length - 1]];
}

async function fetchTablespaces() {
    /*
        Función para obtener la información de los tablespaces:
        Nombre, memoria usada y memoria libre
        Realiza una petición a la ruta '/tablespaces' del servidor y devuelve los datos en formato JSON.
    */
    const responseTablespace = await fetch('/tablespaces');
    const dataTablespaces = await responseTablespace.json();
    return dataTablespaces;
}

async function tablespacesGraph(){
    /*
        Función para graficar la información de los tablespaces.
        Usa los datos obtenidos de fetchTablespaces() para generar un gráfico de barras apiladas 
        que muestra la memoria usada y libre en cada tablespace.
    */
    const dataTablespaces = await fetchTablespaces();

    const nombres = dataTablespaces['Nombres'];
    const memoria_usada = dataTablespaces['Memoria Usada'];
    const memoria_libre = dataTablespaces['Memoria Libre'];

    // Definir los trazos para el gráfico
    var trace1 = {x: Object.values(nombres), y: Object.values(memoria_usada), name: 'Memoria Usada (MB)',type: 'bar'};
    var trace2 = {x: Object.values(nombres), y: Object.values(memoria_libre), name: 'Memoria Libre (MB)', type: 'bar'};
    
    var data = [trace1, trace2];
    
    // Definir el diseño del gráfico
    var layout = { xaxis:{title:'Nombre Tablespaces'}, yaxis:{title:'Tamaño en MB'}, barmode: 'stack'};

    // Graficar los datos usando Plotly
    Plotly.newPlot('graph_tablespaces', data, layout);
}

async function fetchBitacoras() {
    /*
        Función para obtener información sobre las bitácoras (redo logs).
        Realiza una petición a la ruta '/bitacoras' del servidor y devuelve los datos en formato JSON.
    */
    console.log("Fetch bitacoras");
    const responseEstructuraFisca = await fetch('/bitacoras');
    const dataEstructuraFisica = await responseEstructuraFisca.json();
    return dataEstructuraFisica;
}

async function bitacorasGraph(){
    /*
        Función para graficar el estado de las bitácoras (redo logs).
        Usa los datos obtenidos de fetchBitacoras() para generar un gráfico de barras 
        que muestra el tamaño de cada bitácora y su estado (CURRENT o INACTIVO).
    */
    const dataEstructuraFisica = await fetchBitacoras();
    
    const nombres = dataEstructuraFisica['Nombre'];
    const estados = dataEstructuraFisica['Estado'];
    const bytes = dataEstructuraFisica['bytes'];

    let traces = [];
    const indices = Object.keys(nombres);

    // Generar un trazo para cada bitácora en función de su estado
    indices.forEach(index => {
        const nombre = nombres[index];
        const estado = estados[index];
        const tamanioBytes = bytes[index];
        
        // Asignar color según el estado de la bitácora
        const color = estado == 'CURRENT' ? 'green' : 'red';

        // Crear un trazo para la bitácora
        var trace = {x: [index], y: [tamanioBytes], name: `${index} - ${nombre}`,type: 'bar', marker:{ color: color } };
        traces.push(trace);
    });

    // Definir el diseño del gráfico
    var layout = { xaxis:{title:'Indice Archivos'}, yaxis:{title:'Tamaño en Bytes'}, barmode:'group'};

    // Graficar los datos usando Plotly
    Plotly.newPlot('graph_bitacoras', traces, layout);
}
