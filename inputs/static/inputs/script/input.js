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

  var div = document.createElement("div");
  div.id = "box" + courseId + rowOption + day;
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

  return;
}

function checkInput(e, courseId, course, dateInfo, rowOption) {
  const stringDate = JSON.stringify(dateInfo);

  var dates = stringDate.split("<CourseDate: ").map((e) => e.split(">")[0]);
  dates.shift();

  //   console.log(e, courseId, course, dates);
  //   if (e.checked) {
  //     option1.push(courseId);

  //   for (var date of dates) {
  //     createBox(course, date, rowOption);
  //   }

  if (!e.checked) {
    for (var date of dates) {
      dayOfWeek = date.split(" - ")[0];
      var idName = "box" + courseId + rowOption + dayOfWeek;
      document.getElementById(idName).remove();
      options[rowOption][dayOfWeek] = options[rowOption][dayOfWeek].filter(
        (e) => e.id != idName
      );
    }
  } else {
    for (var date of dates) {
      dayOfWeek = date.split(" - ")[0];
      var idName = "box" + courseId + rowOption + dayOfWeek;
      createBox(course, date, rowOption);
      options[rowOption][dayOfWeek].push({
        id: idName,
        course: course,
        date: date,
      });
    }
  }
}
