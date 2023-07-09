const express = require("express");
const shayariRouter = express.Router();
const { shayariPostController } = require("../controllers/shayariController");
shayariRouter.post('/shayari', shayariPostController);
module.exports = { shayariRouter };