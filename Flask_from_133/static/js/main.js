$(function () {
    $('.skill-progress span').each(function (item) {
        $(this).animate({
            'width' : $(this).data('width')
        },1000)
    })
})
