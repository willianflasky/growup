/**
 * Created by willian on 2017/4/25.
 */


$(".menu").click(function(){
    $(this).addClass('active').siblings().removeClass('active');
    var v = $(this).attr('a'); // 1, 2, 3
    $(this).parent().siblings().children("[b='"+ v +"']").removeClass("hide").siblings().addClass("hide");
});

