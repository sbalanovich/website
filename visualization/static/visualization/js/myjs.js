$('select').addClass('shadow_select');
$('select').wrap('<span class="select-wrapper" />');
$('.select-wrapper').width($(this).width());

$('select').focusin(function() {
    $('.select-wrapper').addClass('webkit_specific');
});

$('select').focusout(function() {
    $('.select-wrapper').removeClass('webkit_specific');
});

$("#largeTextbox").keyup(function(event){
    if(event.keyCode == 13){
        $("#submitButton").click();
    }
});

function show(text){
	output = "Crunching the numbers..."
	document.getElementById("scoreOutput").innerHTML = output;
	$.ajax({
        type: 'POST',
        url: '/test_results/',
        data: {
        	title : text
        },
        success: function (data) {
			//Insert Regression function Here
			output = "Woo Hoo! It looks like when this post settles down, it will have a score of: "
			document.getElementById("scoreOutput").innerHTML = output;
			document.getElementById("scoreValue").innerHTML = data;
        },
        error: function(request, status, error) {
            alert(request.responseText);
        }
    });
    return false;
}