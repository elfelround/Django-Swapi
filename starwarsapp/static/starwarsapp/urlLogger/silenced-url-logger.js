var currentdate = new Date().toLocaleString();
var currentwindow = window.location.href;

//test objects

//looping functions

function javascriptToLi(value1, key1) {
  var ul = document.getElementById("list");
  var li = document.createElement("li");
  li.appendChild(document.createTextNode(value1));
  li.setAttribute("id", key1);
  ul.appendChild(li);
  //alert(li.id);
}

function loopObjectToLi(p) {
  for (var key in p) {
    if (p.hasOwnProperty(key)) {
      var value1 = p[key]
      var key1 = key
      javascriptToLi(value1, key1);
        //document.write(key + " -> " + p[key]);
    }
}
}

//pretty much unmodified W3 version
function setCookie(cname,cvalue,exdays) {
  var d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  var expires = "expires=" + d.toGMTString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

//pretty much unmodified W3 version
function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

//totally modified
function checkCookie(a) {
  var cookieinstantiation=getCookie(a);
  if (cookieinstantiation != "") {
    //add value
    //document.write("cookie exists")

    //THIS SHOULD BE MODULARIZED ONTO AN EXTERNAL FUNCTION THAT IS PASSED AS ARGUMENT
    var arr = JSON.parse(cookieinstantiation);
    arr[currentdate] = window.location.href;
    var myJSONtostore = JSON.stringify(arr);
    setCookie("urls", myJSONtostore);

    //var myJSONtoread = JSON.stringify(arr, null, "</br>");
    //document.write(myJSONtoread)


    //loopObjectToLi(arr);
    //case yes
    //alert("Welcome again " + user);
  } else {
     //setCookie()
     //document.write("cookie doesn't exist")
     var obj = {};
     obj[currentdate] = currentwindow;
     var myJSONtostore = JSON.stringify(obj);
     setCookie(a, myJSONtostore);
     //bug, this wont run if cookie has been instantiated with an empty object instead of an empty string
  }
}

function resetCookie(a) {
  var cookieinstantiation=getCookie(a);
  if (cookieinstantiation != "") {

     //document.write("resetting cookie")
     var empty = "";

     setCookie(a, empty);
     location = location
  } else {
     //document.write("cookie doesn't exist, creating it")
  }
}

checkCookie("urls")

//********************UNCOMMENT FOR FUNCTIONALITY
//resetCookie("urls");
//********************
//DELETE COOKIE document.cookie = "urls=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
//********************
