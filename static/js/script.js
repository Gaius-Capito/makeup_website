$(document).ready(function () {
    $('.header__burger').click(function (event) {
        $('.header__burger, .header__menu').toggleClass('active');
        $('body').toggleClass('lock');
    });
});
$(document).ready(function () {
    $('.price__link, .popup__close, .popup__area').click(function (event) {
        $('body').toggleClass('lock');
    });
});