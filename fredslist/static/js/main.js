$(document).ready(function(){

    $('#list').click(function(){
        $('.thumb').css("display","none");
    });

    $('#thumb').click(function(){

        $('.thumb').css("display","inline-block");
    });

    $('#gallery').click(function(){
        $('.thumb').css("display","none").addClass("intro");
    });

});
