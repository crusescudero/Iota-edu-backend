// Función para activar y desactivar el menu responsivo
document.addEventListener('DOMContentLoaded', function() {
    const options = {
        'edge': 'right'
    }
    
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);
});

document.addEventListener('DOMContentLoaded', function() {
    const options = {
        'fullWidth': 'true',
        'indicators': 'true',
        'numVisible': 1,
        'duration': 180
    }

    var elems = document.querySelectorAll('.carousel');
    var instances = M.Carousel.init(elems, options);
    var instance = M.Carousel.init({
        fullWidth: true 
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.slider');
    var instances = M.Slider.init(elems,{
      indicators: false,
      interval:2500
    });
}); 


