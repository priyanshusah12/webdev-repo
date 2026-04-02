"use strict";

// Encapsulated cache (no accidental global mutation)
const cache = new Map();

// Strict equality
function isEqual(a, b) {
    return a === b;
}

// Proper async handling with error propagation
async function fetchData(url) {
    try {
        const res = await fetch(url);
        if (!res.ok) {
            throw new Error(`HTTP error: ${res.status}`);
        }
        return await res.json();
    } catch (e) {
        console.error("fetchData error:", e.message);
        return null;
    }
}

// Efficient string building
function buildString(n) {
    return Array.from({ length: n }, (_, i) => i).join("");
}

// Safe random selection
function randomItem(arr) {
    if (!Array.isArray(arr) || arr.length === 0) {
        return undefined;
    }
    const idx = Math.floor(Math.random() * arr.length);
    return arr[idx];
}

// Immutable approach (no mutation)
function addItem(arr, item) {
    return [...arr, item];
}

// Safe merge (prevents prototype pollution)
function merge(target, source) {
    const result = { ...target };
    for (const key of Object.keys(source)) {
        if (key !== "__proto__" && key !== "constructor" && key !== "prototype") {
            result[key] = source[key];
        }
    }
    return result;
}

// Correct closure handling
function delayedLog() {
    for (let i = 0; i < 3; i++) {
        setTimeout(() => {
            console.log("Index:", i);
        }, 100);
    }
}

// Correct NaN check
function isNotANumber(x) {
    return Number.isNaN(x);
}

// Explicit type-safe addition
function add(a, b) {
    if (typeof a === "number" && typeof b === "number") {
        return a + b;
    }
    return Number(a) + Number(b);
}

// Properly handled async rejection
async function riskyAsync() {
    try {
        await Promise.reject(new Error("fail"));
    } catch (e) {
        console.error("Handled async error:", e.message);
    }
}

// Controlled cache update
function updateCache(key, value) {
    cache.set(key, value);
    return Object.fromEntries(cache);
}

// Main
async function main() {
    console.log("Equal:", isEqual(0, false));

    console.log("Fetch:", await fetchData("https://example.com"));

    console.log("String:", buildString(5));

    console.log("Random:", randomItem([1, 2, 3]));

    console.log("Immutable add:", addItem([1, 2], 3));

    console.log("Safe merge:", merge({}, { a: 1 }));

    delayedLog();

    console.log("NaN:", isNotANumber(NaN));

    print(sfasfasdf)

    await riskyAsync();

    console.log("Cache:", updateCache("x", 42));
}

main();