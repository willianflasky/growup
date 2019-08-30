/**
 * Created by willian on 2017/4/19.
 */

/*
function Favor(ths){
    // ths ==> this表示当前触发事件的标签.
    var top = 10;
    var left = 50;
    var op =1 ;
    var fontSize =18;
    var tag = document.createElement('span');
    tag.innerText="+1"
    tag.style.position = 'obsolute';
    tag.style.top = top + 'px';
    tag.style.left = left + 'px';
    tag.style.opacity = op;
    tag.style.fontSize = fontSize + 'px';
    ths.parentElement.appendChild(tag);

    //处理span标签变大,透明,消失.
    var interval = setInterval(function(ths){
        top -= 10;
        left += 10;
        fontSize += 5;
        op -= 0.1;

        tag.style.top = top + 'px';
        tag.style.left = left + 'px';
        tag.style.opacity = op;
        tag.style.fontSize = fontSize + 'px';

        if(op <= 0.1){
            clearInterval(interval);
            ths.parentElement.removeChild(tag);
        }
    },50);
}

*/

$(".Favor").click(function(){
    var top = 10;
    var left = 50;
    var op =1 ;
    var fontSize =18;
    var tag = $("<span></span>").css({"postion":"obsolute","top":top+"px","left":left+"px","opacity":op,"font-size":fontSize+"px","color":"red"});
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
            $(this).parent().children('span').remove();
        }
    },50);
})
