var page = require('webpage').create();
page.open('https://www.doxue.com', function(status) {
  console.log('Status' + status);
  if (status === 'success') {
    page.render('douxue.png');
  }
  phantom.exit();
});
