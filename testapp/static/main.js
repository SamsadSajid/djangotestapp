window.onload = function() {
  var redirectToUrl = function() {
    var new_url = document.getElementById('url').value;
    window.location.href = new_url;
  }

  var el = document.getElementById("submitButton");
   el.addEventListener("click", redirectToUrl, false);
  if (el.addEventListener) {
   } else {
       el.attachEvent('onclick', redirectToUrl);
   }
}
