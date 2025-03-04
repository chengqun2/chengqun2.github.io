// sync.js
const sequelize = require('./database');
const User = require('../models/user');

(async () => {
  try {
    await sequelize.authenticate();
    console.log('Connection has been established successfully.');

    // Sync all models
    await sequelize.sync({ force: true });
    console.log('All models were synchronized successfully.');

    // Create a new user
    const user = await User.create({
      firstName: 'John',
      lastName: 'Doe',
      email: 'john.doe@example.com',
    });
    console.log('User created:', user.toJSON());

  } catch (error) {
    console.error('Unable to connect to the database:', error);
  } finally {
    await sequelize.close();
  }
})();
