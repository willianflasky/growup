/**
 * Created by willian on 2017/4/18.
 */


function keyFocus() {
    //console.log('获取焦点');
    var val = document.getElementById('key').value;
    if (val == "请输入关键字"){
        document.getElementById('key').value = "";
    }
}

function keyBlur() {
    //console.log('失去焦点');
    var val = document.getElementById('key').value;
    if(val.length>0){

    }else{
        document.getElementById('key').value = "请输入关键字";
    }

}