const express = require('express');
const app = express();
const port = 8080;
const task = require('./schedule/task');
const mysql = require('./sequelize/database');
const bodyParser = require('body-parser');
const ServerWatchRouter = require('./routes/ServerWatchRouter')
const UserRouter = require('./routes/UserRouter');
const SpiderRouter = require('./routes/SpiderRouter');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use('/serverWatch', ServerWatchRouter);
app.use('/user', UserRouter);
app.use('/spider', SpiderRouter);

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
