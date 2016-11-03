/**
 * Created by willian on 16/10/25.
 */

(function(jq)){
        jq.extend()({
            valid:function(){
                jq(form).find(':submit').click(function(){
                    var flag=true;
                    jq(form).find(':text,:password').each(function(){

                    });
                    return flag;
                });
            }
        });
}(jQuery);