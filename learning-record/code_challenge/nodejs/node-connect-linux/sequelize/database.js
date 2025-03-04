// database.js
const { Sequelize } = require('sequelize');

const sequelize = new Sequelize('database_node_example', 'root', '123456', {
  host: 'localhost',
  dialect: 'mysql',
});

module.exports = sequelize;
