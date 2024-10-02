// background.js

// This event is fired when the service worker is registered
chrome.runtime.onInstalled.addListener(() => {
    console.log('Extension installed');
});

// Listen for messages from popup or content scripts
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.message === "hello") {
        sendResponse({ message: "Hello from background.js!" });
    }
});

// Example of a simple listener for alarms
chrome.alarms.onAlarm.addListener((alarm) => {
    console.log('Alarm triggered:', alarm.name);
});