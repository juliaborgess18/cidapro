var path = window.location.pathname;

switch(path)
{
    case "/cliente":
        var item = document.getElementById("sidebar-cliente");
        item.classList.add('active');
        break;
    case "/fornecedor":
        var item = document.getElementById("sidebar-fornecedor");
        item.classList.add('active');
        break;
    case "/produto":
        var item = document.getElementById("sidebar-produto");
        item.classList.add('active');
        break;
    case "/venda":
        var item = document.getElementById("sidebar-venda");
        item.classList.add('active');
        break;
}
