/**
 * Created by willian on 2017/4/18.


function changeMenu(currentTagObj){
    var contentOjb= currentTagObj.nextElementSibling;
    contentOjb.classList.remove('hide')

    var item_list=document.getElementsByClassName('title');

    for(var i=0;i<item_list.length;i++){
        var loop = item_list[i]
        if(loop != currentTagObj){
            loop.nextElementSibling.classList.add('hide');
        }
    }
}
 */

$('.title').click(function(){
    $(this).next().css('display','block');
    $(this).parent().siblings().children('.c1').css('display','none');
})