/**
 * Created by willian on 2017/4/18.
 */


function keyFocus() {
    /*var val = document.getElementById('key').value; */
    var val = $('#key').val();
    if (val == "请输入关键字"){
        /*document.getElementById('key').value = ""; */
        $('#key').val("");
    }
}

function keyBlur() {
    /*var val = document.getElementById('key').value;*/
    var val = $("#key").val();
    if(val.length>0){

    }else{
        /*document.getElementById('key').value = "请输入关键字";*/
        $("#key").val("请输入关键字");
    }
}