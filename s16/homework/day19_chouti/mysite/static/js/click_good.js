/**
 * Created by willian on 2017/6/7.
 */


$(".Favor").click(function(ths){
    var top = 10;
    var left = 50;
    var op =1 ;
    var fontSize =18;
    var tag = $("<span class='tmpspan'></span>").css({"postion":"obsolute","top":top+"px","left":left+"px","opacity":op,"font-size":fontSize+"px","color":"red"});
    tag.text("+1")
    $(this).parent().append(tag);

    var interval = setInterval(function(){
        top -= 10;
        left += 10;
        fontSize += 5;
        op -= 0.1;

        tag.css({"postion":"obsolute","top":top+"px","left":left+"px","opacity":op,"font-size":fontSize+"px","color":"green"})

        if(op <= 0.1){
            clearInterval(interval);
            $('.tmpspan').remove();
        }
    },50);
})