function profile_settings (id) {
	var display = document.getElementById(id).style.display;

	if (display == 'none')
		document.getElementById(id).style.display = 'block';

	else
		document.getElementById(id).style.display = 'none';
}

function confirm_sponsor (id) {
	var display = document.getElementById(id).style.display;

	if (display == 'none') 
		document.getElementById(id).style.display = 'block';

	else 
		document.getElementById(id).style.display = 'none';
}
