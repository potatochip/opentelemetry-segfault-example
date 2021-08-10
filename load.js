// Run with below for 10 virutal users and 1000 iterations
// ❯ k6 run --vus 10 --iterations 1000 ugc.js
import { check } from 'k6';
import http from 'k6/http';

export default function () {
    var url = 'http://localhost:8000/';
    // objects are form url encoded
    var payload = JSON.stringify({
        "text": "tacocat",
    });
    let res = http.get(url, payload);

    check(res, {
        'is status 200': (r) => r.status === 200,
    });
}
