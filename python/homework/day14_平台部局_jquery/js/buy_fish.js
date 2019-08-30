/**
 * Created by willian on 2017/4/27.
 */


function toleft(){
    $("#fish option:selected").appendTo("#fruit");
}

function totalleft(){
    $("#fish option").appendTo("#fruit");
}

function toright(){
    $("#fruit option:selected").appendTo("#fish");
}

function totalright(){
    $("#fruit option").appendTo("#fish");

}