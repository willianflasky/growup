/**
 * Created by willian on 2017/4/18.



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

*/


$("#checkAll").click(function(){
    $(".option1").prop('checked',true);
})

$("#removeAll").click(function(){
    $(".option1").prop("checked",false);
})

$("#reverseAll").click(function(){
    $(".option1").each(function(){
        /*
        var v = $(this).prop('checked')
        if(v){
            $(this).prop('checked',false);
        }else{
            $(this).prop('checked',true);
        }
        */
        $(this).prop('checked') ? $(this).prop('checked',false) : $(this).prop('checked',true);
    })
})