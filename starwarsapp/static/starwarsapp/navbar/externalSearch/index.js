externalsearch = function(e) {
var xhr = new XMLHttpRequest();

xhr.onload = function() {
  if(xhr.status ===200) {
    //var body = xhr.response;
    //b = JSON.stringify(body, null, "</br>");
    //document.write(b);
    //alert(b);
    alert(xhr.responseText);
  }
};

var query = document.getElementById('search-query').value;

xhr.open('GET', 'https://swapi.co/api/people/?search=' + query, true);
xhr.send(null);
};