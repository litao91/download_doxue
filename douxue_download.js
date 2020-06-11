var steps = [];
var loadInProgress = false;

var webPage = require('webpage');
var page = webPage.create();
var page = require('webpage').create();
page.settings.userAgent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36';
page.settings.javascriptEnabled = true;
page.settings.loadImages = false;//Script is much faster with this field set to false
phantom.cookiesEnabled = true;
phantom.javascriptEnabled = true;

console.log('All settings loaded, start with execution');
page.onConsoleMessage = function (msg) {
  console.log(msg);
};

steps = [

  //Step 1 - Open Amazon home page
  function () {
    console.log('Step 1 - open doxue login page')
    page.open("https://passport.doxue.com/login", function (status) {
      console.log("login page status: " + status);
    });
  },
  //Step 2 - login
  function () {
    console.log('Step 2 - submit the login info');
    page.evaluate(function () {
      document.getElementById("login_phone").value = "18612747889";
      document.getElementById("pwd").value = "";
      document.getElementById("submit").submit();
    });
  },
];

interval = setInterval(executeRequestsStepByStep, 50);

function executeRequestsStepByStep() {
  if (loadInProgress == false && typeof steps[testindex] == "function") {
    console.log("step " + (testindex + 1));
    steps[testindex]();
    testindex++;
  }
  if (typeof steps[testindex] != "function") {
    console.log("test complete!");
    phantom.exit();
  }
}

/**
 * These listeners are very important in order to phantom work properly. Using these listeners, we control loadInProgress marker which controls, weather a page is fully loaded.
 * Without this, we will get content of the page, even a page is not fully loaded.
 */
page.onLoadStarted = function () {
  loadInProgress = true;
  console.log('Loading started');
};
page.onLoadFinished = function () {
  loadInProgress = false;
  console.log('Loading finished');
};
page.onConsoleMessage = function (msg) {
  console.log(msg);
};
