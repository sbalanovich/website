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
			[score, prob] = data
			document.getElementById("scoreValue").innerHTML = score;
			output2 = "So how was this done? Well we used our CLF to predict the probability of your post being popular, which ended up being: "			
			document.getElementById("scoreOutput2").innerHTML = output2;
			document.getElementById("scoreValue2").innerHTML = prob;
			output3 = "Then we ran it through our regression model to predict your score! If you'd like to see more about what we did, check out the links on the left or visit our <a href='http://nbviewer.ipython.org/github/intelligent-dolphins/blob/master/ProcessBook.ipynb'>Process Book</a> "			
			document.getElementById("scoreOutput3").innerHTML = output3;
			output4 = ""
			document.getElementById("scoreOutput4").innerHTML = output4;
        },
        error: function(request, status, error) {
            alert(request.responseText);
        }
    });
    return false;
}