import http from "k6/http";

export const options = {
    stages: [
        { duration: "30s", target: 20 }, // Ramp up to 20 users over 30 seconds
        { duration: "10m", target: 20 }, // Stay at 20 users for 10 minutes
        { duration: "30s", target: 0 }, // Ramp down to 0 users over 30 seconds
    ],
};

export default function() {
    if (Math.random() < 0.05) {
        http.get("http://46.21.65.194:8080/");
    }
}