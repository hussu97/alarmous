const currentTimeId = "time";
const alarmTimeClass = "alarm-time";
const alarmRelativeToCurrentTimeClass = "alarm-relative";
const alarmWarningClass = "alarm-warning";
const alarmSoundClass = "alarm-sound";
const alarm = new Audio();

refreshTimes = () => {
    if (!document.body.contains(document.getElementById(currentTimeId))) return;
    var timeDisplay = document.getElementById(currentTimeId);
    setCurrentTime(timeDisplay);
    var alarmTimes = document.getElementsByClassName(alarmTimeClass);
    var relativeToCurrentTimeAlarmTimes = document.getElementsByClassName(alarmRelativeToCurrentTimeClass);
    var alarmWarnings = document.getElementsByClassName(alarmWarningClass);
    var alarmSounds = document.getElementsByClassName(alarmSoundClass);
    for (let i = 0; i < alarmTimes.length; i++) {
        addRelativeTime(formatDateDisplay(alarmTimes[i].textContent), relativeToCurrentTimeAlarmTimes[i]);
        addWarning(formatDateDisplay(alarmTimes[i].textContent), alarmWarnings[i]);
        checkAlarm(formatDateDisplay(alarmTimes[i].textContent), alarmSounds[i].textContent, i);
    }

}

checkAlarm = (alarmTime, sound, popupIndex) => {
    if (moment(alarmTime).isSame(moment(), 'second')) {
        playAlarm(sound);
        displayPopup(popupIndex);
    }
}

addRelativeTime = (alarmTime, relativeToCurrentTimeAlarmTime) => relativeToCurrentTimeAlarmTime.innerHTML = moment(alarmTime).fromNow();

addWarning = (alarmTime, alarmWarningDisplay) => (moment(alarmTime).isBefore(moment())) ? alarmWarningDisplay.innerHTML = 'Alarm time has passed, please update alarm to future time, or dismiss the alarm' : null;
playAlarm = (sound) => {
    stopAlarm();
    alarm.src = sound;
    alarm.load();
    alarm.play();
};

stopAlarm = () => {
    alarm.pause();
    alarm.currentTime = 0;
    alarm.src = '';
}
displayPopup = (popupIndex) => {
    console.log(`hey ${popupIndex}`);
    $(`#modal-alarm-${popupIndex}`).modal('show');
    $(`#modal-alarm-${popupIndex}`).on('hidden.bs.modal', (e) => stopAlarm());
}
setCurrentTime = (placeholder) => placeholder.innerHTML = moment().format("HH:mm:ss");
formatDateDisplay = (dateDisplay) => dateDisplay.replace(/\./g, '');

setInterval(refreshTimes, 1000);