const express = require("express");
const env = require("dotenv");
const cookieParser = require("cookie-parser");

const app = express();
app.use(cookieParser());
env.config({ path: "./config.env" });

const PORT = 3000;

app.use(express.json());
app.use(require("./router/route"));

app.listen(PORT, () => {
    console.log('server running');
});