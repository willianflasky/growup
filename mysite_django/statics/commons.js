/**
 * Created by willian on 16/11/18.
 */



(function(jq){

    function ErrorMessage(inp,message){
        var tag = document.createElement('span');
        tag.innerText = message;
        inp.after(tag)
    }

    jq.extend({
        valid:function(form){
            jq(form).find(':submit').click(function(){
                jq(form).find('.item span').remove();

                var flag=true;
                jq(form).find(':text,:password').each(function(){

                    var require=$(this).attr('require');

                    if(require) {
                        var val = $(this).val();
                        if (val.length <= 0) {
                            var label = $(this).attr('label');
                            ErrorMessage($(this),label+"不能为空")
                            flag = false;
                            return false;
                        }
                        var minLen=$(this).attr('min-len');
                        if(minLen){
                            var minLenInt=parseInt(minLen);
                            if(val.length<minLenInt){
                                var label = $(this).attr('label');
                                ErrorMessage($(this),label+"长度不能小于"+minLenInt)
                                flag = false;
                                return false;
                            }
                        }
                        var phone=$(this).attr('phone');
                        if(phone){
                            //RE
                            var phoneReg = /^1[3|5|8]\d{9}$/;
                            if(!phoneReg.test(val)){
                                var label = $(this).attr('label');
                                ErrorMessage($(this),label+"格式错误")
                                flag = false;
                                return false;
                            }
                        }
                    }
                })

                return flag;
            });
        }
    });
})(jQuery)