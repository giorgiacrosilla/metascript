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
  xhr.open("GET", "./src/Arthur Schnitzler - Dream Story (2003, Green Integer).xml", true);
  xhr.onreadystatechange = function () {
    if (xhr.readyState == 4 && xhr.status == 200) {
      var xmlDoc = xhr.responseXML;
      var sceneElements = xmlDoc.querySelectorAll("div[type='scene']:not([n='none'])");
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
    }
  }
  xhr.send();
};

function fetchScreencaps(scenes) {
  var imageContainer = document.getElementById("image-container");
  sceneNumbers = scenes.split(",").map(function (scene) {
    return scene.trim();
  });
  $("#image-container").empty();

  sceneNumbers.forEach(function (sceneNumber) {
    $.ajax({
      url: "/docs/img/screencaps/SCENE" + sceneNumber + "/",
      success: function (data) {
        $(data)
          .find("a:contains(" + ".png" + ")")
          .each(function () {
            var filename = this.href
              .replace(window.location.host, "")
              .replace("http://", "");
            var img = document.createElement("img");
            img.className = "screencap";
            img.src = filename;
            imageContainer.appendChild(img);
          });
      },
    });
  });

}

function getSelectedScene() {
  var selectedSceneNumber = $('#scene-selector').val()
  fetchTextContent(selectedSceneNumber);
  $('#scene-selector').change(function () {
    selectedSceneNumber = $(this).val();
    fetchTextContent(selectedSceneNumber);
    fetchScreencaps(selectedSceneNumber)
  });
};





$(document).ready(function() {
  parallax();
  fetchScreencaps('4');
  sceneSelector();
});