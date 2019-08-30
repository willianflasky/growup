/**
 * Created by willian on 2017/4/25.
 */


$("#mylight").click(function(){
    if($("#mylight").hasClass('off')){
        $("#mylight").removeClass('off');
    }else{
        $("#mylight").addClass('off');
    }
})