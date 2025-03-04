const express = require('express');
const router = express.Router();
const ServerWatchController = require('../controller/ServerWatchController');

router.post('/serverOperate', ServerWatchController.ServerOperate);

module.exports = router;