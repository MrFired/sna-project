import http from "k6/http";
import { sleep } from "k6";

export const options = {
    stages: [
        { duration: "1m", target: 100 }, // Ramp up from 0 to 100 users in 1 minute
        { duration: "2m", target: 100 }, // Stay at 100 users for 2 minutes
        { duration: "1m", target: 0 }, // Ramp down from 100 to 0 users in 1 minute
    ],
};

export default function() {
    const res = http.get("http://46.21.65.194:8080/");
    sleep(1);
}