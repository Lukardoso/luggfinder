// Post json data on server:
export function sendToServer(jsonPayload) {
    fetch("http://127.0.0.1:5000/update_process", {
    method: "POST",
    body: JSON.stringify(jsonPayload),
    headers: {
        "Content-type": "application/json; charset=UTF-8"
        }
    });
}
