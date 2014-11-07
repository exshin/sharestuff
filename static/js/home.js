margin_right_size = $(window).width()*0.1;
$('#log_in_form')[0].style.marginRight = margin_right_size + 'px';

$('.modal')
  .modal('attach events', '#sign_up_button', 'show')
;
$('.ui.checkbox')
  .checkbox()
;

function hide_modal() {
	$('.modal').modal('hide');
}

function signup() {
	new_user = {}
	new_user['first_name'] = $('#signup_firstname').val();
	new_user['last_name'] = $('#signup_lastname').val();
	new_user['email'] = $('#signup_email').val();
	new_user['username'] = $('#signup_username').val();
	new_user['password'] = $('#signup_password').val();
	new_user['password_confirm'] = $('#signup_password_confirm').val();
	new_user['agree'] = $('#signup_agree')[0].checked;
	if (new_user['password'] != new_user['password_confirm']) {
		console.log('Passwords do not match');
		$('#password_error')[0].style.display = 'block';
		$('#agree_error')[0].style.display = 'none';
		$('#email_error')[0].style.display = 'none';
		$('#signup_password').val('');
		$('#signup_password_confirm').val('');
	} else { 
		if (new_user['agree'] == false) {
			console.log('T&C agreement not checked');
			$('#agree_error')[0].style.display = 'block';
			$('#password_error')[0].style.display = 'none';
			$('#email_error')[0].style.display = 'none';
		} else {
			// ajax post to create new user
			// if ajax response has error (email exists), display $('#email_error')
			$('#password_error')[0].style.display = 'none';
			$('#email_error')[0].style.display = 'none';
			$('#agree_error')[0].style.display = 'none';
			hide_modal();
		}
	}
}

function $insert_new_user(new_user,callback,failback) {
	var req = {
		type: 'POST',
		url: localhost + '/api/new_user',
		data: new_user
	};
	$.ajax(req).done(function(response) {
		console.log(req);
		console.log(response);
		$new_user = new_user;
		callback(response);
	}).fail(function(fail_response) {
		console.log('Issue POSTing new user to Server');
		console.log(fail_response.responseText);
	});
}

