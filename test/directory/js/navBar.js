$(function() {
    $('.nav-title').click(function() {
        $(this).siblings('.nav-content').stop().toggle(500).parent().siblings('.nav-menu').children('.nav-content').hide(500);
    })
})