import http from "k6/http";

export const options = {
    stages: [
        { duration: "20s", target: 50 }, // Ramp up from 0 to 50 users in 20 seconds
        { duration: "1m", target: 50 }, // Stay at 50 users for 1 minutes
        { duration: "20s", target: 0 }, // Ramp down from 50 to 0 users in 20 seconds
    ],
};

export default function() {
    http.get("http://46.21.65.194:8080/");
}