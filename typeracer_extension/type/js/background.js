// console.log("BACKGROUND SCRIPT");
// chrome.commands.onCommand.addListener(function (command) {
//   console.log(command);
//   if (command === "check_speed") {
//     console.log(document.getElementsByClassName('room-title')[0])
//   }
// });
async function sendMsg(msg) {
  try {
    const [tab] = await chrome.tabs.query({
      active: true,
      lastFocusedWindow: true,
    });
    await chrome.tabs.sendMessage(tab.id, { req: msg });
  } catch {}
}

important_req_id = 0;
important_req_name = "";
var enc = new TextDecoder("utf-8");
chrome.webRequest.onBeforeRequest.addListener(
  function (details) {
    // console.log(details);
    if (details.type == "xmlhttprequest") {
      req_body = enc.decode(details.requestBody.raw[0].bytes).split("|");
      try {
        if (req_body[13].length > 10) {
          important_req_id = details.requestId;
          important_req_name = 'end';
          console.log(req_body)
        }

        if (
          req_body[6] == "joinSinglePlayerGame" ||
          req_body[6] == "joinStandaloneGame" ||
          req_body[6] == "leaveGame"
        ) {
          important_req_id = details.requestId;
          important_req_name = req_body[6];
        }
      } catch {}
    }
  },
  { urls: ["https://*.typeracer.com/*"] },
  ["requestBody"]
);
chrome.webRequest.onCompleted.addListener(
  function (details) {
    if (details.type == "xmlhttprequest") {
      // console.log(details.requestId, important_req_id)
      if (details.requestId == important_req_id) {
        if (important_req_name == 'end') {
          console.log(details)
        }
      }
    }
  },
  { urls: ["https://*.typeracer.com/*"] }
);
