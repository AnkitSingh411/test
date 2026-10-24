// Sample JavaScript module with a few small utilities.
const greetingPrefix = 'Hello';
const defaultName = 'World';

function greet(name) {
  const displayName = name || defaultName;
  return greetingPrefix + ', ' + displayName + '!';
}

function add(a, b) {
  return a + b;
}

function multiply(a, b) {
  return a * b;
}

function isEven(value) {
  return value % 2 === 0;
}

function factorial(n) {
  let result = 1;
  for (let i = 2; i <= n; i++) {
    result = result * i;
  }
  return result;
}

function sumArray(numbers) {
  let total = 0;
  for (const number of numbers) {
    total += number;
  }
  return total;
}

function average(numbers) {
  if (numbers.length === 0) {
    return 0;
  }
  return sumArray(numbers) / numbers.length;
}

function findLargest(numbers) {
  let largest = numbers[0];
  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] > largest) {
      largest = numbers[i];
    }
  }
  return largest;
}

function countEven(numbers) {
  let count = 0;
  for (const number of numbers) {
    if (isEven(number)) {
      count++;
    }
  }
  return count;
}

function formatList(items) {
  return items.join(', ');
}

const sampleNumbers = [3, 8, 12, 5, 20, 7];
const sampleNames = ['Ada', 'Grace', 'Linus'];

console.log(greet('Ada'));
console.log('Sum:', sumArray(sampleNumbers));
console.log('Average:', average(sampleNumbers));
console.log('Largest:', findLargest(sampleNumbers));
console.log('Even count:', countEven(sampleNumbers));
console.log('Factorial of 5:', factorial(5));
console.log('Names:', formatList(sampleNames));
console.log('2 + 3 =', add(2, 3));
console.log('4 * 6 =', multiply(4, 6));

export { greet, add, multiply, isEven, factorial, sumArray, average, findLargest, countEven, formatList };
export default greet;
