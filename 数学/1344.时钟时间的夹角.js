/**
 * @param {number} hour
 * @param {number} minutes
 * @return {number}
 */
var angleClock = function(hour, minutes) {
    const angleMinute = minutes * 6;
    const angleHour = hour * 30 + minutes / 2;
    const angle = Math.abs(angleMinute - angleHour);
    return Math.min(360 - angle, angle)
};