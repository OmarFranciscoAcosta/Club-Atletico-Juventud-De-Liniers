let dataTable;
let dataTableIsInitialized = false;
// Configuraciones del DataTable
//
const dataTableOptions = {
    paging: false,
    scrollCollapse: true,
    //Tamaño de la tabla
    //
    scrollY: "250px",
    lengthMenu: [5, 10, 15, 20, 100, 200, 500],
    columnDefs: [
        { className: "centered", targets: [1, 2, 3, 4, 5, 6] },
        { orderable: false, targets: [1, 2, 3, 4, 5, 6, 7] },
        { searchable: false, targets: [3, 4, 5, 6, 7] },
        // Tamaño de las columnas
        //
        { width: "40%", targets: [7] },
        { width: "20%", targets: [1] },
        { width: "10%", targets: [0] }
    ],
    pageLength: 3,
    destroy: true,
    // Configuracion del idioma de las opciones
    //
    language: {
        lengthMenu: "Mostrar _MENU_ registros por página",
        zeroRecords: "Ningún Socio encontrado",
        info: "Mostrando de _START_ a _END_ de un total de _TOTAL_ registros",
        infoEmpty: "Ningún Socio encontrado",
        infoFiltered: "(filtrados desde _MAX_ registros totales)",
        search: "Buscar Socio:",
        loadingRecords: "Cargando...",
        paginate: {
            first: "Primero",
            last: "Último",
            next: "Siguiente",
            previous: "Anterior"
        }
        
    }
};
