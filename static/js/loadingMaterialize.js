$(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.materialboxed').materialbox();
    $('.modal').modal();
    $(".dropdown-trigger").dropdown();
    $('.parallax').parallax();
    $('.carousel').carousel();
    $('.collapsible').collapsible();
    $('.carousel.carousel-slider').carousel({
        fullWidth: true,
        indicators: true
    });
    $('.fixed-action-btn').floatingActionButton();
    $('.tooltipped').tooltip();
});