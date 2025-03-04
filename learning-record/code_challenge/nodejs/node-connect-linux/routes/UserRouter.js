const express = require('express');
const router = express.Router();
const UserController = require('../controller/UserController');

router.get('/:id', UserController.getUser);
router.get('/', UserController.getAll);
router.post('/', UserController.createUser);


// Define the routes and map them to controller functions
// router.get('/', userController.getAllUsers);
// router.get('/:id', userController.getUserById);
// router.post('/', userController.createUser);
// router.put('/:id', userController.updateUser);
// router.delete('/:id', userController.deleteUser);

module.exports = router;