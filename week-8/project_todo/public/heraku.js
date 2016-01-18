'use strict';

var url = 'https://mysterious-dusk-8248.herokuapp.com/todos';
var listItem = document.querySelector("ul");
var newItemInput = document.querySelector('.item-input');
var addNewItemInput = document.querySelector('.addnewitem');
var deleteButton = document.querySelector('.deletebutton');


listItems(updateHtml);


function startRequest(text) {
  postItemToServer(text, textDOM)
}

function listItems(callback) {
  var req = new XMLHttpRequest();
  req.open('GET', url);
  req.send();
  req.onreadystatechange = function () {
    if (req.readyState === 4) {
      var res = JSON.parse(req.response);
      return callback(res);
    }
  };
}

function postItemToServer(text, callback) {
  var req = new XMLHttpRequest();
  req.open('POST', url);
  req.setRequestHeader('Content-Type', 'application/json');
  req.send(JSON.stringify({"text": text}));
  req.onreadystatechange = function () {
    if (req.readyState === 4) {
      var res = JSON.parse(req.response);
      return callback(res);
    }
  };
}

function deleteItem(id, callback) {
  var req = new XMLHttpRequest();
  req.open('DELETE', url + '/' + id);
  req.send();
  req.onreadystatechange = function () {
    if (req.readyState === 4) {
      var res = JSON.parse(req.response);
      return callback(res);
    }
  }
};

function deleteCallBack(res) {
  document.getElementById(res.id).remove();
}


deleteButton.addEventListener("click", function() {
  deleteItem(addNewItemInput.value, deleteCallBack);
});

function updateHtml(res) {
  res.forEach(function(item) {
    if (item.text !== "") {
      var newitem = document.createElement("li");
      newitem.innerText = item.id + ' ' + item.text;
      newitem.setAttribute("id", item.id)
      listItem.appendChild(newitem);
    }
  })
};

function textDOM(response) {
  var output = document.querySelector("li");
  output.innerText = response.id + " " + response.text;
  output.setAttribute("id", response.text)
  document.body.appendChild(output)
};

addNewItemInput.addEventListener('click', function () {
  postItemToServer(newItemInput.value, textDOM);
});
