var options = {
  rowOption1: {
    Monday: [],
    Tuesday: [],
    Wednesday: [],
    Thursday: [],
    Friday: [],
    Saturday: [],
  },
  rowOption2: {
    Monday: [],
    Tuesday: [],
    Wednesday: [],
    Thursday: [],
    Friday: [],
    Saturday: [],
  },
  rowOption3: {
    Monday: [],
    Tuesday: [],
    Wednesday: [],
    Thursday: [],
    Friday: [],
    Saturday: [],
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

function checkInput(e, courseId, course, dateInfo, rowOption) {
  const stringDate = JSON.stringify(dateInfo);

  var dates = stringDate.split("<CourseDate: ").map((e) => e.split(">")[0]);
  dates.shift();

  for (var date of dates) {
    dayOfWeek = date.split(" - ")[0];
    var idName = "box" + courseId + rowOption + dayOfWeek;

    // check if some object has same date value
    var sameDate = options[rowOption][dayOfWeek].filter((e) => e.date == date);

    if (!e.checked) {
      options[rowOption][dayOfWeek] = options[rowOption][dayOfWeek].filter(
        (e) => e.id != idName
      );
    } else {
      if (sameDate.length) {
        alert("Conflito de datas!");
        e.checked = false;
        break;
      } else {
        options[rowOption][dayOfWeek].push({
          id: idName,
          course: course,
          date: date,
        });

        // reorder the array by date
        options[rowOption][dayOfWeek].sort((a, b) => {
          return a.date > b.date ? 1 : -1;
        });
      }
    }

    updateBox();
  }
}
