$(document).ready(function () {
    $('.novel-card-cover-box').hover(function (event) {
        console.log(event.target);
        $(event.target).next().addClass('card-overlay-appear');
    }, function (event) {
        $(event.target).next().removeClass('card-overlay-appear');
    });
});