var options = {
  rowOption1: {
    Monday: [],
    Tuesday: [],
    Wednesday: [],
    Thursday: [],
    Friday: [],
    // Saturday: [],
  },
  rowOption2: {
    Monday: [],
    Tuesday: [],
    Wednesday: [],
    Thursday: [],
    Friday: [],
    // Saturday: [],
  },
  rowOption3: {
    Monday: [],
    Tuesday: [],
    Wednesday: [],
    Thursday: [],
    Friday: [],
    // Saturday: [],
  },
};

function createBox(course, date, rowOption) {
  var courseId = course.split(". ")[0];
  var courseName = course.split(". ")[1];
  var day = date.split(" - ")[0];
  var hour = date.split(" - ")[1];

  var idName = "box" + courseId + rowOption + day;

  var div = document.createElement("div");
  div.id = idName;
  div.className = "calendarClassBox";

  var span = document.createElement("span");
  span.innerHTML = hour;
  div.appendChild(span);

  var p = document.createElement("p");
  p.innerHTML = courseName;
  div.appendChild(p);

  document
    .getElementById(rowOption)
    .getElementsByClassName("columnsDays " + day)[0]
    .appendChild(div);
}

function updateBox() {
  // delete all elements with className "calendarClassBox"
  var elements = document.getElementsByClassName("calendarClassBox");
  while (elements.length > 0) {
    elements[0].parentNode.removeChild(elements[0]);
  }

  for (var rowOption in options) {
    for (var day in options[rowOption]) {
      for (var course in options[rowOption][day]) {
        createBox(
          options[rowOption][day][course]["course"],
          options[rowOption][day][course]["date"],
          rowOption
        );
      }
    }
  }
}

function checkInput(e, courseId, course, dateInfo, rowOption, ects) {
  const stringDate = JSON.stringify(dateInfo);

  var dates = stringDate.split("<CourseDate: ").map((e) => e.split(">")[0]);
  dates.shift();

  for (var date of dates) {
    dayOfWeek = date.split(" - ")[0];
    var idName = "box" + courseId + rowOption + dayOfWeek;

    // check if some object has same date value
    var sameDate = options[rowOption][dayOfWeek].filter((e) => e.date == date);

    var sameDateOtherDate = 0;

    if (dates.length == 2 && dates.indexOf(date) == 0) {
      var secondElement = dates[1];
      var dayOfWeekSecondElement = secondElement.split(" - ")[0];
      sameDateOtherDate = options[rowOption][dayOfWeekSecondElement].filter(
        (e) => e.date == secondElement
      );
    }

    if (!e.checked) {
      options[rowOption][dayOfWeek] = options[rowOption][dayOfWeek].filter(
        (e) => e.id != idName
      );
    } else {
      if (sameDate.length || sameDateOtherDate.length) {
        // alert("Date Conflict!");
        Swal.fire(
          "Oops...",
          "You can not select classes that are simultaneous!",
          "error"
        );
        e.checked = false;
        break;
      } else {
        options[rowOption][dayOfWeek].push({
          id: idName,
          course: course,
          date: date,
          ects: ects,
        });

        // reorder the array by date
        options[rowOption][dayOfWeek].sort((a, b) => {
          return a.date > b.date ? 1 : -1;
        });
      }
    }

    updateBox();
    sumEcts(rowOption);
  }
}

function clearOptions(rowOption, idCheckbox) {
  for (var day in options[rowOption]) {
    options[rowOption][day] = [];
  }

  var checkboxes = document.getElementsByClassName(idCheckbox);
  for (var checkbox of checkboxes) {
    checkbox.checked = false;
  }
  updateBox();
  sumEcts(rowOption);
}

function sumEcts(rowOption) {
  var dict = {};
  for (var day in options[rowOption]) {
    for (var course in options[rowOption][day]) {
      let curso = options[rowOption][day][course]["course"];
      let ects = options[rowOption][day][course]["ects"];
      if (!(curso in dict)) {
        dict[curso] = ects;
      }
    }
  }

  var somaEcts = 0;
  for (var key in dict) {
    somaEcts += parseInt(dict[key]);
  }

  var p = document.getElementsByClassName(`sumEcts ${rowOption}`);
  p[0].innerHTML = "Sum of ECTS: " + somaEcts;

  console.log("ESSE É O ROWOPTION ", rowOption)
  var nome = "ECTS"
  if (rowOption == 'rowOption1'){
    nome += "1" ;
  }
  else if (rowOption == 'rowOption2'){
    nome+="2";
  } 
  else{
    nome+="3";
  }

  console.log("ESSE É O NOME: ", nome)
  document.getElementById(nome).setAttribute('value', somaEcts)
  console.log("ESSE É O VALUE: ", document.getElementById(nome).setAttribute('value', somaEcts))
}

// function that refresh p tag value with ECTs sum
function refreshEcts(rowOption, idCheckbox) {
  var dict = {};
  for (var day in options[rowOption]) {
    for (var course in options[rowOption][day]) {
      let curso = options[rowOption][day][course]["course"];
      let ects = options[rowOption][day][course]["ects"];
      if (!(curso in dict)) {
        dict[curso] = ects;
      }
    }
  }

  var somaEcts = 0;
  for (var key in dict) {
    somaEcts += parseInt(dict[key]);
  }

  var p = document.getElementsByClassName("sumEcts");
  p[0].innerHTML = "Sum of ECTS: " + somaEcts;

}
