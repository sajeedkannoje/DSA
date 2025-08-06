/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    s = s.trim(); // Remove leading and trailing spaces
    let length = 0;

    for (let i = s.length - 1; i >= 0; i--) {
        if (s[i] === ' ') {
            break; // Stop counting when a space is found
        }
        length++;
    }

    return length;
};
