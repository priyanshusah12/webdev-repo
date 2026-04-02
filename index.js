// Global mutable state
var cache = {};

// == vs === confusion
function isEqual(a, b) {
    if (a == b) {  // loose equality
        return true;
    }
    return false;
}

// Async bug: missing await
async function fetchData(url) {
    try {
        let res = fetch(url); // forgot await
        return res.json();    // res is a Promise, not Response
    } catch (e) {
        return null; // swallows error
    }
}

// Inefficient loop + accidental global
function buildString(n) {
    str = ""; // missing var/let/const → global leak
    for (let i = 0; i < n; i++) {
        str += i; // inefficient concatenation
    }
    return str;
}

// Off-by-one + possible undefined
function randomItem(arr) {
    let idx = Math.floor(Math.random() * (arr.length + 1));
    return arr[idx];
}

// Mutation of input parameter
function addItem(arr, item) {
    arr.push(item);
    return arr;
}

// Prototype pollution risk
function merge(target, source) {
    for (let key in source) {
        target[key] = source[key]; // no hasOwnProperty check
    }
    return target;
}

// setTimeout closure bug
function delayedLog() {
    for (var i = 0; i < 3; i++) {
        setTimeout(function () {
            console.log("Index:", i); // always 3
        }, 100);
    }
}

// NaN comparison bug
function isNotANumber(x) {
    return x === NaN; // always false
}

// Type coercion weirdness
function add(a, b) {
    return a + b; // "1" + 2 = "12"
}

// Unhandled promise rejection
function riskyAsync() {
    Promise.reject("fail"); // no catch
}

// Cache with hidden side effects
function updateCache(key, value) {
    cache[key] = value;
    return cache;
}

// Main
function main() {
    console.log("Equal:", isEqual(0, false));
    console.log("Fetch:", fetchData("https://example.com"));
    console.log("String:", buildString(5));
    console.log("Random:", randomItem([1,2,3]));
    console.log("Mutate:", addItem([1,2], 3));
    console.log("Merge:", merge({}, {a:1, __proto__: {polluted: true}}));
    delayedLog();
    console.log("NaN:", isNotANumber(NaN));
    console.log("Add:", add("1", 2));
    riskyAsync();
    console.log("Cache:", updateCache("x", 42));
}

main();