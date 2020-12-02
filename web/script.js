
var hintsViews = [];
var convertWord = true;

function convert() {
    clearHints();
    if (convertWord == true) {
        createKey();
    } else {
        createWord();
    }
}

function changeConversionType() {
    if (convertWord == true) {
        setKeyConversion();
    } else {
        setWordConversion();
    }
}

function setWordConversion() {
    convertWord = true;
    var title = document.getElementById("title");
    var desc = document.getElementById("desc");
    title.innerHTML = "Ключ по слову";
    desc.innerHTML = "Введите слово, по которому хотите создать ключ";
}

function setKeyConversion() {
    convertWord = false;
    var title = document.getElementById("title");
    var desc = document.getElementById("desc");
    title.innerHTML = "Слово по ключу";
    desc.innerHTML = "Введите ключ, по которому хотите создать слово";
}

async function createKey() {
  var word = document.getElementById("word").value;
  var keyView = document.getElementById("key");
  var postProcessContainer = document.getElementById("post-process");

  if (word != "" && /^[a-zA-Z]+$/.test(word)) {
      var keyValue = await eel.create_key(word)();
      var hintsValues = await eel.get_key_hints()();

      postProcessContainer.style.visibility = "visible";
      keyView.innerHTML = keyValue;

      var i;
      for (i = 0; i < hintsValues.length; i++) {
        createHintView(i+1, hintsValues[i][0], hintsValues[i][1]);
      }
   } else {
       alert("Пожалуйста, введите подходящее значение\nВозможны только символы латинского алфавита");
   }
}

async function createWord() {
    var key = document.getElementById("word").value;
    var wordView = document.getElementById("key");
    var postProcessContainer = document.getElementById("post-process");

    if (key != "" && /^[a-zA-z0-9]+$/.test(key)) {
        var wordValue = await eel.create_word(key)();
        var hintsValues = await eel.get_word_hints()();

         postProcessContainer.style.visibility = "visible";
         wordView.innerHTML = wordValue;

         var i;
         for (i = 0; i < hintsValues.length; i++) {
            createHintView(i+1, hintsValues[i][0], hintsValues[i][1]);
         }
     } else {
       alert("Пожалуйста, введите подходящее значение\nВозможны только цифры и символы латинского алфавита");
     }
}

function createHintView(index, title, key) {
  var bg = createHintBg();
  var circle = createIndexView(index);
  bg.appendChild(circle);

  var titleView = createTitleHintView(title);
  bg.appendChild(titleView);

  if (key != "0") {
    var keyView = createKeyValueView(key);
    bg.appendChild(keyView);
  }

  var container = document.getElementById("hints");
  container.appendChild(bg);
  hintsViews.push(bg);
}

function createKeyValueView(key) {
  var view = document.createElement("span");
  view.style.fontFamily = "GilroyBold";
  view.style.fontSize = "22px";
  view.style.color = "#FFF";
  view.style.display = "block";
  view.style.marginTop = "10px";
  view.innerHTML = key;
  return view;
}

function createTitleHintView(title) {
  var view = document.createElement("span");
  view.style.fontFamily = "GilroyMedium";
  view.style.fontSize = "17px";
  view.style.color = "#FFF";
  view.style.display = "block";
  view.style.marginTop = "10px";
  view.innerHTML = title;
  return view;
}

function createIndexView(num) {
  var circle = document.createElement("div")
  var numView = document.createElement("span")

  circle.style.backgroundColor = "#616670";
  circle.style.width = "25px";
  circle.style.height = "25px";
  circle.style.borderRadius = "12.5px";
  circle.style.display = "flex";
  circle.style.justifyContent = "center";
  circle.style.alignItems = "center";

  numView.style.fontFamily = "GilroyBold";
  numView.style.fontSize = "16px";
  numView.style.color = "#FFF";
  numView.innerHTML = num;

  circle.appendChild(numView);

  return circle
}

function createHintBg() {
  var bg = document.createElement("div");
  bg.style.backgroundColor = "#36393F";
  bg.style.display = "inline-block";
  bg.style.justifyContent = "center";
  bg.style.alignItems = "center";
  bg.style.borderRadius = "0px 10px 10px 10px";
  bg.style.padding = "10px";
  bg.style.marginLeft = "25px";
  bg.style.marginRight = "25px";
  bg.style.marginTop = "25px";
  return bg;
}

 function clearHints() {
   var i;
   for (i = 0; i < hintsViews.length; i++) {
        hintsViews[i].remove();
   }
   hintsViews = [];
 }
