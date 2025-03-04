const express = require('express');
const router = express.Router();
const SpiderController = require('../controller/SpiderController');

router.post('/getTitle', SpiderController.getTitle);

module.exports = router;