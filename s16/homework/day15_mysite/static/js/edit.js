/**
 * Created by willian on 2017/5/9.
 */


$(".edit").click(function(){
    $('#s1').removeClass('hide');
    $('#s2').removeClass('hide');

    var tds = $(this).parent().siblings('td');
    tds.each(function(){
        if($(this).attr('target')) {
            var key = $(this).attr('target');
            var value = $(this).text();
            $("input[name=" + key + "]").val(value);
        }
    })
})


function closeMT(){
    $('#s1').addClass('hide');
    $('#s2').addClass('hide');
}
