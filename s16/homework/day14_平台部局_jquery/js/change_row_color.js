/**
 * Created by willian on 2017/4/25.
 */

$("tr").mouseover(function(){
    $(this).css("background-color","green");
});
$("tr").mouseout(function(){
    $(this).css("background-color","");
})