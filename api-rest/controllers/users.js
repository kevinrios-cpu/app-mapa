const { create } = require('../services/users/create');

async function _create(parking_user) {
    return await create(parking_user);
}

module.exports = {
    _create
}