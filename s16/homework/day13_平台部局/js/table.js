/**
 * Created by willian on 2017/4/18.
 */



function checkAll(){
    var inpList = document.getElementsByClassName('option1');
    for(var i=0;i<inpList.length;i++){
        var inp = inpList[i];
        inp.checked=true;
    }
}

function removeAll(){
    var inpList = document.getElementsByClassName('option1');
    for(var i=0;i<inpList.length; i++){
        var inp = inpList[i];
        inp.checked=false;
    }
}

function reverseAll(){
    var inpList=document.getElementsByClassName('option1');
    for(var i=0;i<inpList.length; i++){
        var inp = inpList[i];
        if(inp.checked){
            inp.checked = false;
        }else {
            inp.checked = true;
        }
    }
}