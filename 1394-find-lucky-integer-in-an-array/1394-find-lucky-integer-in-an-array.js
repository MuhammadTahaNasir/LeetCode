/**
 * @param {number[]} arr
 * @return {number}
 */
var findLucky = function(arr) {
    const freq = new Map();

    // Count frequency of each number
    for (let num of arr) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    let result = -1;

    // Check for lucky numbers
    for (let [num, count] of freq.entries()) {
        if (num === count) {
            result = Math.max(result, num);
        }
    }

    return result;
};
