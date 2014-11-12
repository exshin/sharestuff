
var created_dates = $('.created.date');
for (i = 0; i < created_dates.length; i++) { 
  date = new Date(created_dates[i].text).toDateString();
  created_dates[i].text = 'Added ' + date;
}

