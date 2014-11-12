$('.modal')
  .modal('attach events', '#add_button', 'show')
;
$('.ui.checkbox')
  .checkbox()
;

var created_dates = $('.created.date');
for (i = 0; i < created_dates.length; i++) { 
    date = new Date(created_dates[i].text).toDateString();
    created_dates[i].text = 'Added ' + date;
}




function httpGet(theUrl) {
    var xmlHttp = null;

    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false );
    xmlHttp.send( null );
    return jQuery.parseJSON(xmlHttp.responseText);
}

function getImage (image_text) {
	query = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyDqg-XeDMxRF4xxpYeNCEJJJIOP_tOqEaA&cx=002648031817767718379:kftnyjnbcra&q='+image_text+'&searchType=image&alt=json';
	image = httpGet(query).items[0];
	return image;
}


function new_item() {
	// get item form data and insert
	new_item = {}
	new_item['item_name'] = $('#item_name').val();
	new_item['item_category'] = $('#item_category').val();
	new_item['item_description'] = $('#item_description').val();
	new_item['item_image_url'] = $('#item_image_url').val();
	new_item['all_can_view'] = $('#item_view_anyone')[0].checked;
	if (new_item['item_image_url'] == '') {
		image = getImage(new_item['item_name']);
		console.log(image);
		if (image) {
			new_item['item_image_url'] = image.link;
		} else {
			new_item['item_image_url'] = '';
		}
		
	}
	// insert new item
	console.log(new_item);
	$insert_new_item(new_item, function(response) {
		console.log(response);
		if (response) {
			$('#new_item_form')[0].reset();
		}
	})
	
}


function $insert_new_item(new_item,callback,failback) {
	// Create a new user
	var req = {
		type: 'POST',
		url: $SCRIPT_ROOT + '/api/new_item',
		data: new_item
	};
	$.ajax(req).done(function(response) {
		console.log(req);
		console.log(response);
		$new_item = new_item;
		callback(response);
	}).fail(function(fail_response) {
		console.log('Issue POSTing new user to Server');
		console.log(fail_response.responseText);
	});
}