function parallax() {
  var image = document.querySelector(".parallax");
  var zoomFactor = parseFloat(image.getAttribute("data-zoom"));
  var scrollFactor = 0.001;

  window.addEventListener("scroll", function () {
    var scrollY = window.scrollY || window.pageYOffset;
    var zoomedScale = 1 + scrollY * scrollFactor * zoomFactor;

    // Limit the zoom effect
    if (zoomedScale > 1 + zoomFactor) {
      zoomedScale = 1 + zoomFactor;
    }

    image.style.transform = `scale(${zoomedScale})`;
  });
};

function sceneSelector() {
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "../../Arthur Schnitzler - Dream Story (2003, Green Integer).xml", true);
  xhr.onreadystatechange = function () {
    if (xhr.readyState == 4 && xhr.status == 200) {
      var xmlDoc = xhr.responseXML;
      var sceneElements = xmlDoc.querySelectorAll("div[type='scene']");
      sceneElements.forEach(function (sceneElement) {
        var option = document.createElement("option");
        option.text = sceneElement.getAttribute("n");
        option.value = sceneElement.getAttribute("n");
        $('#scene-selector').append(option);
      });
      getSelectedScene();
    }
  }
  xhr.send();
};

function fetchTextContent(selectedSceneNumber) {
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "./src/Arthur Schnitzler - Dream Story (2003, Green Integer).xml", true);
  xhr.onreadystatechange = function () {
    if (xhr.readyState == 4 && xhr.status == 200) {
      var xmlDoc = xhr.responseXML;
      var scene = xmlDoc.querySelector(`div[type='scene'][n='${selectedSceneNumber}']`);
      $('#left-text').empty().append(scene)
      console.log(scene)
    }
  }
  xhr.send();
};

function getSelectedScene() {
  var selectedSceneNumber = $('#scene-selector').val()
  fetchTextContent(selectedSceneNumber);
  $('#scene-selector').change(function () {
    selectedSceneNumber = $(this).val();
    fetchTextContent(selectedSceneNumber);
  });
};





$(document).ready(function() {
  parallax();
  sceneSelector();

});