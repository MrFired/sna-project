import http from "k6/http";

export const options = {
    stages: [
        { duration: "5s", target: 150 }, // Ramp up from 0 to 150 users in 5 seconds
        { duration: "20s", target: 150 }, // Stay at 150 users for 20 seconds
        { duration: "5s", target: 0 }, // Ramp down from 150 to 0 users in 5 seconds
    ],
};

export default function() {
    http.get("http://46.21.65.194:8080/");
}