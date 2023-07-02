myDiv = document.createElement("Div");
myDiv.className = "center-flex MyDiv";
document.body.prepend(myDiv);
myDivEl = document.getElementsByClassName("MyDiv")[0];
ghost_level = 0;
if (document.getElementsByClassName("room-title").length < 1) {
  myDivEl.innerHTML = "WELCOME";
} else if (
  document.getElementsByClassName("room-title")[0].innerHTML ==
  "Practice Racetrack"
) {
  myDivEl.innerHTML = "ACCURACY";
} else {
  myDivEl.innerHTML = "SPEED";
}
document.addEventListener("keydown", (e) => {
  if (e.isComposing || (e.key === "L" && e.ctrlKey && e.shiftKey)) {
    var numberPattern = /\d+/g;
    var floatPattern = /[+-]?\d+(\.\d+)?/g;
    speed = document.getElementsByClassName("tblOwnStatsNumber")[0].innerHTML.match(numberPattern)
    accuracy = document.getElementsByClassName("tblOwnStatsNumber tblOwnStatsNumber-bad")[0].innerHTML.match(floatPattern);
    if (
      document.getElementsByClassName("gwt-InlineHTML").length > 0 &&
      document.getElementsByClassName("gwt-InlineHTML")[0].innerHTML.match(/ghost/)
    ) {
      ghost_level += 1;
      myDivEl = document.getElementsByClassName("MyDiv")[0];
      myDivEl.innerHTML = "YES<br>Ghost level: " + ghost_level +"<br>speed: "+ speed +"<br> acc: " + accuracy;
    } else {
      ghost_level += 0;
      myDivEl = document.getElementsByClassName("MyDiv")[0];
      myDivEl.innerHTML = "NO " + speed + " " + accuracy;
    }
  }
  // do something
});
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  console.log("REQUEST", request)
  if (request.req === "joinSinglePlayerGame") {
    myDivEl.innerHTML = "ACCURACY";
  } else if (request.req === "joinStandaloneGame") {
    myDivEl.innerHTML = "SPEED";
  } else if (request.req == "leaveGame") {
    myDivEl.innerHTML = "WELCOME";
  } else if (request.req == "end") {
    try {
      console.log(document.getElementsByClassName("tblOwnStatsNumber"));
      speed = document.getElementsByClassName("tblOwnStatsNumber")[0].textContent;
      console.log("SPEED", speed);
      speed = speed.split([" "])[0];
      console.log(speed);
    } catch (err) {}
  }
});
