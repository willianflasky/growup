/**
 * Created by willian on 2017/4/18.
 */

function currentDate() {
    //new object
    var da = new Date();

    var year = da.getFullYear();
    //月份从0开始
    var month = da.getMonth()  + 1;
    var day = da.getDate();

    var hours = da.getHours();
    var minutes = da.getMinutes();
    var seconds = da.getSeconds();

    var txt = year + "-" + month + "-" + day + " " + hours+":"+minutes+":"+seconds;

    document.getElementById('h4').innerHTML = txt;
}

setInterval(currentDate,1000);