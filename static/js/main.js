$('.special.cards .image').dimmer({
  on: 'hover'
});
$('.dropdown')
  .dropdown({
    // you can use any ui transition
    transition: 'drop'
  })
;
marginleft_size = $(window).width()*0.1;
$('#cards_window')[0].style.marginLeft = marginleft_size + 'px';

function httpGet(theUrl) {
    var xmlHttp = null;

    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false );
    xmlHttp.send( null );
    return jQuery.parseJSON(xmlHttp.responseText);
}

function getImage (image_text) {
	query = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyDqg-XeDMxRF4xxpYeNCEJJJIOP_tOqEaA&cx=002648031817767718379:kftnyjnbcra&q='+image_text+'&searchType=image&alt=json';
	var randomnumber=Math.floor(Math.random()*11)
	image = httpGet(query).items[randomnumber];
	return image;
}

function switchImage (e) {
	console.log(e);
	img_element = e.target.parentElement.parentElement.parentElement.parentElement.children[1];
	image = getImage('kitten');
	console.log(image);
	img_element.src = image.link;
	img_element.alt = image.title;
}