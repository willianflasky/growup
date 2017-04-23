/**
 * Created by willian on 2017/4/18.
 */


//菜单选择
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