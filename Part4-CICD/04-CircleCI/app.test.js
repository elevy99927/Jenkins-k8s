// index.test.js
const { add } = require('./math');

test('adds 1 + 2 to equal 3', () => {
    expect(add(1, 2)).toBe(3);
});

test('adds -1 + -1 to equal -2', () => {
    expect(add(-1, -1)).toBe(-2);
});

