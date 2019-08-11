function refreshTime() {
    var timeDisplay = document.getElementById("time");
    var dateString = new Date().toLocaleTimeString("en-US", { timeZone: "Asia/Dubai", hour12: false });
    timeDisplay.innerHTML = dateString;
}

setInterval(refreshTime, 1000);