$(document).ready(function () {
    $('.header__burger').click(function (event) {
        $('.header__burger, .header__menu').toggleClass('active');
        $('body').toggleClass('lock');
    });
});
$(document).ready(function () {
    $('.price__link, .close').click(function (event) {
        $('body').toggleClass('lock');
    });
});