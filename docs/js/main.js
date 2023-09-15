function carousel() {
  const carouselTrack = document.querySelector(".carousel-track");
  const slides = document.querySelectorAll(".mySlides");
  const prevButton = document.getElementById("prev-button");
  const nextButton = document.getElementById("next-button");
  nextButton.addEventListener("click", nextSlide);
  prevButton.addEventListener("click", prevSlide);
  let slideIndex = 0;
  const slideWidth = slides[0].clientWidth;

  function updateCarousel() {
    carouselTrack.style.transform = `translateX(-${slideIndex * slideWidth}px)`;
  }

  function nextSlide() {
    slideIndex++;
    if (slideIndex >= slides.length) {
      slideIndex = 0;
    }
    updateCarousel();
  }

  function prevSlide() {
    slideIndex--;
    if (slideIndex < 0) {
      slideIndex = slides.length - 1;
    }
    updateCarousel();
  }
}

function cardsBackground() {
  let background = $(".texts-introduction-section");
  $(".card-left").hover(function() {
    $(".texts-introduction-section > .sectitle > h3").css("color", "white");
    background.css("background-image", "url(./img/klimt.png)");
  });
  $(".card-middle").hover(function() {
    background.css("background-image", "url(./img/script96_page.jpg)");
    $(".texts-introduction-section > .sectitle > h3").css("text-shadow", "none");
    $(".texts-introduction-section > .sectitle > h3").css("color", "black");
  });
  $(".card-right").hover(function() {
    $(".texts-introduction-section > .sectitle > h3").css("color", "white");
    background.css("background-image", "url(./img/making-of.png)");
  });
}

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
}

function populateSelector(zipped_elements) {
  zipped_elements.forEach(function (element) {
    var option = document.createElement("option");
    option.text = element[0].map(item => item.replace('#', ''));
    option.value = element[1] + ' ' + element[2] + ' ' + element[0];
    $("#scene-selector").append(option);
  });
  getSelectedScene();
};

function fetchAlignment() {
  return new Promise(function (resolve, reject) {
    var xhr = new XMLHttpRequest();
    var alignmentData = {
      tElements: [],
      bElements: [],
      sElements: [],
    };
    xhr.open("GET", "./src/scene-alignment.xml", true);
    xhr.onreadystatechange = function () {
      if (xhr.readyState == 4) {
        if (xhr.status == 200) {
          var xmlDoc = xhr.responseXML;
          var alignElements = xmlDoc.querySelectorAll(`link`);
          alignElements.forEach(function (alignElement) {
            targets = alignElement.getAttribute("target");
            var parts = targets.split(" ");
            var tElementsInLink = parts.filter((part) => part.startsWith("#T"));
            alignmentData.tElements.push(tElementsInLink);
            var bElementsInLink = parts.filter((part) => part.startsWith("#B"));
            alignmentData.bElements.push(bElementsInLink);
            var sElementsInLink = parts.filter((part) => part.startsWith("#S"));
            alignmentData.sElements.push(sElementsInLink);
          });
          resolve(alignmentData);
        } else {
          reject(xhr.statusText);
        }
      }
    };
    xhr.send();
  });
}

function fetchAndProcessXML(path, sceneNumbers, container) {
  const xhr = new XMLHttpRequest();
  xhr.open("GET", path, true);

  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      const xmlDoc = xhr.responseXML;

      if (xmlDoc) {
        const sceneIds = sceneNumbers.split(',').map(id => id.trim());

        sceneIds.forEach(sceneId => {
          const element = xmlDoc.querySelector(`div[type="scene"][*|id="${sceneId}"]`);
          if (element) {
            const text = element.textContent;
            $(container).append(text.replace(/\n *\n *\n/gm, "<br>"));
            console.log(text)
          } else {
            console.log(`Scene ${sceneId} not found in ${path}`);
          }
        });
      } else {
        console.error(`Failed to parse XML from ${path}`);
      }
    }
  };

  xhr.send();
}


function fetchTextContent(selectedSceneNumbers) {
    var xmlFiles = [
    { path: "./src/Arthur Schnitzler - Dream Story (2003, Green Integer).xml", sceneNumber: selectedSceneNumbers[0].replace(/#/g, ''), container: $("#left-text") },
    { path: "./src/eyes-wide-shut-1996-screenplay.xml", sceneNumber: selectedSceneNumbers[1].replace(/#/g, ''), container: $("#central-text") },
    { path: "./src/eyes-wide-shut-1999-transcription.xml", sceneNumber: selectedSceneNumbers[2].replace(/#/g, ''), container: $("#right-text") }
  ];
  xmlFiles.forEach((item) => {
    fetchAndProcessXML(item.path, item.sceneNumber, item.container);
  });
};

function fetchScreencaps(scenes) {
  var imageContainer = document.getElementById("image-container");
  sceneNumbers = scenes.split(",").map(function (scene) {
    return scene.trim().replace("#T", "");
  });
  $("#image-container").empty();
  $.getJSON(
    "./img/screencaps/folder_structure.json",
    function (folderStructure) {
      sceneNumbers.forEach(function (sceneNumber) {
        folder_name = "SCENE" + sceneNumber;
        if (folderStructure.hasOwnProperty(folder_name)) {
          file_list = folderStructure[folder_name];
          file_list.forEach(function (filename) {
            image_name =
              "./img/screencaps/SCENE" + sceneNumber + "/" + filename;
            var img = document.createElement("img");
            img.className = "screencap";
            img.src = image_name;
            imageContainer.appendChild(img);
          });
        }
      });
    }
  );
}

function getSelectedScene() {
  var selectedSceneNumber = $("#scene-selector").val().split(' ');
  fetchTextContent(selectedSceneNumber);
  fetchScreencaps(selectedSceneNumber[2]);
}

$(document).ready(function () {
  parallax();
  carousel();
  cardsBackground();
  fetchAlignment()
  .then(function (alignmentData) {
    zippedAlignmentData = alignmentData.tElements.map((tElements, index) => [tElements, alignmentData.bElements[index], alignmentData.sElements[index]]);
    populateSelector(zippedAlignmentData);
  })
  .catch(function (error) {
    console.error("Error fetching alignment:", error);
  });

  $("#scene-selector").change(function () {
    getSelectedScene();
    $(".comparison-item > pre").empty();

  });
});
