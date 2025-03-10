/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
  return {
      toBe: function(check) {
          if (val === check) {
              return true;
          }
          else {
              throw "Not Equal";
          }
      },
      notToBe: function(check) {
          if (val !== check) {
              return true;
          }
          else {
              throw "Equal";
          }
      }
  }
};

/**
* expect(5).toBe(5); // true
* expect(5).notToBe(5); // throws "Equal"
*/