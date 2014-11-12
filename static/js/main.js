$('.special.cards .image').dimmer({
  on: 'hover'
});

$('.dropdown')
  .dropdown({
    // you can use any ui transition
    transition: 'drop'
  });

$(".dropdown_filter_category").dropdown({
  onChange: function (val) {
    console.log(val);
    var m = $(".card");
    for(var n = 0; n < m.length; n++){
      text = m[n].children[1].children[1].textContent.toLowerCase();
      if ( text.indexOf(val) != -1 ) {
        m[n].style.display = "block";
      } else {
        m[n].style.display = "none";
      }
    };
  }
});


marginleft_size = $(window).width()*0.1;
$('#cards_window')[0].style.marginLeft = marginleft_size + 'px';

// Deal with descriptions with length > 110
descriptions = $('.item_description');
for (i = 0; i < descriptions.length; i++) {
  if (descriptions[i].textContent.length > 115) {
    descriptions[i].textContent = descriptions[i].textContent.substring(0,115) + '...';
  }
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

function filter_search(element) {
  var value = $(element).val().toLowerCase();
  if (value.length > 0) {
    var m = $(".card");
    for(var n = 0; n < m.length; n++){
      text = m[n].children[1].textContent.toLowerCase();
      if ( text.indexOf(value) != -1 ) {
        m[n].style.display = "block";
      } else {
        m[n].style.display = "none";
      }
    };
  } 
  else {
    $(".card").show();
  };
};







